---
title: Creating figures with multiple images in LaTeX
generated: true
---

<div markdown="1" class="ans">
```
\begin{figure}
    \begin{subfigure}[b]{0.5\textwidth}
        \includegraphics[scale=0.5]{image.pdf}
    \end{subfigure}
    % ... other subfigures
\end{figure}
```
</div>

**Related:**
- ref=en-US/latex/create-figure-spanning-multiple-document-columns.md

**References:**
- [How to Write a Thesis in LaTeX (Part 3): Figures, Subfigures and Tables - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/How_to_Write_a_Thesis_in_LaTeX_(Part_3)%3A_Figures%2C_Subfigures_and_Tables#Subfigures)
