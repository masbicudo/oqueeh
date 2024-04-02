#file=en-US/python/remove-spaces-at-end-of-string.md
    ---
    title: Remove spaces at end of string in Python
    ---

    <ans>
    ```python
    "MASBicudo  ".rstrip()
    ```
    </ans>

    Result is `"MASBicudo"`.

#file=en-US/python/remove-spaces-at-start-of-string.md
    ---
    title: Remove spaces at start of string in Python
    ---

    <ans>
    ```python
    "  MASBicudo".lstrip()
    ```
    </ans>

    Result is `"MASBicudo"`.

#file=en-US/python/remove-spaces-surrounding-string.md
    ---
    title: Remove spaces surrounding string in Python
    ---

    <ans>
    ```python
    "  MASBicudo  ".strip()
    ```
    </ans>

    Result is `"MASBicudo"`.

    This removes spaces from both ends of a string.

#file=en-US/python/remove-characters-at-end-of-string.md
    ---
    title: Remove characters at end of string in Python
    ---

    <ans>
    ```python
    "MASBicudo?!".rstrip("!?.")
    ```
    </ans>

    Result is `"MASBicudo"`.

    This removes any of the characters from the given string.
    Order does not matter.

#file=en-US/python/remove-characters-at-start-of-string.md
    ---
    title: Remove characters at start of string in Python
    ---

    <ans>
    ```python
    ">:MASBicudo".lstrip(":>|")
    ```
    </ans>

    Result is `"MASBicudo"`.

    This removes any of the characters from the beginning of the string.
    Order does not matter.

#file=en-US/python/remove-characters-surrounding-string.md
    ---
    title: Remove characters surrounding string in Python
    ---

    <ans>
    ```python
    ">:MASBicudo?!".strip(":>|!?.")
    ```
    </ans>

    Result is `"MASBicudo"`.

    This removes any of the characters from both ends of the string.
    Order does not matter.

#file=en-US/python/slice-array.md
    ---
    title: Slice array in Python
    ---

    <ans>
    ```python
    list[1:2]
    ```
    </ans>

    Slice the `list` variable at index 1 and 2.

    #### Negative slice

    ```python
    list[:1] + list[3:]
    ```

    Remains after slicing the `list` variable at index 1 and 2.

#file=en-US/python/tuples-immutable-lists.md
    ---
    title: "Tuples: Immutable lists in Python"
    ---

    <ans>
    Immutable lists are called **tuples**.
    </ans>

    ```python
    (1, 2, 4)
    ```

    A tuple of one item must be initialized like:

    ```python
    (1,)
    ```

#file=en-US/python/remove-item-from-tuple.md
    ---
    title: Remove item from tuple in Python
    ---

    ```python
    t1 = (0, 1, 2, 3, 4)
    t2 = t1[:2] + t1[3:]
    ```

    This removes item at index 2.
    `t2` will contain `(0, 1, 3, 4)`.

    Tuples are **immutable**, so the resulting tuple is a new tuple.
    The value must be assigned back to the original variable to replace the old tuple.

    #### Remove last item from tuple:

    ```python
    t2 = t1[:-1]
    ```

    #### Remove first item from tuple:

    ```python
    t2 = t1[1:]
    ```

#file=en-US/python/pop-or-dequee-item-from-tuple.md
    ---
    title: Pop or dequee item from tuple in Python
    ---

    #### 1. Pop

    ```python
    t1 = (0, 1, 2, 3, 4)
    t1, v = t1[:-1], t1[-1]
    ```

    #### 2. Dequee

    ```python
    t1 = (0, 1, 2, 3, 4)
    t1, v = t1[1:], t1[0]
    ```

#file=en-US/jekyll/iterating-tags.md
    ---
    title: Iterating tags in Jekyll
    ---

    <ans>
    {% raw %}
    ```
    {% for tag in page.tags %}
        <span>{{ tag }}</span>
    {% endfor %}
    ```
    {% endraw %}
    </ans>

    - for pages, use `page.tags`
    - for posts, use `post.tags`

#file=en-US/jekyll/convert-date-to-string.md
    ---
    title: Convert date to string in Jekyll
    ---

    <ans>
    {% raw %}
    ```
    post.date | date_to_string
    ```
    {% endraw %}
    </ans>

#file=en-US/jekyll/supported-languages-in-a-code-block.md
    ---
    title: Supported languages in a code block
    ---

    <ans>
    The list is defined by **Rouge** project.
    </ans>

    #### Using Rouge CLI

    ```
    rougify list
    ```

    #### Website

    #ref=https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers

#file=en-US/python/check-number-is-even-or-odd.md
    ---
    title: Chack if a number is even or odd in Python
    ---

    #### Even:

    <ans>
    ```python
    is_even = lambda num: (num & 1) == 0
    ```
    </ans>

    #### Odd:

    <ans>
    ```python
    is_even = lambda num: (num & 1) == 1
    ```
    </ans>

#file=en-US/jekyll/categories-of-page-is-empty.md
    ---
    title: Categories of page is empty in Jekyll
    ---

    <ans>
    Only posts are assigned categories automatically by looking at folder structure.
    </ans>

    For pages to have categories, they must indicate them in the **front matter**.

#file=en-US/jekyll/front-matter.md
    ---
    title: Front matter in Jekyll
    ---

    <ans>
    {% raw %}
    ```
    ---
    title: Title of the page or post
    ---
    ```
    {% endraw %}
    </ans>

    **Remarks:**

    The front matter of a Jekyll page is like a header of the file.
    It is used to define variables associated with the file.
    These variables are then used in various contexts.
    The variables go directly into the `page` or `post` variable.

    **Example:**

    {% assign var1 = "{{ page.title }}" %}
    ```
    {{ var1 }}
    ```

    **References:**
    - #ref=http://simpleprimate.com/blog/front-matter

#file=en-US/jekyll/last-item-of-array.md
    ---
    title: Last item of array in Jekyll
    ---

    <ans>
    {% raw %}
    ```
    {{ array | last }}
    ```
    {% endraw %}
    </ans>

#file=en-US/css/custom-properties.md
    ---
    title: Custom properties in CSS
    ---
    #ref=https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties

    #### Defining variable

    <ans>
    ```css
    --custom-property: value;
    ```
    </ans>

    #### Using variable

    <ans>
    ```css
    font-size: var(--custom-property);
    ```
    </ans>

#file=en-US/css/font-size-relative-to-resolution.md
    #publish=false
    ---
    title: Font size relative to resolution in CSS
    ---

    #ref=https://stackoverflow.com/questions/16385559/how-to-change-the-font-size-proportionally-to-the-change-size-of-the-window-in-c/25780238
    #ref=https://stackoverflow.com/questions/41062123/css-font-size-responsive-relative-to-device-resolution
    #ref=https://www.w3schools.com/css/css_rwd_mediaqueries.asp
    #ref=https://stackoverflow.com/questions/11777598/font-size-relative-to-the-users-screen-resolution

#file=en-US/python/cannot-read-open-mode-x.md
    ---
    title: Cannot read from file opened with mode "x" in Python
    ---

    <ans>
    Mode "x" is write only, to also read from file, use mode "x+".
    </ans>

#file=en-US/python/psycopg2-copy_from-cannot-insert-field-with-delimiter-even-if-quoted.md
    ---
    title: psycopg2 copy_from cannot insert field with delimiter, even if quoted
    ---

    `copy_from` does not support CSV field quoting. Use `copy_expert` instead:

    <ans>
    ```python
    cur.copy_expert(f"""
        COPY {tablename} (col1, col2, ...)
        FROM STDIN
        WITH (FORMAT CSV)
    """, csv_file_stream)
    ```
    </ans>

#file=en-US/postgresql/create-table-if-not-exists.md
    ---
    title: Create table if it does not exist in PostgreSQL
    ---

    <ans>
    ```sql
    CREATE TABLE IF NOT EXISTS table_name
    ```
    </ans>

#file=en-US/postgresql/drop-table-if-exists.md
    ---
    title: Drop table if it exists in PostgreSQL
    ---

    <ans>
    ```sql
    DROP TABLE IF EXISTS table_name
    ```
    </ans>

    Multiple table names can be specified.

    #### Cascade drop dependent objects

    ```sql
    DROP TABLE IF EXISTS table_name CASCADE
    ```

#file=en-US/postgresql/drop-database-connections.md
    ---
    title: Drop database connections in PostgreSQL
    ---

    <ans>
    ```sql
    SELECT pg_terminate_backend(pid)
    FROM pg_stat_activity
    WHERE datname = 'db_name'
    ```
    </ans>

#file=en-US/python/iterate-dict-key-value-pairs.md
    ---
    title: Iterate dictionary key/value pairs in Python
    ---

    <ans>
    ```python
    for k, v in d.items():
        print(k, v)
    ```
    </ans>

#file=en-US/windows-terminal/open-new-tab.md
    # Open new tab in Windows Terminal

    <ans>
    ```
    wt -w 0 nt
    ```
    </ans>

    #### Using a profile

    ```
    wt -w 0 nt -p "Prompt de comando"
    ```

    The profile name is not culture invariant, so using it in scripts could be a problem.

    #### Reference

    #ref=https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=windows#options-and-commands

#file=en-US/windows-terminal/execute-command-in-new-tab.md
    # Execute command in new tab in Windows Terminal

    <ans>
    ```
    wt -w 0 nt cmd /K echo MASBicudo
    ```
    </ans>

    #### Using a profile

    ```
    wt -w 0 nt -p "Prompt de comando" cmd /K echo MASBicudo
    ```

    The profile name is not culture invariant, so using it in scripts could be a problem.

    #### Reference

    #ref=https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=windows#options-and-commands

#file=en-US/windows-terminal/execute-command-in-new-split-pane.md
    # Execute command in new split pane in Windows Terminal

    <ans>
    ```
    wt -w 0 sp -V cmd /K echo MASBicudo
    ```
    </ans>

    - `-V`: vertical split pane
    - `-H`: horizontal split pane

    #### Reference

    #ref=https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=windows#options-and-commands

#file=en-US/windows-terminal/open-new-split-pane.md
    # Open new split pane in Windows Terminal

    <ans>
    ```
    wt -w 0 sp -V
    ```
    </ans>

    - `-V`: vertical split pane
    - `-H`: horizontal split pane

    #### Reference

    #ref=https://docs.microsoft.com/en-us/windows/terminal/command-line-arguments?tabs=windows#options-and-commands

#file=en-US/powershell/clear-screen.md
    # Clear screen in PowerShell

    <ans>
    ```
    clear
    ```
    </ans>

#file=en-US/powershell/execute-multiple-commands-in-single-line.md
    # Execute multiple commands in a single line in PowerShell

    <ans>
    ```
    cmd1 ; cmd2 ; ...
    ```
    </ans>

#file=en-US/windows-cmd/execute-multiple-commands-in-single-line.md
    # Execute multiple commands in a single line in Batch

    <ans>
    ```
    cmd1 & cmd2 & ...
    ```
    </ans>

#file=en-US/python/execute-function-at-exit.md
    # Execute function at exit in Python

    ```
    atexit.register(fn)
    ```

    This can be used inside a module.

    The function will be called in the end of the Python program, even if the program is terminated by pressing <kbd>ctrl+c</kbd>.

    #### Prerequisite:

    ```python
    import atexit
    ```

#file=en-US/css/condition-styles-to-screen-orientation.md
    # Condition CSS styles to screen orientation

    <ans>
    ```css
    @media (orientation: portrait) {
    }
    ```
    </ans>

    #### `orientation` can be:

    - `portrait`: height greater than width
    - `landscape`: width greater than height

#file=en-US/python/better-performance-with-compiled-regex.md
    # Better performance with compiled regex in Python
    <ans>
    ```python
    pattern = re.compile(r"brown (\w+)")
    ```
    </ans>

    Available `pattern` functions: `match`, `search`, `fullmatch`, `split`, `sub`, `findall`, `finditer` and `subn`.

    Each function has one less parameter for the pattern string.

    ```python
    pattern.sub(r"\1", "The brown fox jumps!")
    ```


    #### Reference

    #ref=https://docs.python.org/3/library/re.html#regular-expression-objects

#file=en-US/python/get-all-capture-groups-from-regex-match.md
    # Get all capture groups from regex match in Python
    <ans>
    ```python
    match.groups()
    ```
    </ans>

    #### Example
    
    ```python
    match = re.match(r"(\d+)(\w+)", "123abc")
    print(match.groups())
    ```

    Output: `('123', 'abc')`

    #### Prerequisite

    ```python
    import re
    ```

    #### Reference

    #ref=https://docs.python.org/3/library/re.html#re.Match.groups

#file=en-US/html/anchor-with-reference-to-page-element.md
    # Anchor with reference to page element in HTML

    <ans>
    ```html
    <a href="#element_id">Link to element</a>
    <div id="element_id">
    ```
    </ans>

    Also works with more URI params filled, e.g. query string, path, domain, and so on.

#file=en-US/html/set-name-of-file-to-be-downloaded-via-link.md
    # Set the name of a file to be downloaded via a link in HTML

    <ans>
    ```html
    <a download="File Name.pdf"
       href="file-name?format=pdf">
            Download File Name PDF
    </a>
    ```
    </ans>

    `download` attribute can be used to suggest a file name.

