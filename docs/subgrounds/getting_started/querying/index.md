# Querying

Subgrounds provides 3 main ways to query data, which provide different data structures and typing:

:::{list-table}
:header-rows: 1

* - Function
  - Return Type
  - Description

* - {func}`~subgrounds.Subgrounds.query`
  - {py:class}`str` | {py:class}`int` | {py:class}`float` | {py:class}`bool` | {py:class}`list` | {py:class}`tuple` | {py:class}`None`
  - The shape of the queried data will determine the shape of the returned data (e.g. whether you query a single entity, list of entities)

* - {func}`~subgrounds.Subgrounds.query_json`
  - {py:class}`dict`
  - For subgraphs, this *can* include generated id keys for each generated sub-query.

* - {func}`~subgrounds.Subgrounds.query_df`
  - {class}`~pandas.DataFrame` or {class}`list`\[{class}`pandas.DataFrame`\]
  - Flattened based on the schema of the API from {func}`~subgrounds.Subgrounds.query_json`, mimicking an SQL `JOIN` operation. If flattening isn't possible, multiple {class}`Dataframes <pandas.DataFrame>` will be returned (like when querying a nested list).
:::

```{tip}
{func}`~subgrounds.Subgrounds.query_df` will likely be the best choice for most folks!
```

## Quick Example

The following code blocks present a comparison between all methods using the `aave-v2` market data:

{{ thebe_button }}

```{code-block} python
:class: thebe
:caption: Setup for the following examples of the query methods using the Aave V2 data from Ethereum
from subgrounds import Subgrounds

sg = Subgrounds()
aave_v2 = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")

aave_markets = aave_v2.Query.markets(
    first=3,
    orderBy=aave_v2.Market.totalValueLockedUSD,
    orderDirection="desc",
    where=[
        aave_v2.Market.createdBlockNumber > 14720000
    ]
)
```

:::::{tab-set}

::::{tab-item} query
```{code-block} python
:class: thebe
:caption: A list of names and a matching list TVL values gets returned

sg.query([
    aave_markets.name,
    aave_markets.totalValueLockedUSD,
])
```
::::

::::{tab-item} query_json
```{code-block} python
:class: thebe
:caption: A more complex JSON data structure gets returned

sg.query_json([
    aave_markets.name,
    aave_markets.totalValueLockedUSD,
])
```
::::

::::{tab-item} query_df
```{code-block} python
:class: thebe
:caption: ✨ A simple {class}`~pandas.DataFrame` gets returned

sg.query_df([
    aave_markets.name,
    aave_markets.totalValueLockedUSD,
])
```
::::

:::::

```{toctree}
:caption: Field Paths
:hidden:

grouping
```

:::{tip}
The Graph provides a default server timeout of 30s so we've chosen this as our default for subgrounds. However, if you are using a custom or self-hosted indexer, you might want to adjust this timeout value. You can do so via the `timeout` constructor param.

```python
sg = Subgrounds(timeout=60)
```
:::