# Querying

Subgrounds provides 3 main ways to query data, which provide different data structures and typing:

* {func}`~subgrounds.subgrounds.Subgrounds.query`
  * Results in raw data types such as a number, a string, etc.
  * *Note*: It is important to consider the shape of the queried data (e.g.: single entities, list of entities...) as the shape of the returned data will depend on it.

* {func}`~subgrounds.subgrounds.Subgrounds.query_json`
  * Results in a raw JSON object ({py:class}`dict`) containing the unprocessed response from the api.
  * For subgraphs, this *can* include generated id keys for each generated sub-query.

* {func}`~subgrounds.subgrounds.Subgrounds.query_df`
  * Results in a {class}`~pandas.DataFrame` or {class}`list`\[{class}`pandas.DataFrame`\].
  * This data is flattened based on the schema of the API from the above JSON data, mimicking the SQL `JOIN` operation
  * If flattening isn't possible, multiple {class}`Dataframes <pandas.DataFrame>` will be returned.

```{thebe-button}
```

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