#file=en-US/javascript/create-data-uri-from-web-content.md
    # Create data URI from web content in JavaScript

    <ans>
    ```js
    get_data_uri_from_web_content = (uri) => new Promise(
        async (resolve, reject) => {
            const blob = await (await fetch(uri)).blob()
            const reader = new FileReader()
            reader.onload  = ()      => resolve(reader.result)
            reader.onerror = (error) => reject(error)
            reader.readAsDataURL(blob)
        })
    ```
    </ans>

    #### Usage

    ```js
    get_data_uri_from_web_content("https://api.github.com/repos/masbicudo/oqueeh")
	    .then(data_uri => document.write(data_uri))
    ```

    #ref=en-US/html/data-uri-generator.md

#file=en-US/html/encode-file-data-inside-link-href-attribute.md
    # Encode file data inside link href attribute

    <ans>
    ```html
    <a href="data:text/plain;charset=utf-8;base64,TUFTQmljdWRv"
        download="masbicudo.txt">Download</a>
    ```
    </ans>

    #### Example

    <a href="data:text/plain;charset=utf-8;base64,TUFTQmljdWRv"
        download="masbicudo.txt">Download</a>

    #ref=en-US/html/data-uri-generator.md

#file=en-US/html/set-selected-item-in-html-select-element.md
    # Set selected item in HTML select element

    ```html
    <option selected>Item text</option>
    ```

#file=en-US/css/ordering-of-values-on-margin-and-padding.md
    # Ordering of values on CSS margin and padding

    #### 4 values

    Clockwise starting from top.

    ```css
    margin: top right bottom left
    ```

    #### 3 values

    From top to bottom.

    ```css
    margin: top right+left bottom
    ```

    #### 2 values

    Vertical then horizontal.

    ```css
    margin: top+bottom right+left
    ```

    #### 1 value

    All.

    ```css
    margin: top+bottom+right+left
    ```

#file=en-US/javascript/load-file-as-data-uri.md
    # Load file as data-URI

    <ans>
    #### JavaScript

    ```javascript
    function openFile(event, target_element) {
        const reader = new FileReader()
        reader.onload = () => target_element.innerText = reader.result
        reader.readAsDataURL(event.target.files[0])
    }
    window.addEventListener('load', e => 
    ```

    #### HTML

    ```html
    <div id='output'></div>
    ```
    </ans>

#file=en-US/javascript/generator-functions.md
    # Generator functions in JavaScript

    <ans>
    ```js
    function* gen() {
        yield 1
        yield 2
    }
    ```
    </ans>

#file=en-US/javascript/async-and-await-with-map.md
    # Using asynchronous functions with Array map in JavaScript

    <ans>
    ```js
    fna = async (data) => Promise.resolve(data)
    promise_list = [1,2,3,4].map(async (x) => (await fna(x)) + 10)
    Promise.all(promise_list).then(all_data => console.log(all_data))
    ```
    </ans>

    `Promise.all` returns a promise that resolves with the values of all listed promises.

#file=en-US/javascript/infinite-generator-functions.md
    # Generator functions in JavaScript

    <ans>
    ```js
    function* gen() {
        var x = 0
        while (true) yield x++
    }
    ```
    </ans>

#file=en-US/javascript/window-load-dom-content-loaded-ready-state-change-events.md

    #include=en-US/javascript/page-load-events-in-web-browser.md

#file=en-US/javascript/page-load-events-in-web-browser.md
    # Page load events in web browser JavaScript

    <ans>
    1. document.readystate = interactive
    2. document.DOMContentLoaded
    3. document.readystate = complete
    4. window.load
    </ans>

    #### Adding the event listeners

    ```js
    window.addEventListener('load',
        e => console.log('window.load'))
    document.addEventListener('readystatechange',
        e => console.log(`document.readystate = ${document.readyState}`))
    document.addEventListener('DOMContentLoaded',
        e => console.log('document.DOMContentLoaded'))
    ```

    #### Reference

    #ref=https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event

#file=en-US/javascript/declaring-variables-with-var-let-and-const.md
    # Declaring variables with var, let and const in JavaScript

    <ans>
    - `var`: function scope variable
    - `let`: block scope variable
    - `const`: block scope constants
    </ans>

#file=en-US/javascript/difference-between-var-let-and-const.md
    # Difference between var, let and const in JavaScript
    #include=en-US/javascript/declaring-variables-with-var-let-and-const.md

#file=en-US/css/split-long-words-to-next-line.md
    # Split long words to next line using CSS

    <ans>
    ```css
    div {
        word-wrap: break-word;
    }
    ```
    </ans>

#file=en-US/javascript/wait-for-many-promises.md
    # Wait for many promises in JavaScript

    <ans>
    ```js
    await Promise.all(promise_list)
    ```
    </ans>

#file=en-US/html/data-uri-generator.md
    # Data URI generator

    <style>
    input, textarea, select {
        width: 100%;
        display: none;
    }
    .visible {
        display: block;
    }
    .output {
        overflow-wrap: break-word;
    }
    </style>
    #### Input

    <select id="sel" class="visible">
        <option value="file" selected>File</option>
        <option value="text">Text</option>
        <option value="uri">URI</option>
    </select>

    <input    id="file" type="file" class="visible" selected>
    <textarea id="text"></textarea>
    <input    id="uri" type="text">
    <div class="highlight">
    <code id='output' class="output"></code>
    </div>
    <script>
        const fileToDataUri = (file_or_blob) => new Promise((resolve, reject) => {
            const reader = new FileReader()
            reader.onload  = ()      => resolve(reader.result)
            reader.onerror = (error) => reject(error)
            reader.readAsDataURL(file_or_blob)
        })
        function itemsToTargetElement(items, target_element) {
            target_element.innerHTML = ""
            for (item of items) {
                div = document.createElement("div")
                div.innerHTML = '<span class="nt">&lt;a</span>'+
                                ' <span class="na">download=</span>'+
                                '<span class="s">"'+item.name+'"</span>'+
                                ' <span class="na">href=</span>'+
                                '<span class="s">"'+item.text+'"</span>'+
                                '<span class="nt">&gt;</span>'+
                                item.name+
                                '<span class="nt">&lt;/a&gt;</span>'
                target_element.appendChild(div)
            }
        }
        async function openFileAndConvertToDataUri(files, target_element) {
            items_promise = [...files].map(async file => ({"name": file.name, "text": await fileToDataUri(f)}))
            await Promise.all(items_promise).then(items => itemsToTargetElement(items, target_element))
        }
        function getTextAndConvertToDataUri(event, target_element) {
            items = [{"name": "foo.txt", "text": "data:text/plain;base64," + btoa(event.target.text)}]
            itemsToTargetElement(items, target_element)
        }
        async function downloadUriAndConvertToDataUri(uri, target_element) {
            const response = await fetch(uri)
            const content_disposition = response.headers.get("Content-Disposition")
            const name = /filename=(.*)$/g.exec(content_disposition)[1]
            const blob = await response.blob()
            items = [{"name": name, "text": await fileToDataUri(blob)}]
            itemsToTargetElement(items, target_element)
        }
        sel.addEventListener("change", e => {
            for (opt of sel.options)
                window[opt.value].classList.remove("visible")
            window[e.target.value].classList.add("visible")
        })
        file.addEventListener("change", async (e) => await openFileAndConvertToDataUri(e.target.files, output))
        text.addEventListener("keydown", (e) => getTextAndConvertToDataUri(e.target.innerText, output))
        var timer = null
        uri.addEventListener("keydown", (e) => {
            clearTimeout(timer)
            timer = setTimeout(async () => await downloadUriAndConvertToDataUri(e.target.value, output), 1)
        })
    </script>

#file=en-US/github/api-to-get-info-about-a-repository.md
    # API to get information about a repository from GitHub

    <ans>
    https://api.github.com/repos/<owner>/<repo>

    Example: https://api.github.com/repos/masbicudo/oqueeh
    </ans>

#file=en-US/javascript/creating-iterable-class.md
    # Creating an iterable class in JavaScript

    <ans>
    ```js
    class Class {
        *[Symbol.iterator]() {
            yield 1
            yield 2
        }
    }
    ```
    </ans>

    Iterables can be used in `for`..`of` statements, and with spread operator:

    ```js
    for (let x of iterable) console.log(x)
    console.log([...iterable])
    ```

    #ref=en-US/javascript/iterables-usage.md

#file=en-US/javascript/creating-iterable-object.md
    # Creating an iterable object in JavaScript

    <ans>
    ```js
    obj = {
        [Symbol.iterator]: function* () {
            yield 1
            yield 2
        }
    }
    ```
    </ans>

    Iterables can be used in `for`..`of` statements, and with spread operator:

    ```js
    for (let x of iterable) console.log(x)
    console.log([...iterable])
    ```

    #ref=en-US/javascript/iterables-usage.md

#file=en-US/javascript/making-object-iterable.md
    # Making an object iterable in JavaScript

    ```js
    obj = {}
    obj[Symbol.iterator] = function* () {
        yield 1
        yield 2
    }
    ```

    Iterables can be used in `for`..`of` statements, and with spread operator:

    ```js
    for (let x of iterable) console.log(x)
    console.log([...iterable])
    ```

    #ref=en-US/javascript/iterables-usage.md

#file=en-US/javascript/iterables-usage.md
    # Iterables usage in JavaScript

    <ans>
    #### `for`..`of` statement

    ```js
    for (let x of iterable) console.log(x)
    ```

    #### Spread operator `...`

    ```js
    console.log([...iterable])
    ```
    </ans>

#file=en-US/javascript/convert-iterable-object-to-array.md
    # Convert iterable object to Array in JavaScript

    <ans>
    ```js
    [...iterable_object]
    ```
    </ans>

    #### Alternative

    <ans>
    ```js
    Array.from(iterable_object)
    ```
    </ans>

#file=en-US/javascript/rest-parameters.md
    # Rest parameters in JavaScript

    ```js
    function fn(a, b, ...others) {
        console.log(a, b, others)
    }
    ```

    Rest parameter is denoted by three dots before last parameter.
    It receives all extra parameters passed.

    #### Example:

    ```js
    fn(1,2,5,8)
    ```

    Output: `1 2 [ 5, 8 ]`

#file=en-US/javascript/create-function-with-variable-number-of-parameters.md
    #publish=false
    # Create function with variable number of parameters in JavaScript

    #include=en-US/javascript/rest-parameters.md

#file=en-US/javascript/convert-arguments-object-to-array.md
    # Convert arguments object to Array in JavaScript

    <ans>
    ```js
    function fn(...args) {
    }
    ```
    </ans>

    Rest parameters are represented by the three dots before the last parameter.
    It receives all extra arguments as an Array.

    #### Alternative: spread into Array

    ```js
    [...arguments]
    ```

    #### Alternative: Array.from
    
    ```js
    Array.from(arguments)
    ```

    #### ES5

    ```js
    Array.prototype.slice.call(arguments)
    ```

    #ref=en-US/javascript/convert-iterable-object-to-array.md

#file=en-US/javascript/what-is-vanilla-javascript.md
    # What is vanilla JavaScript

    <ans>
    To rely on standard JavaScript instead of using external libraries.
    </ans>

#file=en-US/javascript/what-is-ecmascript.md
    # What is ECMAScript?

    <ans>
    ECMAScript is a standard defining a common language specification.

    The purpose is to provide wide compatibility between browsers and web applications.
    </ans>

    There is one new edition of the ECMAScript per year.

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/specification-dialects-and-engine-implementations.md
    # Dialects and engine implementations of JavaScript?

    <ans>
    #### Specification

    - ECMAScript (ECMA-262)

    #### Dialects

    - JavaScript
    - JScript
    - ActionScript

    #### Engines

    - V8
    - SpiderMonkey
    - Chakra
    </ans>

#file=en-US/javascript/what-is-javascript.md
    # What is JavaScript?

    <ans>
    JavaScript is the main dialect of ECMAScript.
    It is used in many modern browsers, backend servers and also in no-sql document databases.
    </ans>

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/what-is-jscript.md
    # What is JScript?

    <ans>
    JScript is the Microsoft's dialect of ECMAScript.
    It is used in Internet Explorer, Edge and Windows Script (WScript).
    </ans>

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/what-is-chakra.md
    # What is Chakra?

    <ans>
    Chakra is the Microsoft's engine implementation of ECMAScript.
    It is used in Internet Explorer, Edge and Windows Script (WScript).
    </ans>

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/what-is-spidermonkey.md
    # What is SpiderMonkey?

    <ans>
    SpiderMonkey is the engine implementation of ECMAScript by Mozilla.
    It is used in Firefox browser and other Mozilla projects.
    Also used in no-sql, i.e. document databases, like MongoDB.
    </ans>

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/what-is-actionscript.md
    # What is ActionScript?

    <ans>
    ActionScript is the Adobe's dialect of ECMAScript, used in Adobe Flash.
    </ans>

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/what-is-v8.md
    # What is V8?

    <ans>
    V8 is an ECMAScript engine implementation by Google (Alphabet).

    It is used in Google Chrome browser and also in Node.js.
    </ans>

    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/firefox-browser-name.md
    # Firefox or FireFox?

    <ans>
    Firefox, with lower f in fox.
    </ans>

