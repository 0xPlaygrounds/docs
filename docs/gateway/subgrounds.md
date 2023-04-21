# Querying using Subgrounds
Although it is entirely possible to use the Playgrounds Gateway by directly sending requests with a valid Playgrounds API key, the Gateway is most useful when used with Subgrounds. This allows you to leverage Subgrounds and its features to query the Graph's decentralized network with ease. Below is an example of how to use Subgrounds with the decentralized network.

```{thebe-button}
```

## 1. Initialize {class}`~subgrounds.Subgrounds` object
The first step is to initialize the {class}`~subgrounds.Subgrounds` object with a custom header value containing you Playgrounds API key.

```{note}
Replace `"PG_API_KEY"` with API key gathered from [earlier](/docs/gateway/key)!
```

```{code-block} python
:class: thebe

from subgrounds import Subgrounds

sg = Subgrounds(headers={"Playgrounds-Api-Key": "PG_API_KEY"})
```

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
