---
title: Create data URI from web content in JavaScript
generated: true
---

    <div markdown="1" class="ans">
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
    </div>

    #### Usage

    ```js
    get_data_uri_from_web_content("https://api.github.com/repos/masbicudo/oqueeh")
	    .then(data_uri => document.write(data_uri))
    ```

    [Data URI generator](/en-US/html/data-uri-generator)
