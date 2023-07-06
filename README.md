# <a style="font-family: ubuntu; color: crimson; font-weight: bold; font-style: italic" href="https://oqueeh.net">oqueeh<span style="font-size:0.8em">.net</span></a>

Just answers to questions, big and easy
to read. No nonsense, no bullshit.

## Motivation

When I look for answers on the internet,
most of the time, what I want comes with
tons of introductory, explanatory,
and a lot of other filler text.

All I wanted was a quick reference,
with these characteristics:

1. First, and foremost, an answer
2. Subsequent information more than prior
3. Most common alternatives
4. Little to no explanation
5. Only relevant references
6. No scroll bars

This is basically describing a cheat-sheet,
that follows a common workflow.
That's what this repository is all about.

### 1. First, and foremost, an answer

Of course the question title comes
before the answer, but that is it.
Everything that is not the main answer
to the problem must go after that.

### 2. Subsequent information more than prior

Most texts on the internet have introductions
and explanations before an answer.
What I want is the opposite: an answer,
and what are the probable next steps.

In no way prerequisites are to be excluded,
but I assume prior knowledge from the reader.

Subsequent and prior knowledge can be
presented directly, or as links.

### 3. Most common alternatives

Incomplete questions have multiple answers.
In this case, the most mainstream answer
comes first.

Other answers are added after that,
directly or as links.

### 4. Little to no explanation

I assume the reader to have prior knowledge,
at least one level below from what is being
answered.

That's why little explanation is needed,
sometimes the answer is self-explanatory
for someone one level below.

Sometimes matters are a bit hideous and
the reader just needs an extra bit of
info to clear everything up.

### 5. Only relevant references

I really don't want to waste space, and
references are the kind of thing that is
used as a last resort.

If references are to be included, they'd
better be some great learning material,
or the source documentation for completeness.

### 6. No scroll bars

I want everything of the greatest relevance
for the matter to fit in a screen.
It's all about focus and priority.

If more than one screen is needed, then
the topic should be split in two or more
related topics, with links to one another.

## Building web-site locally

To build locally, run the following script in order.
These scripts work on Windows only, since I didn't
have time to develop this under Linux.

Also, after running these, the pages must be built too.

If you did run these commands already,
there is no problem in running them again.

Scripts:

```bash
site-tools-install.cmd
```

```bash
site-bundle-init.cmd
```

```bash
site-bundle-update.cmd
```

```bash
site-serve.cmd
```

```bash
oqh build -u
```

## Debugging Python tools

Download and install tool dependencies:

1. Pyenv (on Linux) or Pyenv-Win (on Windows)
2. Python 3.10 - e.g. `pyenv install 3.10.6`

To install libraries and create virtual environment,
run:

```bash
./tools.project.init.sh
```

Inside of VS Code make sure to select the Python version
installed into `.venv` subdirectory. Then it will be possible
to hit F5 to debug the currently open file.

## References

- [GitHub Pages Ruby Gem](https://github.com/github/pages-gem)

- [Installing Ruby](https://www.ruby-lang.org/en/documentation/installation/)

- [Getting Started - Bundler](https://bundler.io/#getting-started)

- [Testing your GitHub Pages site locally with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