#file=en-US/javascript/javascript-language-name.md
    # JavaScript or Javascript?

    <ans>
    JavaScript, with upper S is the correct name.
    </ans>

    #### References

    #ref=https://en.wikipedia.org/wiki/JavaScript
    #ref=https://developer.mozilla.org/en-US/docs/Web/JavaScript
    #ref=en-US/javascript/specification-dialects-and-engine-implementations.md

#file=en-US/javascript/delay-code-execution.md

    <ans>
    ```js
    setTimeout(() => el.innerText = "Update text after 5 seconds", 5000)
    ```
    </ans>

#file=en-US/javascript/use-async-function-in-synchronous-context.md

    <ans>
    ```js
    promise.then(data => proc(data))
    ```
    </ans>

    #### Alternative

    ```js
    (async () => proc(await promise))()
    ```

#file=en-US/javascript/get-name-of-fetched-file.md

    <ans>
    ```js
    response.headers.get("content-disposition")
    ```
    </ans>

    `response` is returned by calling `fetch` asynchronously. Example:

    ```js
    const response = await fetch(uri)
    ```

#file=en-US/javascript/cancel-delayed-code-execution.md

    <ans>
    ```js
    clearTimeout(timer)
    ```
    </ans>

    `timer` object is returned by `setTimeout`. Example:

    ```js
    timer = setTimeout(() => el.innerText = "Update text after 5 seconds", 5000)
    ```

#file=en-US/javascript/fire-change-event-after-user-stops-typing.md

    <ans>
    ```js
    text_input.addEventListener("keydown", e => {
        clearTimeout(timer)
        timer = setTimeout(() => output.innerText = e.target.value, 1000)
    })
    ```
    </ans>

    HTML:

    ```html
    <input type="text" id="text_input" />
    <div id="output"></div>
    ```

#file=en-US/windows-terminal/close-pane-key-binding.md
    # Close pane key binding in Windows Terminal

    <ans>
    <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>W</kbd>
    </ans>

    Closing the last pane will close the tab.
    Closing the last tab will close the window.

#file=en-US/windows-terminal/new-pane-key-binding.md
    # New pane key binding in Windows Terminal

    <ans>
    - New horizontal pane: <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>-</kbd>
    - New vertical pane:   <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>=</kbd>
    </ans>

#file=en-US/javascript/get-select-element-option-values.md
    # Get select element option values in JavaScript

    <ans>
    ```js
    [...sel.options].map(opt => opt.value)
    ```
    </ans>

#file=en-US/javascript/toggle-html-element-class.md
    # Toggle HTML element class in JavaScript

    <ans>
    ```js
    el.classList.toggle("class_name")
    ```
    </ans>

#file=en-US/javascript/prevent-default-dom-event-action.md
    # Prevent default DOM event action in JavaScript

    <ans>
    ```js
    event.preventDefault()
    ```
    </ans>

#file=en-US/javascript/get-select-element-options.md
    # Get select element options in JavaScript

    <ans>
    ```js
    s.options
    ```
    </ans>

    #### References

    #ref=https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement
    #ref=https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionElement

#file=en-US/windows-terminal/default-key-bindings.md
    # Default key bindings in Windows Terminal

    <ans>
    - Close pane/tab/window: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>W</kbd>
    - New horizontal pane:   <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>-</kbd>
    - New vertical pane:     <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>=</kbd>
    - Switch pane:           <kbd>Alt</kbd>+*Arrow kbds*
    - Resize pane:           <kbd>Alt</kbd>+<kbd>Shift</kbd>+*Arrow kbds*
    </ans>

    *Arrow keys*: <kbd>Down</kbd> \| <kbd>Up</kbd> \| <kbd>Left</kbd> \| <kbd>Right</kbd>

#file=en-US/python/encode-uri-query-string-from-dictionary.md
    # Encode URI query string from dictionary in Python

    <ans>
    ```python
    urllib.parse.urlencode({"q": "encode uri", "lang": "python"})
    ```
    </ans>

    Output: `"q=encode+uri&lang=python"`

    #### Prerequisite

    ```python
    import urllib.parse
    ```

#file=en-US/git/set-user-name-and-email.md
    # Set user name and email in Git

    <ans>
    ```bash
    git config --global user.name "Miguel Angelo"
    git config --global user.email "masbicudo@gmail.com"
    ```

#file=en-US/python/encode-string-to-utf-8.md
    # Encode string to UTF-8 in Python


#file=en-US/python/save-text-file-using-utf-8.md
    # Save text file using UTF-8 in Python

    <ans>
    with open("filename.txt", "w", encoding="utf-8") as tfs:
        tfs.write(string_value)
    </ans>

#file=en-US/python/convert-string-to-utf-8-before-saving-file.md
    #delete
#file=en-US/python/write-utf-8-encoded-text-inside-binary-file.md
    # Write UTF-8 encoded text inside binary file in Python

    <ans>
    ```python
    content = "MASBicudo"
    bytes_utf8 = content.encode("utf-8")
    with open("filename.txt", "wb") as fs:
        fs.write(bytes_utf8)
    ```
    </ans>

    `str` has the `encode` method, that returns `bytes` with the encoded string.

#file=en-US/python/read-utf-8-encoded-text-from-binary-file.md
    #publish=0
    #ref=https://docs.python.org/3/howto/unicode.html

#file=en-US/python/sqlite-builtin-database.md
    #publish=0

#file=en-US/javascript/sqlite-database-on-static-web-pages.md
    #publish=0
    #ref=https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/

#file=en-US/postgresql/starting-and-stopping-postgresql-database-service-in-ubuntu.md
    # Starting and stopping a PostgreSQL database service in Ubuntu

    **To start run:**
    <ans>
    ```bash
    sudo service postgresql start
    ```
    </ans>

    **To stop run:**
    <ans>
    ```bash
    sudo service postgresql stop
    ```
    </ans>

#file=en-US/postgresql/starting-postgresql-database-service-in-ubuntu.md
    # Starting a PostgreSQL database service in Ubuntu

    <ans>
    ```bash
    sudo service postgresql start
    ```
    </ans>

#file=en-US/postgresql/stopping-postgresql-database-service-in-ubuntu.md
    # Stopping a PostgreSQL database service in Ubuntu

    <ans>
    ```bash
    sudo service postgresql stop
    ```
    </ans>

#file=en-US/postgresql/starting-postgresql-database-service-in-windows-via-cmd.md
    # Starting a PostgreSQL database service in Windows using CMD

    <ans>
    ```bash
    pg_ctl -D "C:\Program Files\PostgreSQL\15\data" start
    ```
    </ans>

#file=en-US/postgresql/stopping-postgresql-database-service-in-windows-via-cmd.md
    # Stopping a PostgreSQL database service in Windows using CMD

    <ans>
    ```bash
    pg_ctl -D "C:\Program Files\PostgreSQL\15\data" stop
    ```
    </ans>

#file=en-US/postgresql/restarting-postgresql-database-service-in-windows-via-cmd.md
    # Restarting a PostgreSQL database service in Windows using CMD

    <ans>
    ```bash
    pg_ctl -D "C:\Program Files\PostgreSQL\15\data" restart
    ```
    </ans>

#file=en-US/postgresql/managing-postgresql-database-service-in-windows.md
    # Managing a PostgreSQL database service in Windows

    Use Windows Services manager to start, stop, pause and restart the PostgreSQL database service.

    <ans>
    1. Use <kbd>WinKey</kbd>+<kbd>R</kbd> for *Run Window*
    2. Type `services.msc`
    3. Search for `postgresql` in the list
       - You can type to search!
    4. Top bar contains buttons to **start**, **stop**, **pause** and **restart**.
    </ans>

#file=en-US/windows/what-is-the-windows-key-used-for.md
    ---
    keywords: ["winkey", "win-key", "windows key", "windows-key"]
    ---
    # What is the Windows key used for?

    <ans>
    Windows key is used to activate useful keyboard shortcuts.
    </ans>

    Short list of known shortcuts on Windows:
    - <kbd>WinKey</kbd>+<kbd>R</kbd>: open "Run" dialog
    - <kbd>WinKey</kbd>+<kbd>D</kbd>: show Desktop/restore windows
    - <kbd>WinKey</kbd>+<kbd>X</kbd>: system menu

#file=en-US/windows/how-to-open-on-screen-keyboard-in-windows.md
    # How to open On-Screen Keyboard in Windows?

    <ans>
    1. <kbd>WinKey</kbd>+<kbd>R</kbd>
    2. **Settings** > **Accessibility** > **Keyboard**
    3. **On-Screen Keyboard** toggle
    </ans>

#file=en-US/c-sharp/know-if-file-cloudapi-status-is-offline.md
    # How to check CloudAPI offline status?

    <ans>
    ```c#
    var FILE_ATTRIBUTES_RECALL_ON_DATA_ACCESS = 4194304;
    var isNotReady = (File.GetFileInfo(filePath)
        & FILE_ATTRIBUTES_RECALL_ON_DATA_ACCESS) != 0;
    ```
    </ans>

    **References:**
    - #ref=https://learn.microsoft.com/pt-br/dotnet/api/system.io.fileattributes?view=net-7.0
    - #ref=https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants

#file=en-US/markdown/c-sharp-code-fence.md
    # C# code inside a Markdown file

    <ans>
    ````md
    ```c#
    // C# code fence in markdown
    ```
    ````
    </ans>

    **References:**
    - [highlight.js/SUPPORTED_LANGUAGES.md](https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md)

#file=en-US/pdm/ModuleNotFoundError-No-module-named-pdm-core.md

    # ModuleNotFoundError: No module named 'pdm.core'

    <ans>Remove PDM by hand, then reinstall by hand.</ans>

    ```bash
    cd ~
    curl -sSLO https://pdm.fming.dev/dev/install-pdm.py
    python install-pdm.py --remove
    python install-pdm.py
    rm install-pdm.py
    ```

#file=en-US/windows/edit-user-and-system-environment-variables.md
    # Edit user and system environment variables in Windows

    <ans>
    1. <kbd>WinKey</kbd>+<kbd>R</kbd>
    2. Type in `sysdm.cpl`
    3. **Advanced** tab
    4. **Environment Variables...** button
    </ans>

#file=en-US/windows/edit-user-environment-variables.md
    # Edit user environment variables in Windows

    <ans>
    1. <kbd>WinKey</kbd> to open **Start Menu**
    2. Type in `var`
    3. Locate **Edit environment variables for your account**
    </ans>

#file=en-US/windows/edit-system-environment-variables.md
    # Edit system environment variables in Windows

    <ans>
    1. <kbd>WinKey</kbd>
    2. Type in `var`
    3. Locate **Edit the system environment variables**
    </ans>

#file=en-US/pyenv/pyenv-is-not-recognized-as-the-name-of-a-cmdlet-function.md
    #delete
