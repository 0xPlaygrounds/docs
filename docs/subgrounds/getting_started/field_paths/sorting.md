# Sorting

Data can also be queried based on specific sort of a field path. This can be helpful if you want get data such as the top performing pools based on revenue, etc.

{{ thebe_button }}

```{code-block} python
:class: thebe
:caption: We will be using curve as the base subgraph for the following examples

from subgrounds import Subgrounds

sg = Subgrounds()

curve = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")

pool = curve.LiquidtyPool  # shorthand for examples
snapshot = curve.DailySnapshot
```

## The Basics

To sort, we define the `orderBy` argument on a field path:

```{code-block} python
:class: thebe
:caption: Sorting by performing pools by total cumulative revenue

sg.query_df(
    curve.Query.liquidityPool(orderBy=pool.cumulativeTotalRevenueUSD)
)
```

By default, the sorting method is ascending. We can change it to descending (providing us with the highest performing pools) via `orderDirection`:

```{code-block} python
:class: thebe
:caption: Sorting by the top performing pools by total cumulative revenue

sg.query_df(
    curve.Query.liquidityPool(orderBy=pool.cumulativeTotalRevenueUSD, orderDirection="desc")
)
```

## Layered Sorting

Since nested fields can also have arguments, we can layer multiple sortings on top of each other:

```{code-block} python
:class: thebe
:caption: Sorting the top 4 liquidity pools and the top 3 trading days

top_pools = curve.Query.liquidityPool(
    first=4,
    orderBy=pool.cumulativeTotalRevenueUSD,
    orderDirection="desc",
)

sg.query_df(
    top_pools.dailySnapshots(
        first=3,
        orderBy=snapshot.dailyVolumeUSD,
        orderDirection="desc",
    )
)
```

```{warning}
Adding more complexity to your query will lead to longer query times as the indexer has to perform multiple internal database queries to construct the data as you request. If you hit the natural timeout of 30s, you can try running the query again as the indexer will continue to process your query in the background, caching the value for future queries.
```

## Sorting by Nested Fields

We aren't just limited by sorting only on the top-level fields — we can sort *by* nested fields. This is different than layering since we are ordering the main list of rows based upon a nested value (usually within an object).

```{danger}
Nested filtering usually only works at a maximum depth of **2** and may not work across older subgraphs.
```

```{code-block} python
:class: thebe
:caption: "Sorting liquidity pools based upon the output token's last traded price."

sg.query_df(
    curve.Query.liquidityPool(
        orderBy=pool.outputToken.lastPriceUSD,
        orderDirection="desc",
    )
)
```
