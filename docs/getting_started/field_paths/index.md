# Field Paths

{class}`~subgrounds.FieldPath`s are the main building blocks used to construct Subgrounds queries. A {class}`~subgrounds.FieldPath` represents a selection path through a GraphQL schema starting from the root {class}`~subgrounds.subgrounds.query.Query` entity (see [The Query and Mutation types](https://graphql.org/learn/schema/#the-query-and-mutation-types)) all the way down to a scalar leaf.

{class}`~subgrounds.FieldPath` are created by simply selecting attributes starting from the subgraph object returned by the {class}`~subgrounds.Subgrounds.load_subgraph` or {class}`~subgrounds.Subgrounds.load_api` methods:

```{thebe-button}
```

```{code-block} python
:class: thebe
:caption: Loading a curve subgraph

from subgrounds.subgrounds import Subgrounds
sg = Subgrounds()

curve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')
```

:::::{tab-set}

::::{tab-item} Python
```{code-block} python
:class: thebe
:caption: Analyzing curve pool data via the `curve.Query.pools` {class}`~subgrounds.FieldPath`

# `curve.Query.pools` is a field path
curve_pools = curve.Query.liquidityPools

# We can then query based on the routing of these objects
sg.query_df([
    curve_pools.inputTokens.name,
    curve_pools.outputToken.name,
])
```
::::

::::{tab-item} GraphQL
```{code-block} graphql
:caption: This is the GraphQL that subgrounds produces

query {
  liquidityPools {
    inputTokens {
      name
    }
    outputToken {
      name
    }
  }
}
```
::::

:::::


```{note}
If you're having trouble understanding the naming and pathing of the {class}`~subgrounds.FieldPath` classes in subgrounds, we recommend:

* **Use the [Graph*i*QL](https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum) Interface:**
  * Copy and paste the subgraph URL into your web browser to access the [Graph*i*QL](https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum) interface.
  * This tool allows you to build a GraphQL string via the graphical query builder, which can help you understand the structure of the subgraph.

* **Leverage IDE Language Support:**
  * If you use an IDE with Jupyter Notebook support (i.e. VSCode), you can take advantage of the built-in language server to auto-complete the field paths as you work.
  * To use this method, import and load the subgraph in the first notebook cell, then use it in later cells to benefit from auto-completion suggestions based on the schema.
  * This feature is particularly easy to use in VSCode, as the included Python extension automatically enables this behavior.
```

```{toctree}
:caption: Field Paths
:hidden:

arguments
merging
```
