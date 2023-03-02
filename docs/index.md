---
hide-toc: true
---

# Subgrounds

A Pythonic data access layer for applications querying data from The Graph Network.

## Design goals
- **Simple**: Easy to use toplevel API
- **Automated**: Schema introspection and class generation, type checking and pagination is all handled automatically
- **Schema-Driven**: Queries are built with `FieldPaths` while transformations are defined with `SyntheticFields`, as opposed to raw GraphQL and transforming raw data

```{repl}
#repl:hide-output
from subgrounds import Subgrounds
#repl:show-output

sg = Subgrounds()
subgraph = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3")

sg.query_df(subgraph.Query.pools)
```

---

::::{grid} 1 2 2 2
:gutter: 3

```{grid-item-card}
:link: getting_started
:link-type: doc

<h3 class='gradient-text' style='font-size: 24px'> Getting Started </h3>
Start using Subgrounds in 5 minutes!
```

```{grid-item-card}
:link: basics
:link-type: doc

<h3 class='gradient-text' style='font-size: 24px'> The Basics </h3>
Learn how to conjure simple queries
```

```{grid-item-card}
:link: examples
:link-type: doc

<h3 class='gradient-text' style='font-size: 24px'> Examples </h3>
Checkout our curated list of community examples
```

```{grid-item-card}
:link: troubleshooting
:link-type: doc

<h3 class='gradient-text' style='font-size: 24px'> FAQ </h3>
Quick answers to your most burning questions
```
::::

---


```{toctree}
:caption: Subgrounds
:hidden:

getting_started
basics
advanced
troubleshooting
examples
API Reference <modules>
```

<!-- ```{toctree}
:caption: Development
:hidden:

contributing
``` -->
