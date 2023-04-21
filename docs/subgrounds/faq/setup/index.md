# Setup

Python installations vary across various system architectures, OS's, and guides. Often times, the path of a python install can be quite the confusing journey causing multiple pythons installations to pollute your workspace.
<figure style="text-align: center;">
    <img src="/_static/assets/python-env-meme.png" width=50%/>
    <figcaption><i>The pain of managing a python install (<a href=https://xkcd.com/1987>Source</a>)</i></figcaption>
</figure>

This guide will serve to help mitigate this risk by *taming* your python installation 🎉

## Environments

By default, `pip` will install packages to your global environment. While this makes it easy to get started with using `subgrounds`, it can make it more difficult to maintain the proper versions for a specific project. 

Environments are a key tool in fixing this problem, making it much eazier to organize project dependencies. Environments can help direct `pip` to install packages **locally**, specifically to a project. The easiest way to begin using environments is with the included `venv` module that is packaged with every python install!

```{code-block} bash
:caption: Creating a local environment and activating it

python -m venv .venv
source .venv/bin/activate
```

The `.venv` folder contains various "fake" executables that *link* to the real executables behind the scene. A special `activate` script is created which hijacks your shell to trick it that the python inside the `.venv` folder, is the "global" python. It ensures that packages used within this "hijacked" shell are only accessed *within* the `.venv` folder, and no where else.

This allows you to install project dependencies **independently** from your global python install, **without** requiring you to maintain multiple python installations (since it borrows the python from your global setup).

Once activated, `pip` install all of your favorite packages

```{code-block} bash
:caption: Installing `subgrounds`, the best package!

pip install -U "subgrounds[dash]"
```

Now that you have your packages, you can "freeze" them into a file. This essentially captures every version of the dependency (and their dependencies, etc) into a file. 

```{code-block} bash
:caption: Freezing dependencies into a file

pip freeze > requirements.txt
```

In the future, if you decide to update your python and reset your project environments, you can easily restore your project dependencies.

```{code-block} bash
:caption: Installing dependencies into a file

pip install -r requirements.txt
```

```{note}
This is a basic form of **version pinning**, which is a key technique into ensuring a projects stability. Since the versions of every package required is known, you can replicate the project's setup in the future (and across other machines, such as co-workers, etc).
```

You can *always* update the version pins via an additional `pip freeze > requirement.txt` if you update the dependencies in the future.

---

```{warning}
The following pages will recommend the use of **third-party** tooling. Although, the maintainers of this project use and trust many of these tools, we still request users take pre-cautions when using them since they might not work across all systems and architectures as python itself.
```

```{toctree}
:caption: Setup
:hidden:

version_management
```
