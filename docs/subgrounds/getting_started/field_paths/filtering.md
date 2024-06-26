# Filtering

Filtering subgraphs in `subgrounds` is done via the `where` argument in {class}`~subgrounds.FieldPath`. A subgraph's GraphQL provides several options to filter based on nearly any field path.

{{ thebe_button }}

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
In some of the following examples, multiple conditions are stacked on top of each other. This would **not** result in any data being returned since the multiple conditions would likely conflict with each other.
```

## Matching Values

Using the `==` and `=!` operators in Python, matching exact or negated values on field paths is pretty straight forward:

:::::{tab-set}
::::{tab-item} Relative Form
:sync: relative

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where=[
            pool.isSingleSided == False,
            # or
            pool.isSingleSided != True,
        ]
    )
)
```
::::
::::{tab-item} Raw Form
:sync: raw

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where={
            "isSingleSided": False,
            # or
            "isSingleSided_not": False,
        }
    )
)
```
::::
:::::

### Null Values

For null values, you can swap values like `True` and `False` with `None`.

:::::{tab-set}
::::{tab-item} Relative Form
:sync: relative

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where=[
            pool.name == None,
            # or
            pool.name != None,
        ]
    )
)
```
::::
::::{tab-item} Raw Form
:sync: raw

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where={
            "name": None,
            # or
            "name_not": None,
        }
    )
)
```
::::
:::::

```{warning}
You might be tempted to write `pool.name is None` which is recommended by linters for checking `None` values. This is incorrect, as it'll directly return `True` or `False` as there is no special generative code for `is`. You can add `# noqa: E711` at the end of these lines to inform your linter to ignore this specific rule as it doesn't apply to this specific operation.
```

## Comparisons

Filtering can also be based on standard comparison logic on any field path, such as "greater than", "less than", etc — generally more useful for numeric fields.

:::::{tab-set}
::::{tab-item} Relative Form
:sync: relative

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where=[
            pool.cumulativeVolumeUSD > 150000000,
            pool.cumulativeVolumeUSD >= 150000000,
            pool.cumulativeVolumeUSD < 150000000,
            pool.cumulativeVolumeUSD <= 150000000,
        ]
    )
)
```
::::
::::{tab-item} Raw Form
:sync: raw

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where={
            "cumulativeVolumeUSD_gt": 150000000,
            "cumulativeVolumeUSD_gte": 150000000,
            "cumulativeVolumeUSD_lt": 150000000,
            "cumulativeVolumeUSD_lte": 150000000,
        }
    )
)
```
::::
:::::

## Nested Filtering

Entities can have any layer of nestable objects which thereby are **also** filterable in the `where` clause:

:::::{tab-set}
::::{tab-item} Relative Form
:sync: relative

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where=[
            pool.hourlySnapshots.hourlyVolumeUSD > 1000
        ]
    )
)
```
::::
::::{tab-item} Raw Form
:sync: raw

```{code-block} python
:class: thebe
sg.query_df(
    curve.Query.liquidityPools(
        where={
            "hourlySnapshots_": {"hourlyVolumeUSD_gt": 14720000}
        }
    )
)
```

```{note}
The trailing `_` prefix is needed in the GraphQL form since without it, GraphQL assumes you are matching the exact value!
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
