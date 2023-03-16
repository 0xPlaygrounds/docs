# Getting Started

## Installation

Subgrounds can be installed via `pip` with the following commands:

```bash
pip install --upgrade subgrounds
# or
python -m pip install --upgrade subgrounds
```

```{important}
Subgrounds requires `python >= 3.10`.

You can check your version of python via: `python --version`
```

```{note}
We recommend creating python environments to help manage your packages. These help in ensuring your projects have the correct versions for the packages you care about.

If you run into problems during installation, see {ref}`env-setup`.
```

## Simple example

The following example grabs a aave-v2 subgraph and queries market name and their total value locked (in USD) from the the top-level markets entity into a pandas {external:class}`~pandas.DataFrame`.

```{repl}
from subgrounds import Subgrounds

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

```{toctree}
:caption: Getting Started
:hidden:

basics
field_paths/index
querying
synthetic_fields
```
