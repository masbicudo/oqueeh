from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def wait_for(driver, xpath):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    return WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))

def wait_visible(driver, xpath):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def iter_stream_lines(stream, timeout=None):
    from threading  import Thread
    from queue import Queue, Empty

    def enqueue_output(out, queue):
        for line in out:
            queue.put(line)
        out.close()

    q = Queue()
    t = Thread(target=enqueue_output, args=(stream, q))
    t.daemon = True # thread dies with the program
    t.start()

    # read line without blocking
    if timeout is None:
        get = lambda: q.get_nowait()
    else:
        get = lambda: q.get(timeout=timeout)

    while True:
        try:  line = get()
        except Empty:
            yield None
        else: # got line
            yield line

def run_server():
    import subprocess
    import sys
    ON_POSIX = 'posix' in sys.builtin_module_names
    cmd = f"cmd /c bundle exec jekyll serve --port 9875 --host 0.0.0.0"
    proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            close_fds=ON_POSIX,
            universal_newlines=True,
        )

    import re
    re_addr = re.compile(r"^\s*Server address: (.*)\s*$")
    re_running = re.compile(r"\bServer running\b")
    running = False
    addr = None
    for line in iter_stream_lines(proc.stdout, timeout=1):
        if line is not None:
            sys.stdout.write(line)
            match = re_addr.fullmatch(line)
            if match is not None:
                addr = match[1]
            if re_running.search(line) is not None:
                running = True
        if addr is not None and running == True:
            break

    addr = addr.replace("0.0.0.0", "localhost")
    return addr

def set_viewport_size(driver, width, height):
    # ref: https://stackoverflow.com/questions/37181403/how-to-set-browser-viewport-size
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

class TestInfo(object):
    def __init__(self) -> None:
        super().__init__()
        self.address = run_server()
        self.browser = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
            )
        html = ""
        with open("ui-test.html", "r") as fp:
            html = fp.read()
        self.browser.execute_script("""
            ((html) =>
            {
                document.open('text/html')
                document.write(html)
                document.close()
            })
            .apply(null, arguments)
            """, html)

    def test_portrait(self):
        # ref: https://deviceatlas.com/blog/most-used-smartphone-screen-resolutions
        self.browser.maximize_window()
        wait_for(self.browser, r'//*[@id="TEST_FRAME"]')
        self.browser.execute_script(f"""
            (() =>
            {{
                var iframe = document.getElementById('TEST_FRAME')
                iframe.style.width = "{1080/3}px"
                iframe.style.height = "{1920/3}px"
                iframe.src = "{self.address}"
            }})
            .apply(null, arguments)
            """)

    def do_test(self, path):
        iframe = wait_for(self.browser, r'//*[@id="TEST_FRAME"]')
        self.browser.execute_script(f"""
            (() =>
            {{
                var iframe = document.getElementById('TEST_FRAME')
                iframe.src = "{self.address}/{path}"
            }})
            .apply(null, arguments)
            """)
        self.browser.switch_to.frame(iframe)
        # TODO: do automated tests
        self.browser.switch_to.parent_frame()
        command = None
        while command is None:
            try:
                command = wait_visible(self.browser, r'//*[@id="COMMAND"]')
            except TimeoutException:
                pass
        value = command.get_attribute("data-value")
        self.browser.execute_script(f"""
            (() =>
            {{
                var command = document.getElementById('COMMAND')
                command.style.display = "none"
            }})
            .apply(null, arguments)
            """)
        return value

def do_tests():
    t = TestInfo()
    tests = [
        {"path": "postgresql/connect-to-database-via-cli", "accepted": False},
        {"path": "postgresql/drop-table-if-exists", "accepted": False},
    ]
    for test_item in tests:
        while True:
            t.test_portrait()
            action = t.do_test(test_item["path"])
            if action == "ACCEPT":
                test_item["accepted"] == True
                break
            if action == "REJECT":
                break
    return None

def main():
    do_tests()

if __name__ == "__main__":
    main()
