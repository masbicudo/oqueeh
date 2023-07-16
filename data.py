category_names = {
    "api": "API",
    "c-sharp": "C#",
    "css": "CSS",
    #"batch": "Batch",
    "firefox": "FireFox",
    "github": "GitHub",
    "html": "HTML",
    "javascript": "JavaScript",
    "nodejs": "Node.js",
    "pdm": "PDM",
    "postgresql": "PostgreSQL",
    "powershell": "PowerShell",
    #"windows": "Windows",
    "pt-BR": "Todos os tópicos",
    "en-US": "All topics",
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
