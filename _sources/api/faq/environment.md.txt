# Environment Vars

As listed in the docs page for [subgrounds](../subgrounds.md), environment variables are one of the easiest ways to access the Playgrounds API seemlessly throughout your projects.

## What are they?

An environment variable is a named value set by the user, often used for configuration. Usually, the contain secrets like api keys so that a program can access them in a standardized manner.

```{code-block} bash
:caption: Keys generally start with `$`, this is what ours look like.

$PLAYGROUNDS_API_KEY
```

## Inserting into your shell

In most shells, it's relatively straightforward to insert your environment variable.

```{code-block} bash
PLAYGROUNDS_API_KEY=pg-123456
python my_script.py
```

However, this won't *persist* if you restart your shell. For that, you'll need to add a value to your shell's profile or rc file. These files get ran when your shell launches, so they will always ensure your environment var is always loaded. You'll need to look up the correct file for your shell, here's a shortlist of some common ones:

- `bash`
  - `~/.profile`
  - `~/.bash_profile`
  - `~/.bashrc`
- `zsh` (Often on MacOS)
  - `~/.profile`
  - `~/.zshrc`

If you don't have this file, feel free to create a new one. Then, you can fill it with this contents or append this line to an already existing one!

```{code-block} bash
export PLAYGROUNDS_API_KEY=pg-123456
```

Once you set this in your file, you'll have to restart your shell for the changes to take effect.

```{hint}
There's quite a few options here! Don't fret, likely something like `.profile` will work. Each one has a slightly different purpose such as whether the file will run in an interactive or non-interactive shell.
```

## Benefits

Now, you are able to use the `Subgrounds` or `AsyncSubgrounds` object w/o needing to reference any api keys within your code. This will make your code more portable and easier to share with others!

```{code-block} python
:caption: You'll no longer need to include any explicit API key reference in your code!

from subgrounds import Subgrounds

deployment = "..."

with Subgrounds() as sg:
    sg.load_subgraph("https://api.playgrounds.network/v1/proxy/deployments/id/{deployment}")
    sg.query_df(...)
```

