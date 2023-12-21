# Contributing: Docs

## Setup

This project uses [poetry >= 1.2](https://python-poetry.org/docs/) to manage it's dependencies. Please checkout the official instructions to setup poetry on your system.

```bash
$ git clone https://github.com/0xPlaygrounds/docs && cd docs
$ poetry install --no-root
```

We also use a `poetry` plugin called `poethepoet` to aid in managing our frequently run tasks.

```bash
$ poetry self add 'poethepoet[poetry_plugin]'
```

Our docs are managed by [mudkip](https://github.com/vberlier/mudkip), a wrapper on the popular [sphinx](https://www.sphinx-doc.org/) project.


```bash
$ poe dev
```

This will launch a development web server on `localhost:5500` which loads the locally built docs. The process will also watch the `docs` folder for any changes and will trigger a rebuild which reloads your page with your changes implemented.


<details class="admonition hint dropdown toggle-hidden" style="padding: 0.75em">
<summary><b>Alternative to using <code>poe</code></b></summary>
<br>

If you wish not use `poe`, you'll have to run the following and checkout the commands listed in the `pyproject.toml` under `[tool.poe.tasks]`.

This will run `<my-command>` inside a virtual environment (`poetry shell` will explictly keep you inside one until you run `deactivate`)

```bash
$ poetry shell
$ mudkip develop
$ deactivate
# or
$ poetry run mudkip develop
```
</details>


### Generating API Docs

Our API documentation is generated from docstrings directly from our source code. To generate the files, run the following within the root of the project:

```bash
$ poe generate-api-docs
```

### Style

Our docs are primarily written in markdown, with some extra flavor added via the [MyST](https://myst-parser.readthedocs.io) plugin. This makes it easier to start writing content, while being able to sprinkle in fancier content!

Additionally, we also use the follow extensions:
  - Colon Fences
    - Makes using ":::" and "::::" instead of pure "\`\`\`" and "\`\`\`\`" which is nicer to use within `markdown` files.
    - We prefer using "::::" for grids and groupings while "\`\`\`" for simple cards and dropdowns.

  - Substitution
    - Allows the use of simple Jinja2 substitutions within YAML frontmatter.

  - [Sphinx Design](https://sphinx-design.readthedocs.io/)
    - This extension adds several useful cards, grids, icons, and dropdowns to make the documentation look nicer.
