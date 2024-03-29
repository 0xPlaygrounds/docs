# Arguments

Some {class}`FieldPaths <subgrounds.FieldPath>` can be parameterized with certain arguments such as specific token ids, sorting by certain fields, etc. These arguments can be configured by "calling" said function (e.g. `aave_v2.Query.market(first=10)`).

{{ thebe_button }}

```{code-block} python
:class: thebe
:caption: Loading a curve subgraph

from subgrounds import Subgrounds
sg = Subgrounds()

curve = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
```

:::::{tab-set}

::::{tab-item} Python
```{code-block} python
:class: thebe
:caption: Analyzing curve pool data via the `curve.Query.pools` {class}`~subgrounds.FieldPath`

# `curve.Query.pools` is a field path
#  we "call it to add arguments!
curve_pools = curve.Query.liquidityPools(
    first=10,
    orderBy=curve.LiquidityPool.totalValueLockedUSD,
    orderDirection="desc",
    where=[
        curve.LiquidityPool.createdBlockNumber > 14720000
    ]
)

# We can then query based on the routing of these objects
sg.query_df([
    curve_pools.outputToken.name,
    curve_pools.totalValueLockedUSD,
])
```
::::

::::{tab-item} GraphQL
```{code-block} graphql
:caption: Analyzing curve pool data via the `curve.Query.pools` {class}`~subgrounds.FieldPath`

query {
  liquidityPools(
    first: 10
    orderBy: totalValueLockedUSD
    orderDirection: desc
    where: {createdBlockNumber_gt: 14720000}
  ) {
    outputToken{
      name
    }
    totalValueLockedUSD
  }
}
```
::::

:::::

```{note}
Notice that the values for the `orderBy` and `where` arguments are {class}`~subgrounds.FieldPath` themselves. This allows users to construct complex queries in pure Python by using the {class}`~subgrounds.Subgraph` object returned when loading an API.

The {class}`FieldPaths <subgrounds.FieldPath>` *here* are used as in their relative form, i.e.: they do not start from the root {class}`~subgrounds.subgrounds.query.Query` entity, but rather start from an entity type (in this case the `Pool` entity). 
```

```{warning}
It is important to make sure that the relative {class}`~subgrounds.FieldPath` used as values for the `orderBy` and `where` arguments match the entity type of the field on which the arguments are applied (in our example, the `pools` field is of type `Pool`). If this is not respected, a type error exception will be thrown. 
```

Argument values can *also* be supplied in their "raw" form, without the use of relative {class}`FieldPaths <subgrounds.FieldPath>`:

:::::{tab-set}

::::{tab-item} Raw Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    first=10,
    orderBy="totalValueLockedUSD",
    orderDirection="desc",
    where={
        "createdBlockNumber_gt": 14720000
    }
)
```
::::

::::{tab-item} Relative Form
```{code-block} python
:class: thebe

curve_pools = curve.Query.liquidityPools(
    first=10,
    orderBy=curve.LiquidityPool.totalValueLockedUSD,
    orderDirection="desc",
    where=[
        curve.LiquidityPool.createdBlockNumber > 14720000
    ]
)
```
::::

:::::

```{warning}
When using raw form instead of relative form, you lose out on any type validation. This means, errors will only surface when using `query` rather than surfacing when building the {class}`FieldPaths <subgrounds.FieldPath>`.

We **highly** recommend sticking with relative form, even if it seems more verbose!
```
