# Synthetic Fields

One of Subgrounds' unique features is the ability to define schema-based (i.e.: pre-querying) transformations using {class}`SyntheticFields <subgrounds.SyntheticField>`.

{class}`SyntheticFields <subgrounds.SyntheticField>` can be created using Python arithmetic operators on relative {class}`~subgrounds.FieldPath` (i.e.: {class}`FieldPaths <subgrounds.FieldPath>` starting from an entity and not the root `Query` object) and must be added to the entity which they enhance. Once added to an entity, {class}`SyntheticFields <subgrounds.SyntheticField>` can be queried just like regular GraphQL fields.

The example below demonstrates how to create a simple {class}`~subgrounds.SyntheticField` to calculate the swap price of `Swap` events stored on the Sushiswap subgraph:

{{ thebe_button }}

```{code-block} python
:class: thebe
from subgrounds import Subgrounds
sg = Subgrounds()

sushiswap = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/sushiswap/exchange")
swap = sushiswap.Swap  # short hand for ease-of-use

# Define a synthetic field named price1 (the swap price of token1,
#   in terms of token0) on Swap entities
swap.price1 = (
    abs(swap.amount0Out - swap.amount0In)
    / abs(swap.amount1Out - swap.amount1In)
)

# Build query to get the last 10 swaps of the WETH-USDC pair on Sushiswap 
weth_usdc = sushiswap.Query.pair(id="0x397ff1542f962076d0bfe58ea045ffa2d347aca0")

last_10_swaps = weth_usdc.swaps(
    orderBy=swap.timestamp,
    orderDirection="desc",
    first=10
)

# Query swap prices using the `SyntheticField` price1 as if they were regular fields
sg.query_df([
    last_10_swaps.timestamp,
    last_10_swaps.price1     # synthetic fields get used the same!
])
```

{class}`SyntheticFields <subgrounds.SyntheticField>` can *also* be created using the constructor, allowing for much more complex transformations.

```{code-block} python
:class: thebe
from datetime import datetime
from subgrounds import SyntheticField

# Create a SyntheticField on the Swap entity called `datetime`, which will format 
# the timestamp field into something more human readable
swap.datetime = SyntheticField(
    f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
    type_=SyntheticField.STRING,
    deps=swap.timestamp,
)

last_10_swaps = sushiswap.Query.swaps(
    orderBy=swap.timestamp,
    orderDirection="desc",
    first=10,
)

sg.query_df([
    last_10_swaps.datetime,
    last_10_swaps.pair.token0.symbol,
    last_10_swaps.pair.token1.symbol,
])
```

## Helpers

Since there are several common instances {class}`SyntheticFields <subgrounds.SyntheticField>` we see in the wild, we've added some helper constructors for ease of use.

### `SyntheticField.datetime_of_timestamp`

This helper constructor makes it easy to convert `timestamps` into {class}`~datetime.datetime` objects.

:::::{tab-set}

::::{tab-item} Helper Method
```{code-block} python

swap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)
```
::::

::::{tab-item} Translation
```{code-block} python

swap.datetime = SyntheticField(
    f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
    type_=SyntheticField.STRING,
    deps=swap.timestamp,
)
```
::::

:::::

<!-- ### `SyntheticField.map`

This constructor allows you to map values from field paths via key-values set in a dict, returning a default if not found

:::::{tab-set}

::::{tab-item} Helper Method
```{code-block} python

# Fake mapping of pool addresses to symbol
pooladdr_symbol_map = {
    "0x5777d92f208679db4b9778590fa3cab3ac9e2168": "DAI/USDC-001",
    "0x6c6bc977e13df9b0de53b251522280bb72383700": "DAI/USDC-005",
    "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8": "USDC/ETH-030",
    "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640": "USDC/ETH-005",
}

# Create map SyntheticField using our dictionary with 'UNKNOWN' as the
# default value
sushiswap.Pool.symbol = SyntheticField.map(
    pooladdr_symbol_map,
    SyntheticField.STRING,
    sushiswap.Pool.id,
    "DEFAULT",
)
```
::::

::::{tab-item} Translation
```{code-block} python

swap.datetime = SyntheticField(
    f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
    type_=SyntheticField.STRING,
    deps=swap.timestamp,
)
```
::::

::::: -->
