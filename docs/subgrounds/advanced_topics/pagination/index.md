# Pagination

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.0.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

{{ thebe_button }}

By default, Subgrounds handles GraphQL query pagination automatically. That is, if a query selects more than 1000 entities using the `first` argument (1000 being The Graph's limit to the `first` argument), then Subgrounds will automatically split the query into multiple queries that each query at most 1000 entities.

Pagination is performed by Subgrounds with the use of a pagination strategy: a class that implements the {class}`~subgrounds.pagination.PaginationStrategy` protocol. Subgrounds provides two pagination strategies out of the box, however, users wishing to implement their own strategy should create a class that implements the aforementioned protocol (see below).

If at some point during the pagination process, an unhandled exception occurs, Subgrounds will raise a {class}`~subgrounds.pagination.PaginationError` exception containing the initial exception message as well as the {class}`~subgrounds.pagination.PaginationStrategy` object in the state it was in when the error occured, which, in the case of iterative querying (e.g.: when using {meth}`~subgrounds.Subgrounds.query_df_iter`), could be useful to recover and start pagination from a later stage.

## Available Strategies
Subgrounds provides two pagination strategies out of the box:
1. {class}`~subgrounds.pagination.LegacyStrategy`: A pagination strategy that implements the pagination algorithm that was used by default prior to this update. This pagination strategy supports pagination on nested fields, but is quite slow. Below is an example of a query for which you should use this strategy:

```graphql
query {
  liquidityPools(first: 10) {
    swaps(first: 5000) {
      id
    }
  }
}
```

2. {class}`~subgrounds.pagination.ShallowStrategy`: A new pagination strategy that is faster than the {class}`~subgrounds.pagination.LegacyStrategy`, but does not paginate on nested list fields. In other words, this strategy is best when nested list fields select fewer than 1000 entities. Below is an example of a query for which you should use this strategy:

```graphql
query {
  liquidityPools(first: 5000) {
    swaps(first: 10) {
      id
    }
  }
}
```

To use either pagination strategy, set the `pagination_strategy` argument of toplevel querying functions:
```{code-block} python
:class: thebe
from subgrounds import Subgrounds
from subgrounds.pagination import ShallowStrategy

sg = Subgrounds()
subgraph = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/compound-v2-ethereum")

mkt_daily_snapshots = subgraph.Query.marketDailySnapshots(
    orderBy="timestamp",
    orderDirection="desc",
    first=50,
)

field_paths = [
    mkt_daily_snapshots.timestamp,
    mkt_daily_snapshots.market.inputToken.symbol,
    mkt_daily_snapshots.rates.rate,
    mkt_daily_snapshots.rates.side,
]

sg.query_df(field_paths, pagination_strategy=ShallowStrategy) 
```

Note that pagination can be explicitly disabled by setting {class}`~subgrounds.pagination.LegacyStrategy` to `None`, in which case the query will be executed as-is:
```{code-block} python
:class: thebe
sg.query_df(field_paths, pagination_strategy=None) 
```

```{toctree}
:caption: Pagination
:hidden:

custom
```
