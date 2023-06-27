# Subgrounds Integration with the Subgraph Proxy
While you can certainly use the Playgrounds proxy alone by submitting requests with a valid Playgrounds API key, pairing it with Subgrounds simplifies and streamlines the querying and data analysis from decentralized subgraphs. Here's an example demonstrating the integration:

```{thebe-button}
```

## 1. Add your Playgrounds API Key to your Subgrounds project

There are two main ways to validate your API key with subgrounds.

```{note}
Replace `"PG_API_KEY"` with API key gathered from [earlier](/docs/gateway/key)!
```

:::::{tab-set}

::::{tab-item} Constructor
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
