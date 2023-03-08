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

The following example grabs a aave-v2 subgraph and queries market name and their total value locked (in USD) from the the top-level markets entity into a pandas `DataFrame`.

```{repl}
#repl:hide-output
from subgrounds import Subgrounds
#repl:show-output

sg = Subgrounds()

# Load
aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

# Construct the query
latest = aave_v2.Query.markets(
  orderBy=aave_v2.Market.totalValueLockedUSD,
  orderDirection='desc',
  first=5,
)

# Return query to a dataframe
sg.query_df([
  latest.name,
  latest.totalValueLockedUSD,
])
```