#file=en-US/pyenv-win/pyenv-is-not-recognized-as-the-name-of-a-cmdlet-function.md
    # 'pyenv' is not recognized as the name of a cmdlet, function

    <ans>
    Reinstall PyEnv-Win:
    ```powershell
    Invoke-WebRequest -UseBasicParsing `
        -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" `
        -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
    ```
    </ans>

    **Alternative:**
    <ans>
    Add the following to current user `Path`:
    - `%USERPROFILE%\.pyenv\pyenv-win\bin`
    - `%USERPROFILE%\.pyenv\pyenv-win\shims`
    </ans>

    See [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)

#file=en-US/windows-cmd/maths-division-cmd.md
    # Division using CMD

    <ans>
    ```
    set /a result=10/2
    ```
    </ans>

    You can use variables in the place of numbers.

#file=en-US/windows-cmd/maths-in-cmd.md
    # Mathematics using CMD

    <ans>
    ```
    set /a result=10/(2+1)
    ```
    </ans>

    Supported operations:
    - addition (`+`) and subtraction (`-`)
    - multiplication (`*`) and division (`/`) (i.e. integer division)
    - modulo (`%`) (aka remainder from division)
    - parentheses (`(` and `)`) (aka precedence operators)

    You can use variables in the place of numbers.

#file=en-US/windows-cmd/assign-output-of-command-to-variable.md
    # Assign the output of a command to a variable in CMD

    <ans>
    ```bat
    FOR /F "tokens=*" %%A IN ('dir "."') DO (
        SET var=%%A
    )
    ECHO %var%
    ```
    </ans>

#file=en-US/windows-cmd/run-powershell-command.md
    # Run PowerShell command in CMD

    <ans>
    ```bat
    powershell -command "ls"
    ```
    </ans>

#file=en-US/windows/what-is-powershell.md
    ---
    keywords: ["powershell"]
    ---
    # What is PowerShell?

    <ans>
    PowerShell is a shell command and scripting language.
    Key features:
    - pipes to redirect streams
    - use native .Net commands and variables
    - use environment commands and variables
    </ans>

#file=en-US/markdown/set-code-block-language.md
    # Set Markdown code block language

    ## To Python

    ````markdown
    ```python
    ````

    ## To Javascript

    ````markdown
    ```javascript
    ````

    **References:**
    - [highlight.js/SUPPORTED_LANGUAGES.md](https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md)

#file=en-US/c-sharp/reading-embedded-resources.md
    # Reading embedded resources in C#

    <ans>
    ```c#
    var assembly = Assembly.GetExecutingAssembly();
    var resourceName = "AssemblyNamespace.FolderNamespace.FileName";
    using (Stream stream = assembly.GetManifestResourceStream(resourceName))
    ```
    </ans>

    - **AssemblyNamespace:** the default root namespace of the assembly containing the embedded resource
    - **FolderNamespace:** path for the file inside the project with dots (`"."`) separating path items
    - **FileName:** name of the file including extension

    Know more:
    - #ref=en-US/visual-studio/embedding-resource-files.md
    - #ref=en-US/c-sharp/listing-embedded-resources.md

#file=en-US/c-sharp/listing-embedded-resources.md
    # Listing embedded resources in C#

    <ans>
    ```c#
    assembly.GetManifestResourceNames()
    ```
    </ans>

    Know more:
    - #ref=en-US/visual-studio/embedding-resource-files.md
    - #ref=en-US/c-sharp/reading-embedded-resources.md

#file=en-US/visual-studio/embedding-resource-files.md
    # Embedding resource files in Visual Studio

    <ans>
    1. Include the file in the project structure
    2. Select file and open properties window
    3. Set *Build Action* to **Embedded Resource**
    </ans>

    Know more:
    - #ref=en-US/c-sharp/reading-embedded-resources.md
    - #ref=en-US/c-sharp/listing-embedded-resources.md

#file=en-US/c-sharp/reading-embedded-resource-from-resx-file.md
    # Reading embedded resource from *.resx* file

    <ans>
    ```c#
    AssemblyNamespace.FolderStructure.ResourceFileName.resource_name
    ```
    </ans>

    **Example:**
    ```c#
    AssemblyNamespace.Properties.Resources.foo_txt
    ```

    **Notes:**
    - **AssemblyNamespace:** is the default namespace of the assembly containing the embedded resource
    - **FolderStructure:** is the relative path to the *.resx* file separated by dots (`"."`)
    - **ResourceFileName:** is the name of resource file, without *.resx* extension
    - **resource_name:** is the name of the resource item inside the resource file
    - can only access from another assembly if resource is *public*

    Know more:
    - #ref=en-US/visual-studio/adding-embedded-resource-to-resources-resx-file.md

#file=en-US/visual-studio/adding-embedded-resource-to-resources-resx-file.md
    # Adding embedded resource to *Resources.resx* file

    <ans>
    1. Right click the project, then select *Properties*
       - *-or-* select project, and press <kbd>Alt</kbd>+<kbd>Enter</kbd>
    2. Go to *Resources*
    3. Open or create resource file
    4. Select the option *Files* from tool-box menu
    5. Click *Add resource* button
    </ans>

    **Notes:**
    - *Resources.resx* file will be created inside the *Properties* folder

    **Know more:**
    - #ref=en-US/c-sharp/reading-embedded-resource-from-resx-file.md

#file=en-US/c-sharp/localized-embedded-resource-files.md
    # Localizing embedded resource files

    <ans>
    Add localization to file name.
    - e.g. *Resources.en-US.resx*.
    </ans>

    Know more:
    - #ref=en-US/visual-studio/adding-embedded-resource-to-resources-resx-file.md
    - #ref=en-US/c-sharp/reading-embedded-resource-from-resx-file.md

#file=en-US/liquid-templates/adding-numbers.md
    # Adding numbers in Liquid templates

    <ans>
    ```
    {{"{%"}} assign number = number1 | plus: number2 %}
    ```
    </ans>

#file=en-US/liquid-templates/multiply-numbers.md
    # Multiplying numbers in Liquid templates

    <ans>
    ```
    {{"{%"}} assign number = number1 | times: number2 %}
    ```
    </ans>

#file=en-US/liquid-templates/subtract-numbers.md
    # Subtracting numbers in Liquid templates

    <ans>
    ```
    {{"{%"}} assign number = number1 | minus: number2 %}
    ```
    </ans>

#file=en-US/liquid-templates/escaping-tags.md
    # Escaping tags in Liquid templates

    <ans>
    Escape only the opening of tags:
    - For `{{"{%"}}`, use `{{"{{"}}"{{"{%"}}"}}`
    - For `{{"{{"}}`, use `{{"{{"}}"{{"{{"}}"}}`
    </ans>

#file=en-US/liquid-templates/get-size-of-array.md
    # Getting the size of arrays in a Liquid template

    <ans>
    Using dot notation: `array.size`
    *-or-* using pipe notation: `array | size`
    </ans>

    References:
    - #ref:https://shopify.github.io/liquid/filters/size/

#file=en-US/pgadmin4/nonetype-object-has-no-attribute-value.md
    # 'NoneType' object has no attribute 'value'

    <ans>
    Downgrade pgAdmin4
    </ans>

#file=en-US/pgadmin4/missing-from-clause-entry-for-table-rel.md
    # missing FROM-clause entry for table "rel"

    <ans>
    Downgrade pgAdmin4
    </ans>

#file=en-US/c-sharp/redirect-output-of-child-process.md
    # Redirect output of child process using C#

    ```c#
    var process = Process.Start(
        new ProcessStartInfo("ping", "google.com") {
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            RedirectStandardInput = true });
    Console.WriteLine(process.StandardOutput.ReadToEnd());
    ```

    **Notes:**
    - `UseShellExecute` must be false, otherwise reading from `StandardOutput` throws an exception.
    - `RedirectStandardInput` may be needed even if you don't need to redirect input stream.

    **References:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.redirectstandardoutput?view=net-7.0
    - #ref=https://7thzero.com/blog/
    process-startinfo-redirectstandardoutput-not-quite-what-you-d-ex

#file=en-US/c-sharp/get-exit-code-of-child-process.md
    # Get exit code of a child process using C#

    ```c#
    process.WaitForExit();
    int exitCode = process.ExitCode;
    ```

    **References:**
    - #ref=https://stackoverflow.com/questions/37144749/how-to-run-and-get-output-from-another-application-using-c-sharp

#file=en-US/windows/create-desktop-shortcut-for-uwp-app.md
    # Create desktop shortcut for UWP app

    <ans>
    Drag and drop from the Start Menu
    </ans>

    **Note:**
    - Does not work in Windows 11

#file=en-US/python/what-are-enter-and-exit-functions.md
    # What are __enter__ and __exit__ functions in Python

    <ans>
    - Manage the usage of resources which need to be freed.
    - `__enter__` allocates the resource
    - `__exit__` release the resource
    </ans>

    **Notes:**
    - Can be used to create code-blocks in which a context is valid.

#file=en-US/python/string-interpolation.md
    # String interpolation in Python

    <ans>
    ```python
    f"Some value: {someValue}"
    ```
    </ans>

#file=en-US/c-sharp/string-interpolation.md
    # String interpolation in C#

    <ans>
    ```c#
    $"Some value: {someValue}"
    ```
    </ans>

    **References:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated

#file=en-US/c-sharp/string-interpolation-formatting.md
    # String interpolation formatting in C#

    <ans>
    ```c#
    $"Some value: {someValue:0.0}"
    ```
    </ans>

    **Know more:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated

#file=en-US/c-sharp/string-interpolation-escaping.md
    # String interpolation escaping in C#

    <ans>
    ```c#
    $$"{someValue}: {{"{{"}}someValue:0.0}}"
    ```
    *-or-*
    ```c#
    $"{{"{{"}}someValue}}: {someValue:0.0}"
    ```
    </ans>

    **Notes:**
    - Use multiple *$* to denote that braces (*{* and *}*)should be also the same multiple.

    **Know more:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated

#file=en-US/c-sharp/string-interpolation-conversions-types.md
    # String interpolation conversions types in C#

    <ans>
    These are the builtin string interpolation handler types:
    - String
    - FormattableString
    - IFormattable
    </ans>

    **Know more:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated

#file=en-US/c-sharp/string-interpolation-formattable-string.md
    # String interpolation conversion to FormattableString in C#

    <ans>
    ```c#
    FormattableString message = $"Value is {value}";
    ```
    </ans>

    **Know more:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated

#file=en-US/c-sharp/specify-culture-in-string-interpolation.md
    # How to specify culture in a C# interpolated string?

    <ans>
    Use the conversion to *FormattableString* or *IFormattable*:
    ```c#
    FormattableString message = $"Value is {value}";
    message.ToString(specificCulture);
    ```
    </ans>

    **Know more:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated

#file=en-US/c-sharp/creating-custom-string-interpolation-handler.md
    # Creating a custom string interpolation handler in C#

    Create a class with the following:
    <ans>
    - Attribute *InterpolatedStringHandler* applied to the class
    - Constructor with parameters `int literalLength` and `int formatCount`
    - Public methods *AppendLiteral* and *AppendFormatted*:
      - `public void AppendLiteral(string s)`
      - `public void AppendFormatted<T>(T t)`
    </ans>

    **Notes:**
    - *AppendFormatted* may have additional parameters `int alignment` and `string format`:
      - e.g. when using `$"{value,-15:red}"`
    - The methods may return *bool* to stop interpolation at any point.

    **Know more:**
    - #ref=en-US/c-sharp/passing-parameters-to-interpolation-handler-constructor.md

    **References:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/interpolated-string-handler

#file=en-US/c-sharp/passing-parameters-to-interpolation-handler-constructor.md
    # Passing parameters to a string interpolation handler constructor in C#

    Annotate the argument receiving the interpolated string handler with the attribute *InterpolatedStringHandlerArgument*, for example:

    <ans>
    ```c#
    public void PrintMessage(
        string color,
        [InterpolatedStringHandlerArgument("", "color")]
        ColorInterpolatedStringHandler builder
      )
    ```
    </ans>

    **Remarks:**
    - `""` parameter refers to `this` in that context.
    - `"color"` parameter refers to the argument named *color*.
      - The constructor of *ColorInterpolatedStringHandler* must receive both parameters:
        e.g. `ctor(int literalLength, int formatCount, MyClass my, string color)`

    **Know more:**
    - #ref=en-US/c-sharp/creating-custom-string-interpolation-handler.md

    **References:**
    - #ref=https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/interpolated-string-handler

#file=en-US/c-sharp/compare-arrays.md
    # Comparing arrays in C#

    <ans>
    ```c#
    Enumerable.SequenceEquals(array1, array2)
    ```
    *-or-*
    ```c#
    array1.AsSpan().SequenceEqual(array2)
    ```
    </ans>

    **References:**
    - #ref=https://code-maze.com/csharp-compare-arrays/

#file=en-US/postgresql/replace-string-using-regex-pattern.md
    # Replace string using regex pattern in PostgreSQL

    <ans>
    ```sql
    regexp_replace(string_value, '(\w)s*=\s*(\d)', '\1', 'g')
    ```
    </ans>
    
    The previous example extracts the name of a variable being assigned inside the text of *string_value*.

#file=en-US/postgresql/convert-string-to-number.md
    # Convert string to number in PostgreSQL

    <ans>
    ```sql
    string_value::numeric
    ```
    </ans>

    This example converts *string_value* to numeric type.

#file=en-US/postgresql/convert-specific-value-to-null.md
    # Convert specific value to Null in PostgreSQL

    <ans>
    ```sql
    NULLIF(input_value, '')
    ```
    </ans>

    This example converts the empty string in *input_value* to NULL.

#file=en-US/c-sharp/downloading-file-from-internet.md
    # How to download a file from the Internet using C#?

    <ans>
    ```c#
    using System.Net;
    using (WebClient webClient = new WebClient())
        webClient.DownloadFile(remoteUrl, localDestination);
    ```
    *-or-*
    ```c#
    using (HttpClient client = new HttpClient())
    {
        var contents = await client.GetStringAsync(url1);
        await File.WriteAllTextAsync(filePath, contents);
    }
    ```
    </ans>

#file=en-US/c-sharp/how-to-parse-html.md
    # Parsing HTML in C#?

    There are multiple libraries for parsing HTML in a .Net environment:
    <ans>
    - HtmlAgilityPack
      - Fizzler
    - AngleSharp
    - CsQuery
    </ans>

    **Know more:**
    - #ref=en-US/c-sharp/parsing-html-using-html-agility-pack.md
      - #ref=en-US/c-sharp/parsing-html-using-fizzler-extensions-for-html-agility-pack.md
    - #ref=en-US/c-sharp/parsing-html-using-angle-sharp.md
    - #ref=en-US/c-sharp/parsing-html-using-cs-query.md

#file=en-US/c-sharp/parsing-html-using-angle-sharp.md
    # Parsing HTML5 using Angle Sharp

    <ans>
    ```c#
    var parser = new HtmlParser();
    var document = await parser.ParseDocumentAsync(html);
    var linkElements = document.QuerySelectorAll("a");
    ```
    </ans>
    
    **Know more:**
    - #ref=https://anglesharp.github.io/
    - #ref=en-US/dot-net/what-is-angle-sharp.md

#file=en-US/c-sharp/parsing-html-using-html-agility-pack.md
    # Parsing HTML using HtmlAgilityPack

    <ans>
    ```c#
    var parser = new HtmlDocument();
    parser.LoadHtml(html);
    var linkElements = parser.DocumentNode.SelectNodes("//a[@href]");
    ```
    </ans>

    **Know more:**
    - #ref=en-US/c-sharp/parsing-html-using-fizzler-extensions-for-html-agility-pack.md
    - #ref=en-US/dot-net/what-is-html-agility-pack.md

#file=en-US/c-sharp/parsing-html-using-fizzler-extensions-for-html-agility-pack.md
    # Parsing HTML using CSS selectors with HtmlAgilityPack and Fizzler

    *Fizzler* is a library that contains extensions for *HtmlAgilityPack*
    that allows using CSS selectors instead of XPath.
    <ans>
    ```c#
    var parser = new HtmlDocument();
    parser.LoadHtml(html);
    var linkElements = parser.DocumentNode.QuerySelectorAll("a");
    ```
    </ans>

    **Know more:**
    - #ref=https://github.com/atifaziz/Fizzler
    - #ref=en-US/dot-net/what-is-html-agility-pack.md

#file=en-US/c-sharp/parsing-html-using-cs-query.md
    # Parsing HTML5 using CsQuery

    <ans>
    ```c#
    CQ cq = CQ.Create(html);
    var linkElements = cq.Find("a");
    ```
    </ans>

    **Know more:**
    - #ref=https://github.com/jamietre/CsQuery
    - #ref=en-US/dot-net/what-is-cs-query.md

#file=en-US/dot-net/what-is-angle-sharp.md
    #keywords=["anglesharp", "angle-sharp"]
    # What is AngleSharp?

    <ans>
    AngleSharp is a library made for parsing HTML in .Net environment.
    </ans>

    **Know more:**
    - #ref=https://anglesharp.github.io/

#file=en-US/dot-net/what-is-cs-query.md
    #keywords=["csquery", "cs-query"]
    # What is CsQuery?

    <ans>
    CsQuery is a library made for parsing HTML in .Net environment.
    It supports all CSS2 and CSS3 selectors.
    </ans>

    **Know more:**
    - #ref=https://github.com/jamietre/CsQuery

#file=en-US/dot-net/what-is-html-agility-pack.md
    #keywords=["htmlagilitypack", "html-agility-pack"]
    # What is HtmlAgilityPack?

    <ans>
    HtmlAgilityPack is a library made for parsing HTML in .Net environment.
    </ans>
    
    **Know more:**
    - #ref=https://html-agility-pack.net/

#file=en-US/python/initializing-pyprojectx-project-manager.md
    # Initializing a PyProjectX Python project

    <ans>
    Download PyProjectX tool to project directory:
    - Linux: `curl -LO https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip && unzip wrappers.zip && rm -f wrappers.zip`
    - Windows: `powershell
    Invoke-WebRequest https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip -OutFile wrappers.zip; Expand-Archive -Path wrappers.zip -DestinationPath .; Remove-Item -Path wrappers.zip
    `
    Then initialize, using one of the following:
    - `./pw --init pdm`
    - `./pw --init poetry`
    </ans>

#file=en-US/postgresql/string-concatenation.md
    # String concatenation in PosgreSQL

    <ans>
    ```sql
    SELECT 'a' || 'b'
    ```
    *-or-*
    ```sql
    SELECT concat('a', 'b')
    ```
    *-or-*
    ```sql
    SELECT concat_ws(',', 'a', 'b')
    ```
    </ans>

    *concat_ws* stands for concatenate with separator.

    **Know more:**
    - #ref=en-US/postgresql/string-concatenation-aggregation.md

    **References:**
    - #ref=https://www.postgresqltutorial.com/postgresql-string-functions/postgresql-concat-function/

#file=en-US/postgresql/string-concatenation-aggregation.md
    # String concatenation aggregation in PostgreSQL

    <ans>
    ```sql
    SELECT STRING_AGG(col_name, ',')
    FROM SampleTable
    ```
    </ans>

    **Know more:**
    - #ref=en-US/postgresql/string-concatenation.md

#file=en-US/postgresql/escaping-characters-in-string-literal.md
    # Escaping characters in String literal in PostgreSQL

    <ans>
    There is a special escaped string representation in PostgreSQL:
    ```sql
    SELECT 'line1' || E'\n' || 'line2'
    SELECT E'lin 1\nline 2'
    ```
    </ans>

    **Know more:**
    - #ref=en-US/postgresql/new-line-character.md
    - #ref=en-US/postgresql/enter-and-search-new-line-character-in-jsonb.md

#file=en-US/postgresql/new-line-character.md
    # New line character in PostgreSQL

    <ans>
    ```sql
    SELECT 'a' || chr(10) || 'b'
    SELECT 'a' || E'\n' || 'b'
    ```
    </ans>

    **Know more:**
    - #ref=en-US/postgresql/escaping-characters-in-string-literal.md
    - #ref=en-US/postgresql/enter-and-search-new-line-character-in-jsonb.md

#file=en-US/postgresql/enter-and-search-new-line-character-in-jsonb.md
    # Enter and search for new-line character in JSONB column in PostgreSQL

    <ans>
    ```sql
    with sample_table(jsonb_column) as (
        values ('{"data": "line 1\nline 2"}'::jsonb)
    )
    select *
    from sample_table
    where jsonb_column->>'data' ~ '^.*\n.*$'
    ```
    </ans>

    The escaped string '\n' has no special meaning in PostgreSQL,
    but it has a meaning inside JSONB column.

    If you try to enter a new line character (`chr(10)`) in a JSONB column,
    there will be an error stating:
    - Character with value 0x0a must be escaped.

    **Know more:**
    - #ref=en-US/postgresql/escaping-characters-in-string-literal.md
    - #ref=en-US/postgresql/new-line-character.md

#file=en-US/postgresql/return-any-row-in-aggregation.md
    # Enter and search for new-line character in JSONB column in PostgreSQL

    <ans>
    ```sql
    select distinct on (column1) column1, column2
    from sample_table
    ```
    *-or-*
    ```sql
    select column1, max(column2)
    from sample_table
    group by column1
    ```
    </ans>

    These examples return one of the values aggregated in *column2*.
    While the first example will return the first that it finds,
    the second will return the maximum value, which is one of the values.

    **References:**
    - #ref=https://stackoverflow.com/questions/42556344/aggregate-function-that-returns-any-value-for-a-group

#file=en-US/matplotlib/how-to-get-gridspec-from-axes.md
    # How to get the GridSpec from Axes in PyPlot?
    <ans>
    ```python
    ax.get_gridspec()
    ```
    </ans>
    
    **Know more:**
    - #ref=en-US/matplotlib/how-to-subdivide-axes-using-gridspec.md

#file=en-US/matplotlib/how-to-subdivide-axes-using-gridspec.md
    # How to subdivide Axes using GridSpec in PyPlot?
    <ans>
    ```python
    import matplotlib.gridspec as gridspec
    gs = ax.get_gridspec()
    subgs = gridspec.GridSpecFromSubplotSpec(
        2, 2,
        subplot_spec=gs,
        wspace=0.1, hspace=0.1)
    for it in range(len(subgs))
        ax = plt.Subplot(fig, inner[it])
        # ax.plot(...)
    ```
    </ans>

    **Know more:**
    - #ref=en-US/matplotlib/how-to-get-gridspec-from-axes.md

#file=en-US/streamlit/cache-data-from-function-between-runs.md
    # Cache data from a function between runs in StreamLit

    <ans>
    ```python
    import streamlit as st
    @st.cache_data
    def get_some_data():
        # ... do something here!
        return result
    ```
    </ans>

    **Know more:**
    - #ref=en-US/streamlit/clear-cache-for-function.md
    - #ref=en-US/streamlit/cache-function-data-in-disk.md

    **Reference:**
    - #ref=https://docs.streamlit.io/library/api-reference/performance/st.cache_data

#file=en-US/streamlit/clear-cache-for-function.md
    # Clear cache of a specific cached function in StreamLit

    <ans>
    Just call clear function on the cached function itself.
    
    ```python
    get_some_data.clear()
    ```
    </ans>

    ```python
    import streamlit as st
    @st.cache_data
    def get_some_data():
        # ... function code
        return result
    ```

    **Know more:**
    - #ref=en-US/streamlit/cache-data-from-function-between-runs.md
    - #ref=en-US/streamlit/cache-function-data-in-disk.md

    **Reference:**
    - #ref=https://docs.streamlit.io/library/api-reference/performance/st.cache_data

#file=en-US/streamlit/cache-function-data-in-disk.md
    # Cache function data in disk using StreamLit

    <ans>
    Use atribute *cache_data* with argument `persist="disk"`.
    
    ```python
    import streamlit as st
    @st.cache_data(persist="disk")
    def get_some_data():
        # ... function code!
        return result
    ```
    </ans>

    **Know more:**
    - #ref=en-US/streamlit/cache-data-from-function-between-runs.md
    - #ref=en-US/streamlit/clear-cache-for-function.md

    **Reference:**
    - #ref=https://docs.streamlit.io/library/api-reference/performance/st.cache_data

#file=en-US/matplotlib/creating-scatter-plot.md
    # Creating a scatter plot using MatPlotLib

    <ans>
    ```python
    import matplotlib.pyplot as plt
    plt.scatter(x=xs, y=ys, s=sizes, c=colors)
    ```
    </ans>

    Other important parameters:
    - marker
    - linewidths

    **Reference:**
    - #ref=https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

#file=en-US/matplotlib/scatter-plot-marker-size.md
    # How to change marker size in a scatter plot in MatPlotLib?

    <ans>
    Use *s* parameter with a single size value or an array of sizes:
    ```python
    import matplotlib.pyplot as plt
    plt.scatter(x=xs, y=ys, s=sizes, c=colors)
    ```
    </ans>

    **Know more:**
    - #ref=en-US/matplotlib/creating-scatter-plot.md

    **Reference:**
    - #ref=https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

#file=en-US/matplotlib/plot-distribution-from-data-using-seaborn.md
    # Plotting the distribution from data using SeaBorn and MatPlotLib

    A distribution can be represented by a PDF or a CDF using one of the following functions:

    <ans>
    ```python
    import seaborn as sns
    sns.kdeplot(data=values, cumulative=True)
    sns.histplot(values, bins=15, cumulative=True)
    sns.displot(values, kde=True, bins=15, cumulative=False)
    ```

    The *displot* function draws a histogram and a line chart of the distribution.

    Parameters:
    - **bins:** controls the number of bin for the histogram
    - **cumulative:** controls whether to draw PDF or CDF
    </ans>

    References:
    - #ref=https://seaborn.pydata.org/generated/seaborn.kdeplot.html

#file=en-US/numpy/cdf-distribution-from-pdf.md
    # Getting the CDF of a distribution given the PDF using NumPy

    <ans>
    ```python
    dX = 0.01 # X distance between values inside PDF
    cdf = np.cumsum(pdf*dX)
    ```
    </ans>

    References:
    - #ref=https://stackoverflow.com/a/9379432/195417

#file=en-US/python/list-installed-packages.md
    # How to list installed Python packages?

    <ans>
    ```bash
    pip list
    ```
    </ans>

#file=en-US/python/list-installed-packages-conda.md
    # How to list installed Python packages with Conda?

    <ans>
    ```bash
    conda list
    ```
    </ans>

#file=en-US/nssm/what-is-nssm.md
    # What is NSSM?

    <ans>
    Non-sucking Service Manager -
    Registers and runs anything as a service in Windows
    with multiple options, such as restart service if it stops.
    </ans>

#file=en-US/nssm/list-services.md
    # How to list NSSM services?

    <ans>
    ```bash
    nssm list
    ```
    </ans>

    *- or -* a more detailed list:
    
    ```powershell
    Get-WmiObject win32_service | ?{$_.PathName -like '*nssm*'} | select Name, DisplayName, State
    ```

#file=en-US/postgresql/create-date-type-value.md
    # Creating a Date type value in PostgreSQL

    <ans>
    ```sql
    DATE('2023-08-21')
    ```
    *- or -*
    ```sql
    '2023-08-21'::DATE
    ```
    </ans>

#file=en-US/postgresql/date-type-column-with-current-date.md
    # Creating a Date type column with current date as default value in PostgreSQL

    <ans>
    ```sql
    CREATE TABLE documents (
        ...
        some-Date DATE DEFAULT CURRENT_DATE
        ...
    );
    ```
    </ans>

#file=en-US/postgresql/get-current-date.md
    # Get current date in PostgreSQL

    <ans>
    ```sql
    now()::DATE
    ```
    *- or -*
    ```sql
    DATE(now())
    ```
    *- or -*
    ```sql
    CURRENT_DATE
    ```
    </ans>

    *Know more:*
    - #ref=en-US/postgresql/get-current-date-and-time.md
    - #ref=en-US/postgresql/get-current-time.md

#file=en-US/postgresql/get-current-date-and-time.md
    # Get current date and time in PostgreSQL

    <ans>
    ```sql
    now()
    ```
    *- or -*
    ```sql
    CURRENT_DATE + CURRENT_TIME
    ```
    </ans>

    *Know more:*
    - #ref=en-US/postgresql/get-current-date.md
    - #ref=en-US/postgresql/get-current-time.md

#file=en-US/postgresql/get-current-time.md
    # Get current time in PostgreSQL

    <ans>
    ```sql
    now()::TIME
    ```
    *- or -*
    ```sql
    CURRENT_TIME
    ```
    </ans>

    *Know more:*
    - #ref=en-US/postgresql/get-current-date-and-time.md
    - #ref=en-US/postgresql/get-current-date.md

#file=en-US/matplotlib/change-scatter-plot-transparency.md
    # How to change the transparency of a scatter plot points?
    <ans>
    Argument *alpha*:
    ```python
    ax.scatter(x=xs, y=ys, alpha=0.5)
    ```
    </ans>

    Where:
    - **0:** transparent
    - **1:** opaque

#file=en-US/git/force-end-of-line-to-lf-on-checkout.md
    # How to force end-of-lines to LF on checkout using git?

    <ans>
    Inside the *.gitattributes* file:
    ```
    *.txt text=auto eol=lf
    ```
    </ans>

#file=en-US/git/get-all-changes-but-dont-apply-them-immediately.md
    # How to get all changes from origin without applying them using git?

    <ans>
    ```bash
    git fetch --all
    ```
    </ans>

    **Remarks:**

    Use `git merge` afterwards to merge changes.

#file=en-US/pandoc/converting-markdown-containing-emojis-to-pdf.md
    # Converting MD containing emojis to PDF

    <ans>
    Use [Pandoc-Emojis-Filter](https://github.com/masbicudo/Pandoc-Emojis-Filter)
    </ans>

#file=en-US/bash/shebang.md
    # Shebang for Bash?

    <ans>
    ```bash
    #!/bin/bash
    ```
    </ans>

    `#!/usr/bin/env bash` is more portable, but less predictable.

#file=en-US/texlive/installing-packages.md
    # Installing new packages in TexLive

    <ans>
    Example - installing *xcolor* package:
    ```bash
    tlmgr install xcolor
    ```
    </ans>

#file=en-US/texlive/latex-error-file-footnote-sty-not-found.md
    # LaTeX Error: File 'footnote.sty' not found

    <ans>
    Install *mdwtools* package:
    ```bash
    tlmgr install mdwtools
    ```
    </ans>

#file=en-US/python/open-text-file.md
    # Open text file in Python

    <ans>
    with open("filename.txt") as fs:
        for line in fs:
            print(line)
    </ans>

    **Know more:**
    - #ref=en-US/python/open-binary-file.md

#file=en-US/python/open-binary-file.md
    # Open binary file in Python

    <ans>
    with open("filename.txt", "rb") as fs:
        for line in fs:
            print(line)
    </ans>

    **Remarks:**
    Even though lines are a concept of text files, it works with binary files too.

    **Know more:**
    - #ref=en-US/python/open-text-file.md

#file=en-US/bash/get-file-size.md
    # How to get the size of a file in bash script?

    <ans>
    ```bash
    stat -c%s "$filename"
    ```
    </ans>

#file=en-US/vscode/remove-all-extensions.md
    # How to remove all VS Code extensions?
    <ans>
    In Bash (Linux or Mac):

    ```bash
    rm -rf ~/.vscode/extensions
    ```

    In Batch (Windows CMD):

    ```bash
    rmdir %USERPROFILE%\.vscode\extensions /s
    ```
    </ans>

#file=en-US/c-sharp/detect-offline-or-not-synchronized-files.md
    # Detect offline or not synchronized files

    <ans>
    ```c#
    const FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS
        = (FileAttributes)4194304; // (0x00400000)
    var isNotReady = (File.GetAttributes(filename)
        & FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS) != 0;
    ```
    </ans>

    **References:**
    - #ref=https://learn.microsoft.com/pt-br/dotnet/api/system.io.fileattributes?view=net-7.0
    - #ref=https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants

#file=en-US/python/upgrade-pip.md

    <ans>
    ```bash
    python -m pip install --upgrade pip
    ```
    </ans>

#file=en-US/pdm/install-pdm.md

    # How to install PDM

    <ans>
    On Windows:

    ```powershell
    (Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python -
    ```

    On Linux/Mac:

    ```bash
    curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
    ```
    </ans>

    ```bash
    cd ~
    curl -sSLO https://pdm.fming.dev/dev/install-pdm.py
    python install-pdm.py --remove
    python install-pdm.py
    rm install-pdm.py
    ```

#file=en-US/python/get-currently-executing-filename.md
    # Get currently executing file name

    <ans>
    ```python
    __file__
    ```
    </ans>

    **Know more:**

    - #ref-en-US/python/get-currently-executing-file-path.md
    - #ref-en-US/python/get-current-working-directory.md

#file=en-US/python/get-currently-executing-file-path.md
    # Get currently executing file path

    <ans>
    ```python
    import pathlib
    pathlib.Path(__file__).parent.resolve()
    ```
    </ans>

    **Know more:**

    - #ref-en-US/python/get-currently-executing-filename.md
    - #ref-en-US/python/get-current-working-directory.md

#file=en-US/python/get-current-working-directory.md
    # Get current working directory

    <ans>
    ```python
    import pathlib
    pathlib.Path().resolve()
    ```
    </ans>

    **Know more:**

    - #ref-en-US/python/get-currently-executing-filename.md
    - #ref-en-US/python/get-currently-executing-file-path.md

#file=en-US/pyprojectx/what-is-it.md
    # What is Pyprojectx?

    <ans>
    Pyprojectx makes it easy to create all-inclusive Python projects; no need to install any tools upfront, not even Pyprojectx itself!
    </ans>

#file=en-US/pyprojectx/installing.md
    # Installing Pyprojectx to manage Python project

    <ans>
    - #ref=en-US/pyprojectx/install-in-bash.md
    - #ref=en-US/pyprojectx/install-in-powershell.md
    </ans>

#file=en-US/pyprojectx/install-in-bash.md
    # Installing Pyprojectx using Bash

    <ans>
    ```bash
    curl -LO https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip && unzip -o wrappers.zip && rm -f wrappers.zip
    ```
    </ans>

    Then setup files in Git:
    ```bash
    git add pw pw.bat
    git update-index --chmod=+x pw
    echo .pyprojectx/ >> .gitignore
    ```

    **Know more:**
    - #ref=en-US/pyprojectx/install-in-powershell.md
    - #ref=en-US/pyprojectx/initialize.md

#file=en-US/pyprojectx/install-in-powershell.md
    # Installing Pyprojectx using PowerShell

    <ans>
    ```powershell
    Invoke-WebRequest https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip -OutFile wrappers.zip; Expand-Archive -Force -Path wrappers.zip -DestinationPath .; Remove-Item -Path wrappers.zip
    ```
    </ans>

    Then setup files in Git:
    ```bash
    git add pw pw.bat
    git update-index --chmod=+x pw
    echo .pyprojectx/ >> .gitignore
    ```

    **Know more:**
    - #ref=en-US/pyprojectx/install-in-bash.md
    - #ref=en-US/pyprojectx/initialize.md

#file=en-US/pyprojectx/initialize.md
    # Initializing a Python project using Pyprojectx

    <ans>
    - #ref=en-US/pyprojectx/initialize-plain-python-project.md
    - #ref=en-US/pyprojectx/initialize-poetry-python-project.md
    - #ref=en-US/pyprojectx/initialize-pdm-python-project.md
    </ans>

#file=en-US/pyprojectx/initialize-plain-python-project.md
    # Initialize a plain Python project using Pyprojectx

    <ans>
    ```bash
    .\pw --init project
    ```

    **Know more:**
    - #ref=en-US/pyprojectx/installing.md
    - #ref=en-US/pyprojectx/initialize-poetry-python-project.md
    - #ref=en-US/pyprojectx/initialize-pdm-python-project.md


#file=en-US/pyprojectx/initialize-poetry-python-project.md
    # Initialize a project with poetry's init command using Pyprojectx

    <ans>
    ```bash
    .\pw --init poetry
    ```

    **Know more:**
    - #ref=en-US/pyprojectx/installing.md
    - #ref=en-US/pyprojectx/initialize-plain-python-project.md
    - #ref=en-US/pyprojectx/initialize-pdm-python-project.md

#file=en-US/pyprojectx/initialize-pdm-python-project.md
    # Initialize a project with pdm's init command using Pyprojectx

    <ans>
    ```bash
    .\pw --init pdm
    ```
    </ans>

    **Know more:**
    - #ref=en-US/pyprojectx/installing.md
    - #ref=en-US/pyprojectx/initialize-plain-python-project.md
    - #ref=en-US/pyprojectx/initialize-poetry-python-project.md

#file=en-US/pdm/adding-library-dependencies.md
    # Adding library dependencies using PDM

    <ans>
    ```bash
    pdm add pandas numpy
    ```
    </ans>

    You can specify multiple package names.

    **Know more:**
    - #ref=en-US/pdm/adding-development-library-dependencies.md
    - #ref=en-US/pdm/adding-editable-library-dependencies.md

#file=en-US/pdm/adding-development-library-dependencies.md
    # Adding development library dependencies using PDM

    <ans>
    ```bash
    pdm add pandas --dev
    ```
    </ans>

    You can specify multiple package names.

    **Know more:**
    - #ref=en-US/pdm/adding-library-dependencies.md
    - #ref=en-US/pdm/adding-editable-library-dependencies.md

#file=en-US/pdm/adding-editable-library-dependencies.md
    # Adding editable library dependencies using PDM

    <ans>
    ```bash
    # A relative path to the directory
    pdm add -e ./sub-package --dev
    # A file URL to a local directory
    pdm add -e file:///path/to/sub-package --dev
    # A VCS URL
    pdm add -e git+https://github.com/pallets/click.git@main#egg=click --dev
    ```
    </ans>

    **Remarks:**
    Editable installs are only allowed in the dev dependency group.

    **Know more:**
    - #ref=en-US/pdm/adding-library-dependencies.md
    - #ref=en-US/pdm/adding-development-library-dependencies.md

#file=en-US/pdm/error-cannot-add-editables-to-default-or-optional-dependency-group.md
    # [PdmUsageError]: Cannot add editables to the default or optional dependency group

    <ans>
    Editables must be added to the *dev* dependency group, by using `--dev`.
    </ans>

    **Know more:**
    - #ref=en-US/pdm/adding-editable-library-dependencies.md
    - #ref=en-US/pdm/adding-development-library-dependencies.md

#file=en-US/vscode/error-crashing-on-restart.md
    # Crashing on restarting VS Code

    <ans>
    If you see the following after restarting VS Code:
    > We are sorry for the inconvenience!
    > You can reopen the window to continue where you left off.
    Just downgrade, some versions of VS Code are bogus.
    <ans>

#file=en-US/vscode/change-indentation-of-tree-file-structure.md
    # How to change indentation in VS Code tree file structure?

    <ans>
    1. Go to *File* > *Preference* > *Settings*
    2. In the search box type: *tree indent*
    3. Option *Workbench › Tree: Indent*

    *- or -*

    1. In your *settings.json* file
    2. Enter this: `"workbench.tree.indent": 20`
    <ans>

#file=en-US/c-sharp/generating-criptographic-signature-of-a-stream.md
    # Generating a criptographic hash of a stream in C#

    <ans>
    ```c#
    using System.Security.Cryptography;
    var algorithm = SHA256.Create();
    var hash = await algorithm.ComputeHashAsync(stream);
    return Convert.ToBase64String(hash);
    ```
    </ans>

#file=en-US/powershell/get-directory-size.md
    # Get directory size in PowerShell

    <ans>
    Example - measuring Documents folder:
    ```powershell
    ls -r ~/Documents | measure -sum Length
    ```
    </ans>

    You can do it from CMD:
    ```bash
    powershell -noprofile -command "ls -r ~/Documents | measure -sum Length"
    ```

#file=en-US/powershell/run-powershell-command-from-cmd.md
    # Run PowerShell command from CMD

    <ans>
    Example - running *ls*:
    ```powershell
    powershell -noprofile -command "ls"
    ```
    </ans>

#file=en-US/python/argparse-attribute-error-namespace-object-has-no-attribute-name.md
    # AttributeError: 'Namespace' object has no attribute 'name'

    <ans>
    Use `args.name` instead of `args["name"]`
    </ans>

#file=en-US/python/argparse-show-help-if-no-arguments.md
    # Display help message when no arguments are provided using Python argparse

    <ans>
    ```
    if len(sys.argv) == 1:
        parser.print_usage(sys.stderr)
        sys.exit(1)
    ```
    </ans>

#file=en-US/c-sharp/list-files-in-directory.md
    # List files in directory in C#

    <ans>
    ```c#
    var allfiles = Directory.GetFiles(
            "D:\",
            "*",
            SearchOption.AllDirectories
        );
    ```
    </ans>

    **Remarks:**

    This may fail with *UnauthorizedAccessException* if any path in the structure requires privileges you don't have.

    If you need directories too, use `Directory.GetFileSystemEntries`.

#file=en-US/licensing/cc-by-sa-30.md
    # What is CC BY-SA 3.0?

    <ans>
    Attribution-ShareAlike 3.0 Unported
    - Can share and adapt
    - Must give attribution, and be under same license, without other restrictions
    </ans>

    **References:**
    - #ref=https://creativecommons.org/licenses/by-sa/3.0/

#file=en-US/python/checking-variable-exists-in-namespace.md
    # Checking if variable exists in *Namespace* in Python

    <ans>
    ```python
    hasattr(ns, "name")
    ```
    *- or -*
    ```python
    'name' in vars(ns)
    ```
    </ans>

#file=en-US/python/get-list-of-true-values-in-namespace.md
    # Get a list of True values inside a *Namespace* in Python

    <ans>
    ```python
    list_true_keys = [ k for (k, v) in ns.items() if v ]
    ```
    </ans>

#file=en-US/python/group-iterable-list-in-chunks.md
    # Group iterable sequence in chunks of N elements in Python

    <ans>
    ```python
    import itertools as it
    def grouped(chunk_size, sequence):
        iterable = iter(sequence)
        return iter(lambda: (*it.islice(iterable, chunk_size),), ())
    ```
    </ans>

#file=en-US/python/convert-list-of-characters-into-string.md
    # Convert list of characters into string in Python

    <ans>
    ```python
    "".join(["a", "b", "c"])
    ```
    </ans>

#file=en-US/python/convert-char-code-to-string.md
    # Convert char-code to string in Python

    <ans>
    ```python
    chr(97)
    ```
    </ans>

    **Know more:**
    - #ref=en-US/python/convert-character-to-char-code.md

#file=en-US/python/convert-character-to-char-code.md
    # Convert string containing character to char-code in Python

    <ans>
    ```python
    ord('a')
    ```
    </ans>

    **Know more:**
    - #ref=en-US/python/convert-char-code-to-string.md

#file=en-US/python/urllib2-httperror-403-forbidden-with-urlopen.md
    # urllib2.HTTPError: HTTP Error 403: Forbidden using urlopen in Python

    <ans>
    ```python
    headers = { 'User-Agent': 'Mozilla/5.0' }
    request = Request(uri, headers=headers)
    stream = urlopen(request)
    ```
    </ans>

    **Remarks:**

    When using a URL string with `urlopen` the header *User-Agent* is not defined,
    and this causes the server to return 403 Forbidden.

#file=en-US/python/time-delays-using-time-sleep.md
    # Time delays using `time.sleep` in Python

    <ans>
    ```python
    time.sleep(10) # 10 seconds
    ```
    </ans>

    **Prerequisite:**

    ```python
    import time
    ```

#file=en-US/python/re-raise-exception-without-chaining.md
    # Re-raise exception without chaining in Python

    <ans>
    Use `raise exc from None` to remove parent exceptions.
    </ans>

    **Example:**

    ```python
    try: # ...
    except Exception ex1: # ...
        try: # ...
        except Exception ex2: # ...
            raise ex1 from None
    ```

    **Related:**
    - #ref=en-US/python/re-raise-exception.md
    - #ref=en-US/python/raise-exception.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/python/re-raise-exception.md
    # Re-raise exception in Python

    <ans>
    Use `raise` to re-raise exception.
    </ans>

    **Example:**

    ```python
    try: # ...
    except: # ...
        print("Error occurred")
        raise
    ```

    **Related:**
    - #ref=en-US/python/re-raise-exception-without-chaining.md
    - #ref=en-US/python/raise-exception.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/python/raise-exception.md
    # Raise exception in Python

    <ans>
    ```python
    raise Exception("Error")
    ```
    </ans>

    **Related:**
    - #ref=en-US/python/re-raise-exception.md
    - #ref=en-US/python/re-raise-exception-without-chaining.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/python/raise-exception-from-none.md
    # Raise exception from None in Python

    <ans>
    Remove parent exceptions, e.g. when exception is raised in the except block of another exception.
    </ans>

    **Example:**
    ```python
    try: # ...
    except ex1:
        try: # ...
        except ex2:
            # ex1 is parent of ex2
            # use from None to force parent to be None
            raise ex2 from None
    ```

    **Related:**
    - #ref=en-US/python/re-raise-exception-without-chaining.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/numpy/sum-all-items-in-multi-dimensional-array.md
    # Sum multi-dimensional array along all axes using NumPy

    <ans>
    ```python
    numpy.sum(a)
    ```
    </ans>

    **Remarks:**

    The sum function from NumPy has an *axes* parameter which defaults to `None`, causing NumPy to sum over all axes.

    **References:**
    - #ref=https://numpy.org/doc/stable/reference/generated/numpy.sum.html

#file=en-US/numpy/get-total-size-of-multi-dimensional-array.md
    # Get total size/length of multi-dimensional array using NumPy

    <ans>
    Use *size* property, instead of *len* function.
    ```python
    a.size
    ```
    </ans>

    **Remarks:**

    Python's `len` function will not give number of elements in NumPy multi-dimensional array.

    `size` property is the multiplication of all items in `shape` property.

    **References:**
    - #ref=https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html

#file=en-US/opencv/thresholding-multi-channel-images.md
    # Thresholding multi-channel images like CMYK using OpenCV

    <ans>
    ```python
    # Thresholding C and K values
    binaryImage = cv.inRange(
        inputImageCMYK,
        (128,   0,   0,   0),
        (255, 255, 255, 196))
    ```
    </ans>

    **Remarks:**

    You can then display the thresholded images:
    ```python
    plt.imshow(binaryImage, cmap='gray')
    ```

#file=en-US/opencv/saving-jpeg-image-file.md
    # Saving jpeg image file using OpenCV

    <ans>
    ```python
    cv2.imwrite("some.jpg", img)
    ```
    </ans>

#file=en-US/opencv/loading-images-with-imread-return-none.md
    # Loading images with `imread` return None in OpenCV

    <ans>
    OpenCV `imread` fails silently in multiple situations:
    - File doesn't exist
    - File name or path contains non-ASCII characters
    </ans>

#file=en-US/opencv/images-not-opening-with-imread.md
    # OpenCV not opening images with `imread` in Python
    #include=en-US/opencv/loading-images-with-imread-return-none.md

#file=en-US/pandas/create-timestamp-without-timezone.md
    # Creating a timestamp without timezone using Pandas

    <ans>
    ```python
    timestamp = pd.Timestamp('2024-02-14 22:15:14')
    ```
    </ans>

    **References:**
    - #ref=en-US/pandas/create-timestamp-with-timezone.md
    - #ref=en-US/pandas/remove-timezone-from-timestamp.md

#file=en-US/pandas/create-timestamp-with-timezone.md
    # Creating a timestamp with timezone using Pandas

    <ans>
    ```python
    timestamp = pd.Timestamp(
        '2024-02-14 22:15:14',
        tz='America/Sao_Paulo')
    ```
    </ans>

    **References:**
    - #ref=en-US/pandas/create-timestamp-without-timezone.md
    - #ref=en-US/pandas/remove-timezone-from-timestamp.md

#file=en-US/pandas/remove-timezone-from-timestamp.md
    # Removing timezone from a Pandas timestamp

    <ans>
    ```python
    timestamp.tz_localize(None)
    ```
    </ans>

    **References:**
    - #ref=en-US/pandas/create-timestamp-with-timezone.md

#file=en-US/python/get-type-name-of-object.md
    # Get type name of an object in Python

    <ans>
    ```python
    type(obj).__name__
    ```
    </ans>

#file=en-US/pandas/convert-ndarray-with-dates-to-pandas-series-with-timestamps.md
    # Convert ndarray with dates to Pandas series with timestamps

    <ans>
    ```python
    pd.to_datetime(ndarray_with_dates)
    ```
    </ans>

#file=en-US/numpy/convert-ndarray-with-dates-to-pandas-series-with-timestamps.md
    # Convert ndarray with dates to Pandas series with timestamps
    #include=en-US/pandas/convert-ndarray-with-dates-to-pandas-series-with-timestamps.md

#file=en-US/python/what-actions-are-available-in-warnings-simplefilter.md
    # Whats actions are available for `warnings.simplefilter` in Python

    <ans>
    - "ignore": Never print.
    - "error": Treat as errors.
    - "always": Always print.
    - "default": Print once per code location.
    - "module": Print once per module.
    - "once": Print once.
    </ans>

#file=en-US/python/treating-errors.md
    # Treating errors in Python

    <ans>
    ```python
    try: # code to try
    except Exception as ex: # execute on error
    else: # execute only if no errors
    finally: # always execute
    ```
    </ans>

    **Remarks:**
    - You can omit exception variable name and type.
    - Multiple `except` blocks with different types are allowed.

    **Related:**
    - #ref=en-US/python/raising-errors.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/python/handling-multiple-exception-types-same-block.md
    # Handling multiple exception types in the same `except` block in Python

    <ans>
    except (ExceptionType1, ExceptionType2):
    </ans>

    **Related:**
    - #ref=en-US/python/treating-errors.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/python/raising-errors.md
    # Raising errors in Python

    <ans>
    ```python
    raise Exception("Error")
    ```
    </ans>

    **Related:**
    - #ref=en-US/python/treating-errors.md

    **References:**
    - #ref=https://docs.python.org/3/tutorial/errors.html

#file=en-US/python/treating-future-warnings-as-errors.md
    # Treating `FutureWarning` as errors in Python

    <ans>
    ```python
    warnings.simplefilter('error', FutureWarning)
    ```
    </ans>

    **Remarks:**
    You can undo the change using:
    ```python
    warnings.simplefilter('default', FutureWarning)
    ```

    **References:**
    - #ref=en-US/python/what-actions-are-available-in-warnings-simplefilter.md

#file=en-US/python/decoding-web-requests-returning-json.md
    # Descoding web-requests returning JSON in Python

    <ans>
    ```python
    data = requests.get(url).json()
    ```
    </ans>

    **Prerequisite:**
    ```python
    import requests
    ```

    **Alternative:**
    - #ref=en-US/python/decoding-json-web-requests-using-urllib.md

#file=en-US/python/decoding-json-web-requests-using-urllib.md
    # Descoding JSON web-requests using URL-Lib in Python

    <ans>
    ```python
    data = json.load(urllib.request.urlopen(url))
    ```
    </ans>

    **Prerequisite:**
    ```python
    import json
    import urllib.request
    ```

    **Alternative:**
    - #ref=en-US/python/decoding-web-requests-returning-json.md

#file=en-US/pyenv-win/listing-python-versions-to-install.md
    # Listing Python versions to install in PyEnv-Win

    <ans>
    ```powershell
    pyenv install -l
    ```
    </ans>

    If you don't see the desired Python version, update the version cache:
    ```powershell
    pyenv update
    ```

    **Related:**
    - #ref=en-US/pyenv-win/listing-installed-python-versions.md
    - #ref=en-US/pyenv-win/installing-python-version.md

    **References:**
    See [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)

#file=en-US/pyenv-win/listing-installed-python-versions.md
    # Listing installed Python versions in PyEnv-Win

    <ans>
    ```powershell
    pyenv versions
    ```
    </ans>

    **Related:**
    - #ref=en-US/pyenv-win/listing-python-versions-to-install.md

    **References:**
    See [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)

#file=en-US/pyenv-win/installing-python-version.md
    # Installing Python version in PyEnv-Win

    <ans>
    ```powershell
    pyenv install 3.12.2
    ```
    </ans>

    **Related:**
    - #ref=en-US/pyenv-win/listing-python-versions-to-install.md

    **References:**
    See [pyenv for Windows](https://github.com/pyenv-win/pyenv-win)

#file=en-US/python/running-http-server-returning-empty-response.md
    # Running `http.server` returning `ERR_EMPTY_RESPONSE` in Python

    <ans>
    Add a binding to localhost when running:
    ```bash
    python -m http.server 8000 --bind localhost
    ```
    </ans>

    **Related:**
    - #ref=en-US/python/running-http-server-returning-invalid-address.md
    - #ref=en-US/python/running-http-server-returning-connection-refused.md

#file=en-US/python/running-http-server-returning-invalid-address.md
    # Running `http.server` returning `ERR_ADDRESS_INVALID` in Python

    <ans>
    Use a valid IP or hostname to access the server:
    - localhost
    - 127.0.0.1
    
    You can bind to 0.0.0.0, but not access it.
    </ans>

    **Remarks:**
    Binding to 0.0.0.0 means to accept any IP address when connecting.

    **Related:**
    - #ref=en-US/python/running-http-server-returning-empty-response.md
    - #ref=en-US/python/running-http-server-returning-connection-refused.md

#file=en-US/python/running-http-server-returning-connection-refused.md
    # Running `http.server` returning `ERR_CONNECTION_REFUSED` in Python

    <ans>
    You need to use the specific binding IP or hostname to access the server:
    Either:
    - http://localhost &lt;or&gt;
    - http://127.0.0.1
    </ans>

    **Related:**
    - #ref=en-US/python/running-http-server-returning-empty-response.md
    - #ref=en-US/python/running-http-server-returning-invalid-address.md

#file=en-US/matplotlib/italics-in-texts.md
    # Italics in texts using Matplotlib

    <ans>
    ```python
    plt.title(r"$\mathit{text in italics}$")
    ```
    </ans>

    **Related:**
    - #ref=en-US/matplotlib/text-formating.md
    - #ref=en-US/matplotlib/bold-italic-texts.md

    **References:**
    - #ref=https://matplotlib.org/stable/users/explain/text/mathtext.html

#file=en-US/matplotlib/bolded-texts.md
    # Bold font using Matplotlib

    <ans>
    ```python
    plt.title(r"$\mathbf{text in bold}$")
    ```
    </ans>

    **Related:**
    - #ref=en-US/matplotlib/text-formating.md
    - #ref=en-US/matplotlib/bold-italic-texts.md

    **References:**
    - #ref=https://matplotlib.org/stable/users/explain/text/mathtext.html

#file=en-US/matplotlib/bold-italic-texts.md
    # Bold italic using Matplotlib

    <ans>
    ```python
    plt.title(r"$\mathbfit{text in bold italic}$")
    ```
    </ans>

    **Related:**
    - #ref=en-US/matplotlib/text-formating.md
    - #ref=en-US/matplotlib/italics-in-texts.md
    - #ref=en-US/matplotlib/bolded-texts.md

    **References:**
    - #ref=https://matplotlib.org/stable/users/explain/text/mathtext.html

#file=en-US/matplotlib/text-formating.md
    # Text formating in Matplolib

    <ans>
    - `\mathit{}`: default (italic)
    - `\mathrm{}`: Roman (upright)
    - `\mathtt{}`: Typewriter (monospace)
    - `\mathbf{}`: bold
    - `\mathbfit{}`: bold italic
    - `\mathcal{}`: calligraphic
    - `\mathsf{}`: sans-serif
    </ans>

    **References:**
    - #ref=https://matplotlib.org/stable/users/explain/text/mathtext.html

#file=en-US/matplotlib/math-notation-in-texts.md
    # Math notation in texts using Matplotlib

    <ans>
    ```python
    plt.title("$y = x^2$")
    ```
    </ans>

    Note that backslashes `'\'` must be escaped (e.g. `"\\alpha"`), or used inside raw strings (e.g. `r"\alpha"`).

    **Related:**
    - #ref=en-US/matplotlib/text-formating.md

    **References:**
    - #ref=https://matplotlib.org/stable/users/explain/text/mathtext.html

#file=en-US/pandas/convert-datetime-to-timestamp.md
    # Convert datetime to Timestamp format in Pandas

    <ans>
    ```python
    pd.to_datetime(dt.datetime(2024, 3, 31)) # dtype('<M8[ns]')
    pd.to_datetime(dt.date(2024, 3, 31)) # dtype('<M8[ns]')
    ```
    </ans>

    **Related:**
    - #ref=en-US/numpy/convert-datetime-to-datetime64.md

#file=en-US/numpy/convert-datetime-to-datetime64.md
    # Convert datetime to datetime64 format in NumPy

    <ans>
    ```python
    np.datetime64(dt.datetime(2024, 3, 31)) # dtype('<M8[us]')
    pd.datetime64(dt.date(2024, 3, 31)) # dtype('<M8[D]')
    ```
    </ans>

    **Related:**
    - #ref=en-US/pandas/convert-datetime-to-timestamp.md
    - #ref=en-US/numpy/converting-datetime64-formats.md

#file=en-US/numpy/converting-datetime64-formats.md
    # Converting datetime64 formats using NumPy

    <ans>
    dt64d.astype("<M8[us]")
    dt64ns.astype("<M8[D]")
    </ans>

    **Remarks:**
    NumPy can store date and times in multiple formats inside datetime64.
    The stored int64, which can be accessed using `value` property may be different even if the represented date is the same.

    **Related:**
    - #ref=en-US/numpy/convert-datetime-to-datetime64.md

#file=en-US/cudf/native-windows-installation.md
    # Can cuDF be installed natively in Windows

    <ans>
    cuDF does not support Windows natively, only via WSL2.
    </ans>

#file=en-US/cudf/requirements.md
    # Requirements for cuDF

    <ans>
    - GPU: NVIDIA Volta™ with compute capability 7.0+
    - OS: Ubuntu 20 or 22 / CentOS 7 / Rocky Linux 8 / Windows 11 with WSL2
    - CUDA: 11 / 12 + updated drivers
    </ans>

    **References:**
    - #ref=https://docs.rapids.ai/install#system-req

#file=en-US/cupy/requirements.md
    # Requirements for using cuPy

    <ans>
    - GPU: NVIDIA with CUDA support
    - CUDA: 11 / 12 + updated drivers
    - C++ compiler: MSVC on Windows / g++ on Linux
    </ans>

    **References:**
    - #ref=https://docs.cupy.dev/en/stable/install.html#requirements
    - #ref=https://docs.cupy.dev/_/downloads/en/v7.3.0/pdf/

#file=en-US/cupy/installing.md
    # Installing cuPy

    <ans>
    - step 1
        ```bash
        python -m pip install -U setuptools pip
        ```
    - step 2
        ```bash
        pip install cupy-cuda11x
        # =or= pip install cupy-cuda12x
        ```
    - step 3
        Install MSVC on Windows =or= g++ on Linux
    </ans>

    **References:**
    - #ref=https://docs.cupy.dev/en/stable/install.html
    - #ref=https://docs.cupy.dev/_/downloads/en/v7.3.0/pdf/

#file=en-US/scipy/remove-drift-from-data.md
    # Removing linear tendency (or drift) from data using SciPy

    <ans>
    ```python
    def remove_linear_drift(data):
        x = np.arange(len(data))
        return data - stats.linregress(x, data).slope * x
    ```
    </ans>

#file=en-US/python/hashing-a-function-object.md
    # Hashing a function object in Python

    <ans>
    ```python
    def get_function_hash(fn):
        return hash((
            inspect.getsource(fn),
            get_function_closures(fn),
            get_function_globals(fn),
        ))
    ```
    See related content for `get_function_closures` and `get_function_globals` implementations.
    </ans>

    **Requirements:**
    ```python
    import inspect
    ```

    **Related:**
    - #ref=en-US/python/get-closure-variables-used-by-function.md
    - #ref=en-US/python/get-global-context-variables-used-by-function.md

#file=en-US/python/get-closure-variables-used-by-function.md
    # Get closure variables used by a function in Python

    <ans>
    ```python
    def get_function_closures(fn):
        return (*(
                closure.cell_contents
                for closure
                in fn.__closure__
            ),)
    ```
    </ans>

    **Related:**
    - #ref=en-US/python/get-global-context-variables-used-by-function.md

#file=en-US/python/get-global-context-variables-used-by-function.md
    # Get global context variables used by a function in Python

    <ans>
    ```python
    def get_function_globals(fn):
        return (*(
                fn.__globals__[instruction.argval]
                for instruction
                in dis.Bytecode(fn)
                if instruction.opname == 'LOAD_GLOBAL'
            ),)
    ```
    </ans>

    **Requirements:**
    ```python
    import dis
    ```

    **Related:**
    - #ref=en-US/python/get-closure-variables-used-by-function.md

#file=en-US/windows-cmd/split-commands-in-multiple-lines-in-batch-file.md
    # Split commands in multiple lines in a batch file

    <ans>
    ```bat
    somecommand ^
        --param1
    ```
    </ans>

#file=en-US/windows-cmd/what-is-windows-command-prompt.md
    # What is Windows Command Prompt (CMD)?

    <ans>
    It is an instruction parser used to issue commands to the computer and execute programs.
    </ans>

    **Related:**
    - #ref=en-US/windows-cmd/what-is-windows-command-file.md

#file=en-US/windows-cmd/what-is-windows-batch-file.md
    # What is a Windows batch file (*.bat)?

    <ans>
    It is a script file that executes Windows Command Prompt instructions.
    </ans>

    **Related:**
    - #ref=en-US/windows-cmd/what-is-windows-command-prompt.md
    - #ref=en-US/windows-cmd/what-is-windows-command-file.md

#file=en-US/windows-cmd/what-is-windows-command-file.md
    # What is a Windows command file (*.cmd)?

    <ans>
    It is a script file that executes Windows Command Prompt instructions.
    </ans>

    **Related:**
    - #ref=en-US/windows-cmd/what-is-windows-command-prompt.md
    - #ref=en-US/windows-cmd/what-is-windows-batch-file.md

#file=en-US/gallery-dl/what-is-gallery-dl.md
    # What is gallery-dl?

    <ans>
    It is used to batch download picture files from online gallery sites such as Pinterest.
    </ans>

#file=en-US/gallery-dl/skip-already-downloaded-files.md
    # Skipping already downloaded files using gallery-dl

    <ans>
    It skips already downloaded files by default. =)
    </ans>

#file=en-US/gallery-dl/write-metadata-about-galleries-and-files.md
    # Write metadata about galleries and files using `gallery-dl`

    <ans>
    Use the arguments:
    - `--write-metadata`: Write metadata to separate JSON files
    - `--write-info-json`: Write gallery metadata to a info.json file
    </ans>

#file=en-US/gallery-dl/install-using-choco.md
    # Install gallery-dl using Chocolatey

    <ans>
    ```bash
    choco upgrade -y gallery-dl
    ```
    </ans>

    **Related:**
    - #ref=en-US/chocolatey/what-is-choco.md

#file=en-US/chocolatey/what-is-choco.md
    # What is Chocolatey?

    <ans>
    It is a package manager for Windows which manages installed softwares.
    </ans>

    **Remarks:**
    Choco packages may also add [shims](/en-US/chocolatey/what-are-shims) to help running programs in the command line.

#file=en-US/chocolatey/what-are-shims.md
    # What are Shims created by Chocolatey packages?

    <ans>
    Shims are program shortcuts in the form of an executable.
    They are used to relocate a program to a common folder, such that only a single folder is needed for many programs in the PATH environment variable.
    </ans>

#file=en-US/numpy/create-range-of-date-times.md
    # Creating a range of date-times using NumPy

    <ans>
    ```python
    date_range = np.arange(
            dt.datetime(2024, 1, 1),
            dt.datetime(2025, 1, 1),
            dt.timedelta(days=1),
        )
    ```
    </ans>

    The element types of the resulting array will be `datetime64`, with dtype `'<M8[us]'`.

#file=en-US/latex/creating-figures-with-multiple-images.md
    # Creating figures with multiple images in LaTeX

    <ans>
    ```
    \begin{figure}
        \begin{subfigure}
        \end{subfigure}
    \end{figure}
    ```
    </ans>

#file=en-US/markdown/list-of-supported-markdown-language.md
    # List of supported Markdown languages in code blocks

    <ans>
    See [highlight.js/SUPPORTED_LANGUAGES.md](https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md)
    </ans>

#file=en-US/markdown/creating-latex-code-block.md
    # LaTeX code inside a Markdown file

    <ans>
    ````
    ```tex
    \LaTeX code inside Markdown
    ```
    ````
    </ans>

    **References:**
    - [highlight.js/SUPPORTED_LANGUAGES.md](https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md)

#file=en-US/latex/creating-latex-logo-using-latex.md
    # Creating LaTeX logo using LaTeX

    <ans>
    ```tex
    \LaTeX
    ```
    </ans>

    **Example:**

    $$\LaTeX$$

    **Related:**
    - #ref=en-US/latex/creating-latex-logo-using-unicode.md

#file=en-US/latex/creating-latex-logo-using-unicode.md
    # Creating LaTeX logo using unicode

    <ans>
    <roman>LᴬTᴇX</roman>

    *=or=*

    LaTeX
    </ans>

    **Related:**
    - #ref=en-US/latex/creating-latex-logo-using-latex.md

    **References:**
    - [Letter a](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/vollmann_ralf/Computersachen/uni_letter_a.html)
    - [Letter e](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/vollmann_ralf/Computersachen/uni_letter_e.html)

#file=en-US/jekyll/adding-support-for-latex-using-mathjax.md
    # Adding support for LaTeX using MathJax

    <ans>
    Add the following to your `_layouts/default.html` page:
    ```html
    <script type="text/javascript" id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    ```
    </ans>

    **References:**
    - #ref=https://stackoverflow.com/questions/34347818/using-mathjax-on-a-github-page

#file=en-US/github-pages/adding-support-for-latex-with-mathjax.md
    # Adding support for LaTeX with MathJax using GitHub Pages
    #include=en-US/jekyll/adding-support-for-latex-using-mathjax.md

#file=en-US/tech_name/article_name.md
    #delete
    # Title

    <ans>
    </ans>

    **Related:**
    - #ref=

#file=en-US/tech_name/article_name.md
    #delete
    # Title

    <ans>
    </ans>

    **Related:**
    - #ref=

#file=en-US/tech_name/article_name.md
    #delete
    # Title

    <ans>
    </ans>

    **Related:**
    - #ref=

#file=en-US/tech_name/article_name.md
    #delete
    # Title

    <ans>
    </ans>

    **Related:**
    - #ref=

#file=en-US/tech_name/article_name.md
    #delete
    # Title

    <ans>
    </ans>

    **Related:**
    - #ref=

#file=_.md
    #ref=https://realpython.com/python-modulo-operator/#how-to-check-if-a-number-is-even-or-odd
    #ref=https://jekyllrb.com/docs/variables/
    #ref=https://github.com/daattali/beautiful-jekyll
    #ref=https://flaviocopes.com/postgres-how-to-list-tables-database/
    #ref=https://python-poetry.org/
