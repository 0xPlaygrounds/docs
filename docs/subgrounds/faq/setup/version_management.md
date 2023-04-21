# Python Versioning

While the `python -m venv` module is quite handy, it has one fatal flaw: it requires `python` itself to be stable. This can makes upgrading python a hastle as it resets all of your project environment setups forcing you to recreate them with a new `python` (albeit much easier with a `requirements.txt`). This is a *very* common issue when using tools and apps through `python` or installed via `pip`. 

Fortuntely, a slew of third-party tooling has made this much easier to self-manage

```{note}
At time of writing, `3.11.3` is the latest Python version.
```

## [pyenv](https://github.com/pyenv/pyenv)

Pyenv is a tool used to manage different versions of Python on a single operating system (follow this [guide](https://github.com/pyenv/pyenv#installation) for installation instructions). It uses shell shims to reroute `python` to different versions based on various conditions (local `.python_version` files, etc). If you are having problems getting Python 3.10+ to work, we recommend you try `pyenv` to set it up.

```{warning}
`pyenv` has **limited** windows support (only a separately managed windows forks exists)
```

Once pyenv is installed, navigate to your project's directory and run the following commands:

```bash
:caption: Install then set the local python
pyenv install 3.11.3
pyenv local 3.11.3
```

The first command downloads Python version `3.11.3` on your operating system. The second command create a `.python-version` file in your current directory which will be used by pyenv so set the active Python version when you are working from that directory.

To test that the correct Python version has been selected, you can run the following command:

```bash
pyenv version
```

Which should output something like:

```bash
3.11.3 (set by /my/project/path/.python-version)
```

<!-- ## [rtx](https://github.com/jdxcode/rtx)

```{warning}
This is some bleeding edge tech, hot off the press! The maintainers haven't used this tool yet.
```

`rtx` is runtime manager for multiple runtimes (built after the predecessor, [asdf](https://asdf-vm.com/)). Similar to `pyenv`, it can help manage multiple python versions. This tool might be better for you if you:

- Need a solution for other runtimes (`ruby`, `nodejs`)
- Find `pyenv`  -->


## [pipx](https://github.com/pypa/pipx)

`pipx` is a seemless way to install python-like apps (from CLI to full-fledged UIs) with their own managed python environment. This makes them easy to manage (and fix) and works seemlessly with `pyenv`.

Follow the instructions in the repo to get started.

```bash
:caption: Example of installing `black` as an app

pipx install black
```

Here, `black` will be available in your terminal globally. The dependencies of `black` will stay independent to other projects and your global python due to the environment that `pipx` manages for it.

```{note}
We **highly** recommend using `pipx` to manage python cli tools as it makes it easier to manage. It can be a better solution than using a native package manager as you can stay more up-to-date to the latest versions of the software.
```
