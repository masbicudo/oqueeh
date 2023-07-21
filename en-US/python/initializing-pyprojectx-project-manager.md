---
title: Initializing a PyProjectX Python project
generated: true
---

<div markdown="1" class="ans">
Download PyProjectX tool to project directory:
- Linux: `curl -LO https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip && unzip wrappers.zip && rm -f wrappers.zip`
- Windows: `powershell
Invoke-WebRequest https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip -OutFile wrappers.zip; Expand-Archive -Path wrappers.zip -DestinationPath .; Remove-Item -Path wrappers.zip
`
Then initialize, using one of the following:
- `./pw --init pdm`
- `./pw --init poetry`
</div>
