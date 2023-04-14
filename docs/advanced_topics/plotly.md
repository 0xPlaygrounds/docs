# Contrib - Plotly
> This page will assume you are generally comfortable with using Plotly

**Resources**
- [Plotly Docs](https://plotly.com/python/)

## Getting Started

```{code-block} python
:class: thebe

from subgrounds import Subgrounds
from subgrounds.contrib.plotly import Figure, Indicator

sg = Subgrounds()
aave_v2 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")

Figure(
    subgrounds=sg,
    traces=[
        Indicator(value=pair.token0Price),
    ],
)
```
