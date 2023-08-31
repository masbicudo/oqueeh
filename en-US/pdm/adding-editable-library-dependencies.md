---
title: Adding editable library dependencies using PDM
generated: true
---

<div markdown="1" class="ans">
```bash
# A relative path to the directory
pdm add -e ./sub-package --dev
# A file URL to a local directory
pdm add -e file:///path/to/sub-package --dev
# A VCS URL
pdm add -e git+https://github.com/pallets/click.git@main#egg=click --dev
```
</div>

**Remarks:**
Editable installs are only allowed in the dev dependency group.

**Know more:**
- [Adding library dependencies using PDM](/en-US/pdm/adding-library-dependencies)
- [Adding development library dependencies using PDM](/en-US/pdm/adding-development-library-dependencies)
