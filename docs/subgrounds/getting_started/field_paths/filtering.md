# Filtering

Filtering subgraphs in `subgrounds` is done via the `where` argument in {class}`~subgrounds.FieldPath`. Subgraph's GraphQL provides several options to filter based on nearly any field path.

The following list will contain examples of all of the ways to filter field paths.

{{ thebe-button }}

```{code-block} python
:class: thebe
:caption: We will be using curve as the base subgraph for the following examples

from subgrounds import Subgrounds

sg = Subgrounds()

curve = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")

pool = curve.LiquidityPool  # shorthand for examples
```

```{note}
In some of the following examples, I stack multiple conditions on top of each other. This would not result in any data being returned since the multiple conditions would likely conflict with each other.
```

## Matching Values

Matching exact values on field paths. Can also match negated values.

:::::{tab-set}
::::{tab-item} Relative Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    where=[
        isSingleSided == False,
        # or
        isSingleSided != True,
    ]
)
```
::::
::::{tab-item} Raw Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    where={
        "isSingleSided": False,
        # or
        "isSingleSided_not": False,
    }
)
```
::::
:::::

## Comparisons

You can filter based on your basic filters of greater than, lesser than, etc. on any field path (usually numerical). This is where Subgrounds relative form becomes more obvious than pure GraphQL.

:::::{tab-set}
::::{tab-item} Relative Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    where=[
        pool.cumulativeVolumeUSD > 150000000,
        pool.cumulativeVolumeUSD >= 150000000,
        pool.cumulativeVolumeUSD < 150000000,
        pool.cumulativeVolumeUSD <= 150000000,
    ]
)
```
::::
::::{tab-item} Raw Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    where={
        "cumulativeVolumeUSD_gt": 150000000,
        "cumulativeVolumeUSD_gte": 150000000,
        "cumulativeVolumeUSD_lt": 150000000,
        "cumulativeVolumeUSD_lte": 150000000,
    }
)
```
::::
:::::

## Nested Filtering
Since entities are nested with field paths, we can also filter based on nested values.

:::::{tab-set}
::::{tab-item} Relative Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    where=[
        pool.hourlySnapshots.hourlyVolumeUSD > 1000
    ]
)
```
::::
::::{tab-item} Raw Form
```{code-block} python
:class: thebe
curve_pools = curve.Query.liquidityPools(
    where={
        "hourlySnapshots_": {"hourlyVolumeUSD_gt": 14720000}
    }
)
```
::::
:::::


<!-- 
-- REMAINING CONDITIONS TO DOCUMENT --

_in
_not_in
_contains
_contains_nocase
_not_contains
_not_contains_nocase
_starts_with
_starts_with_nocase
_ends_with
_ends_with_nocase
_not_starts_with
_not_starts_with_nocase
_not_ends_with
_not_ends_with_nocase
-->
