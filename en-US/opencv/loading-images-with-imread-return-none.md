---
title: Loading images with `imread` return None in OpenCV
generated: true
---

<div markdown="1" class="ans">
OpenCV `imread` fails silently in multiple situations:
- File doesn't exist
- File name or path contains non-ASCII characters
</div>
