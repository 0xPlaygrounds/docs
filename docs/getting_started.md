# Getting Started

## Installation

Subgrounds can be installed via `pip` with the following command:
`pip install subgrounds`

```{important}
Subgrounds requires `python>=3.10`
```

```{note}
If you run into problems during installation, see {ref}`Set up an isolated environment <isolated_environment_setup>`.
```

## Simple example

The following example grabs a uniswap-v3 subgraph and queries the top-level pools entity as a pandas `DataFrame`. 

```{repl}
#repl:hide-output
from subgrounds import Subgrounds
#repl:show-output

sg = Subgrounds()
subgraph = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3")

sg.query_df(subgraph.Query.pools)
```
