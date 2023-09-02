---
title: Display help message when no arguments are provided using Python argparse
generated: true
---

<div markdown="1" class="ans">
```
if len(sys.argv) == 1:
    parser.print_usage(sys.stderr)
    sys.exit(1)
```
</div>
