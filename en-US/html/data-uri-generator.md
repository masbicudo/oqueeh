---
title: Data URI generator
generated: true
---

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
