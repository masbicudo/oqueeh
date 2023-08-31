# To Do

[ ] `oqh list --without-generator`
    Used to list all files that are in the file structure,
    but don't have any generator in the _split.md file.
[ ] `oqh serve`
    Used to serve oqueeh web site locally.
    It should open the site in the browser.
[ ] `oqh init` should initialize all needed tools.
    Installation of global tools require user acceptance.
    `oqh init --yes` can be used to avoid asking for permission.
[ ] `oqh update`
    Used to update oqh dependencies and oqh script itself.
    Updating global tools requires user acceptance.
    `oqh update --yes` can be used to avoid asking for permission.
[ ] running `oqh` should contain instructions
    about how to do first setup, namely running `oqh init`.

[ ] add css `font-size: calc(0.06vw * var(--cols));`
    [ ] add `--cols` variable to all code blocks
[ ] post **Set user name and email in Git** has UI bugs
[x] fix typo *width greater then height* replace "then" with "than"

[ ] https://itectec.com/webapp/google-drive-how-to-one-link-directly-to-a-specific-page-of-a-pdf-in-google-drive/#

## UI Tests

Test list:
[ ] Create list of tests from the folder structure
[ ] Hash each file to be tested

Test interface:
[x] add button to refresh iframe
    [ ] auto-refresh on file change
[x] add button to accept output of a page
[x] add button to reject output of a page
[ ] only show tests for changed content
    [ ] invalidate all tests if global CSS file is changed
