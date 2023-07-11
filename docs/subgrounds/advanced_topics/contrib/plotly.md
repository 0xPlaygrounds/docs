# Plotly

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.4.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

The Subgrounds Plotly Wrapper is an extension of the Plotly components to understand and work seamlessly with the Subgrounds library. It provides a convenient way to visualize data fetched from subgraphs using Plotly, by wrapping Plotly's trace components with additional functionality.

**Resources**
- [Plotly Docs](https://plotly.com/python/)

```{thebe-button}
```

## Getting Started

To start using the Subgrounds Plotly Wrapper, you'll need to import the required components:

```python
from subgrounds import Subgrounds
from subgrounds.contrib.plotly import Figure, Indicator
```
Next, load your subgraph using the Subgrounds library:

```python
sg = Subgrounds()
aave_v2 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")
```
Now, you can create a Figure instance with the appropriate traces:

```python
Figure(
    subgrounds=sg,
    traces=[
        Indicator(value=pair.token0Price),
    ],
)
```
## Examples

Here are some code examples demonstrating how to use the Subgrounds Plotly Wrapper:

### Simple Indcator
```{code-block} python
:caption: An indicator for the price of a token
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

### Scatter and Bar Plots
```{code-block} python
:caption: Scatter and bar plots across a months worth of data
:class: thebe

from datetime import datetime

import pandas as pd

from subgrounds import FieldPath, Subgrounds, SyntheticField
from subgrounds.contrib.plotly import Figure, Scatter, Bar

sg = Subgrounds()

lido_activity = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/lido-ethereum"
)

usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(
    orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp,
    orderDirection="desc",
    first=30,
)

daily_snapshot = lido_activity.UsageMetricsDailySnapshot

daily_snapshot.datetime = SyntheticField.datetime_of_timestamp(
    daily_snapshot.timestamp
)

# Create the Scatter trace with appropriate field paths
trace = Scatter(
    x=usage_daily_snapshot_30days.datetime,
    y=usage_daily_snapshot_30days.dailyActiveUsers,
)

# Create the Figure instance with the trace and display it
fig = Figure(
    subgrounds=sg,
    traces=trace,
    layout=dict(
        title="Daily Active Users vs Datetime",
        xaxis=dict(title="Datetime"),
        yaxis=dict(title="Daily Active Users")
    ),
)

# Create the Bar trace with appropriate field paths:
trace2 = Bar(
    x=usage_daily_snapshot_30days.datetime,
    y=usage_daily_snapshot_30days.dailyTransactionCount,
)

# Create the Figure instance with the trace and display it:
fig2 = Figure(
    subgrounds=sg,
    traces=trace2,
    layout=dict(
        title="Daily Transaction Count",
        xaxis=dict(title="Datetime"),
        yaxis=dict(title="Daily Transaction Count")
    ),
)
```

```{code-block} python
:class: thebe
:caption: Show figure 1

fig.figure.show()
```

```{code-block} python
:class: thebe
:caption: Show figure 2

fig2.figure.show()
```

In this example, we first load a subgraph and fetch data for the past 30 days. We then create a synthetic field to convert the timestamp into a datetime object. Next, we create a Scatter trace and a Bar trace with the appropriate field paths. Finally, we create two Figure instances and display them.

With the Subgrounds Plotly Wrapper, you can easily extend the provided classes to support more Plotly trace types and create custom visualizations for your subgraph data.
