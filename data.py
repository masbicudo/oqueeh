category_names = {
    "api": "API",
    "c-sharp": "C#",
    "cmd": "Windows Command Prompt (CMD)",
    "css": "CSS",
    "cudf": "cuDF",
    "cupy": "cuPy",
    "dot-net": ".NET",
    "en-US": "All topics",
    "firefox": "FireFox",
    "gallery-dl": "gallery-dl",
    "github": "GitHub",
    "github-pages": "GitHub Pages",
    "html": "HTML",
    "javascript": "JavaScript",
    "latex": "LaTeX",
    "mathjax": "MathJax",
    "matplotlib": "Matplotlib",
    "nodejs": "Node.js",
    "nssm": "NSSM",
    "numpy": "NumPy",
    "opencv": "OpenCV",
    "pdm": "PDM",
    "postgresql": "PostgreSQL",
    "powershell": "PowerShell",
    "pt-BR": "Todos os tópicos",
    "pyenv-win": "PyEnv-Win",
    "scipy": "SciPy",
    "streamlit": "Streamlit",
    "syncthing": "Syncthing",
    "texlive": "TeX Live",
    "vscode": "VS Code",
    "windows-cmd": "Windows Command Prompt (CMD)",
}

# Equivalence classes of words
# ----------------------------
#   This is used to give warnings about
# multiple words with same meaning being
# used in the text of documents.
#   It is useful to maintain consistency
# among the thousands of documents that
# are present in this repository.
#   This will also be used by the automated
# fix tool: `oqh fix --word-consistency`,
# and the assisted mode `oqh fix -wi`,
# `wi` being short form for `--word-consistency`
# and `--interactive`.
equiv_classes = {
    r"\b(powershell|power-shell|posh)\b": ["PowerShell"],
    r"\b(batch|bat)\b": ["Batch"],
    r"\bWindows (Command)\b": ["CMD"],
}
