# Merging

When passing a list of {class}`FieldPaths <subgrounds.FieldPath>` to any {func}`~subgrounds.Subgrounds.query` function, subgrounds will merge them into a single query.

```{warning}
This is **only** true if the {class}`FieldPaths <subgrounds.FieldPath>` originate from the **same subgraph**.
```

```{thebe-button}
```

:::::{tab-set}

::::{tab-item} Python
```{code-block} python
:class: thebe
:caption: In this query, we are taking the top 4 curve pools by **cumulative volume** and analyzes the top 3 days by **daily total revenue**

from subgrounds import Subgrounds
sg = Subgrounds()

curve = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")

# Partial FieldPath selecting the top 4 most traded pools on Curve
most_traded_pools = curve.Query.liquidityPools(
    orderBy=curve.LiquidityPool.cumulativeVolumeUSD,
    orderDirection="desc",
    first=4,
)

# Partial FieldPath selecting the top 2 pools by daily total revenue of
#  the top 4 most traded tokens.
# Mote that reuse of `most_traded_pools` in the partial FieldPath
most_traded_snapshots = most_traded_pools.dailySnapshots(
    orderBy=curve.LiquidityPoolDailySnapshot.dailyTotalRevenue,
    orderDirection="desc",
    first=3,
) 

# Querying:
#  - the name of the top 4 most traded pools, their 2 most liquid 
# pools' token symbols and their 2 most liquid pool's TVL in USD
sg.query_df([
    most_traded_pools.name,
    most_traded_snapshots.dailyVolumeUSD,
    most_traded_snapshots.dailyTotalRevenueUSD,
])
```
::::

::::{tab-item} GraphQL
```graphql
query {
  liquidityPools(first: 4, orderBy: cumulativeVolumeUSD, orderDirection: desc) {
    name

    dailySnapshots(first: 3, orderBy: dailyTotalRevenueUSD, orderDirection: desc) {
      dailyVolumeUSD
      dailyTotalRevenueUSD
    }
  }
}
```
::::

:::::

```{note}
This becomes very helpful when chaining partial {class}`FieldPaths <subgrounds.FieldPath>` together since you can leverage normal python constructs to help organize the data as you want to access and {func}`~subgrounds.Subgrounds.query` will handle the rest!
```