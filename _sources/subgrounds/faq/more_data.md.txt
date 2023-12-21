# Getting More Data

{{ thebe_button }}

By default, subgraphs will emit only 100 rows for a given entity. In order to surface more data from an entity, you must leverage [field arguments](/subgrounds/getting_started/field_paths/arguments), specifically the `first` argument. This specifies how many entities you wish to retrieve from that specific entity.

```{code-block} python
:class: thebe
:caption: Gathering data from the curve finance subgraph

from subgrounds import Subgrounds

with Subgrounds() as sg:
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")

    sg.query_df(
        curve.Query.financialsDailySnapshots(first=2500)
    )
```

```{note}
It is possible to query more than a 100 rows worth of data **without** specifying a `first` argument by using nested fields. Essentially, you would be querying multiple rows for each row as `subgrounds` would paginated the nested field and then auto-flatten said field.
```

## Pagination

Subgraphs and GraphQL usually restrict you to a maximum `first` argument of `1000`. In `subgrounds`, you can specify as large as a number as you want as `subgrounds` will automatically create multiple, **paginated**, requests to retrieve more data. This means you'll be able to access all the data from an entity by just setting the `first` argument to a high-enough number!

---

::::{grid} 1 2 2 2
:gutter: 3

```{grid-item-card}
:link: ../getting_started/field_paths/arguments
:link-type: doc

<h3 class='gradient-text card-heading'>
Field Arguments
</h3>

Customizing other field path arguments
```

```{grid-item-card}
:link: ../advanced_topics/pagination/index
:link-type: doc

<h3 class='gradient-text card-heading'>
Pagination
</h3>

Learn more about how `subgrounds` paginates!
```
::::
