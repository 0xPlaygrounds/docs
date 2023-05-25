# Querying using Subgrounds
Although it is entirely possible to use the Playgrounds Gateway by directly sending requests with a valid Playgrounds API key, the Gateway is most useful when used with Subgrounds. This allows you to leverage Subgrounds and its features to query the Graph's decentralized network with ease. Below is an example of how to use Subgrounds with the decentralized network.

```{thebe-button}
```

## 1. Add your Playgrounds API Key to your Subgrounds project

There are two main ways to validate your API key with subgrounds.

```{note}
Replace `"PG_API_KEY"` with API key gathered from [earlier](/docs/gateway/key)!
```

:::::{tab-set}

::::{tab-item} Alternative Constructor
```{code-block} python
:class: thebe
:caption: Initialize {class}`~subgrounds.Subgrounds` object with a playgrounds api key

from subgrounds import Subgrounds

sg = Subgrounds.from_pg_key("PG_API_KEY")
```
::::

::::{tab-item} Environment Var
```{code-block} bash
:caption: The environment variable can be set any way you like!

PLAYGROUNDS_API_KEY="PG_API_KEY"
```

```{code-block} python
:class: thebe
:caption: This method is great since you don\'t need to change your code at all!
from subgrounds import Subgrounds

sg = Subgrounds()
```
```{warning}
This method will produce a {class}`RuntimeWarning` if `$PLAYGROUNDS_API_KEY` does *not* look like valid.

It will also be overriden if the headers are set manually, or via {method}`Subgrounds.from_pg_key`
```
::::

::::{tab-item} Under the Hood
```{code-block} python
:class: thebe
:caption: Internally, both method sets the request headers
from subgrounds import Subgrounds

sg = Subgrounds(headers={"Playgrounds-Api-Key": "PG_API_KEY"})
```
::::

:::::

## 2. Query a decentralized network subgraph
Once the {class}`~subgrounds.Subgrounds` object has been initialized with the custom header containing your API key, you can query a decentralized network subgraph through our proxy endpoint just like you would query any other subgraph. 

```{code-block} python
:class: thebe

subgraph = sg.load_subgraph(
    "https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7"
)

sg.query_df([
    subgraph.Query.tokens.id,
    subgraph.Query.tokens.symbol,
])
```
