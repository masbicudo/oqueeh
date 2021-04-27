#file=python/remove-spaces-at-end-of-string.md
    ---
    title: Remove spaces at end of string in Python
    ---

    <ans>
    ```python
    "MASBicudo  ".rstrip()
    ```
    </ans>

    Result is `"MASBicudo"`.

#file=python/remove-spaces-at-start-of-string.md
    ---
    title: Remove spaces at start of string in Python
    ---

    <ans>
    ```python
    "  MASBicudo".lstrip()
    ```
    </ans>

    Result is `"MASBicudo"`.

#file=python/remove-spaces-surrounding-string.md
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

#file=python/remove-characters-at-end-of-string.md
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

#file=python/remove-characters-at-start-of-string.md
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

#file=python/remove-characters-surrounding-string.md
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

#file=python/slice-array.md
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

#file=python/tuples-immutable-lists.md
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

#file=python/remove-item-from-tuple.md
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

#file=python/pop-or-dequee-item-from-tuple.md
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

#file=jekyll/iterating-tags.md
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

#file=jekyll/convert-date-to-string.md
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

#file=jekyll/supported-languages-in-a-code-block.md
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

#file=python/check-number-is-even-or-odd.md
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

#file=jekyll/categories-of-page-is-empty.md
    ---
    title: Categories of page is empty in Jekyll
    ---

    <ans>
    Only posts are assigned categories automatically by looking at folder structure.
    </ans>

    For pages to have categories, they must indicate them in the **front matter**.

#file=jekyll/front-matter.md
    ---
    title: Front matter in Jekyll
    ---

    #ref=http://simpleprimate.com/blog/front-matter

    <ans>
    {% raw %}
    ```
    ---
    title: Title of the page or post
    ---
    ```
    {% endraw %}
    </ans>

    The front matter of a Jekyll page is like a header of the file.

    It is used to define variables associated with the file.

    These variables are then used in various contexts.

    The variables go directly into the `page` or `post` variable.

    ```
    {{ page.title }}
    ```

#file=jekyll/last-item-of-array.md
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

#file=css/custom-properties.md
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

#file=css/font-size-relative-to-resolution.md
    #publish=false
    ---
    title: Font size relative to resolution in CSS
    ---

    #ref=https://stackoverflow.com/questions/16385559/how-to-change-the-font-size-proportionally-to-the-change-size-of-the-window-in-c/25780238
    #ref=https://stackoverflow.com/questions/41062123/css-font-size-responsive-relative-to-device-resolution
    #ref=https://www.w3schools.com/css/css_rwd_mediaqueries.asp
    #ref=https://stackoverflow.com/questions/11777598/font-size-relative-to-the-users-screen-resolution

#file=python/cannot-read-open-mode-x.md
    ---
    title: Cannot read from file opened with mode "x" in Python
    ---

    <ans>
    Mode "x" is write only, to also read from file, use mode "x+".
    </ans>

#file=python/psycopg2-copy_from-cannot-insert-field-with-delimiter-even-if-quoted.md
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

#file=postgresql/create-table-if-not-exists.md
    ---
    title: Create table if it does not exist in PostgreSQL
    ---

    <ans>
    ```sql
    CREATE TABLE IF NOT EXISTS table_name
    ```
    </ans>

#file=postgresql/create-table-if-not-exists.md
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

#file=postgresql/drop-database-connections.md
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

#file=python/iterate-dict-key-value-pairs.md
    ---
    title: Iterate dictionary key/value pairs in Python
    ---

    <ans>
    ```python
    for k, v in d.items():
        print(k, v)
    ```
    </ans>

#file=
    #ref=https://realpython.com/python-modulo-operator/#how-to-check-if-a-number-is-even-or-odd
    #ref=https://jekyllrb.com/docs/variables/
    #ref=https://github.com/daattali/beautiful-jekyll
    #ref=https://flaviocopes.com/postgres-how-to-list-tables-database/
    #ref=https://python-poetry.org/
