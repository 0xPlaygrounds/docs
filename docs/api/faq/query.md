# What is a Query?

In the Playgrounds API, queries are 1:1 to the number of requests made to the underlying decentralized API. Queries are **not** 1:1 with a singular `subgrounds`' snippet as a single `subgrounds` request could be getting hundreds of thousands of rows with a single line of code. Since `subgrounds` automatically handles pagination, it makes multiple GraphQL queries behind the scenes.

## Examples

Generally, whatever is placed in the `first` argument correlates to the number of expected pages.

{{ thebe-button }}

```{code-block} python
:class: thebe
:caption: Common setup for the examples (using the hosted service as an example)

from subgrounds import Subgrounds

sg = Subgrounds()
curve = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
```

The following example will result in a single query:

```{code-block} python
:class: thebe
:caption: Grabbing liquidity pool data

# default for `first` is 100
sg.query_df(
    curve.Query.liquidityPools
)
```

The following example will result in 10 queries:

```{code-block} python
:class: thebe
:caption: Grabbing liquidity pool data

sg.query_df(
    curve.Query.liquidityPools(first=9000)
)
```

```{code-block} python
:caption: This would still be 10 queries as both of these entities would get [merged](/subgrounds/getting_started/field_paths/merging).

sg.query_df(
    curve.Query.liquidityPools(first=9000),
    curve.Query.liquidityGauges(first=9000),
)
```

```{note}
Just because you put a very high number for `first` (such as `1_000_000`), it doesn't mean it'll actually result in that many queries since there might be less than that many rows of data.
```

## Nested Pagination

Since nested fields can also have their own set of arguments, defining `first` in them will result in nested pagination. This can **greatly** increase the number of queries made as each nested field will be multiplicative

The number of queries directly is related to the argument you put in `first`. If you only define `first` for the most top-level entities, than pagination is summed across all those fields. If you start defining `first` for sub-fields, then pagination can get multiplicative as for each top-level page, the whole series of sub-pages would be queried.

```{code-block} python
:caption: This would still be 100 (10・10) queries due to nested pagination and return 81 million (9000・9000) rows.

pools = curve.Query.liquidityPools(first=9000)

sg.query_df(
    pools.dailySnapshots(first=9000)
)
```
