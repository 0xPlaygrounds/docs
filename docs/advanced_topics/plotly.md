# Contrib - Plotly

The Subgrounds Plotly Wrapper is an extension of the Plotly components to understand and work seamlessly with the Subgrounds library. It provides a convenient way to visualize data fetched from subgraphs using Plotly, by wrapping Plotly's trace components with additional functionality.

**Resources**
- [Plotly Docs](https://plotly.com/python/)

## Getting Started

To start using the Subgrounds Plotly Wrapper, you'll need to import the required components:

```{code-block} python
:class: thebe

from subgrounds import Subgrounds
from subgrounds.contrib.plotly import Figure, Indicator

```
Next, load your subgraph using the Subgrounds library:

```{code-block} python
:class: thebe

sg = Subgrounds()
aave_v2 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")


```
Now, you can create a Figure instance with the appropriate traces:

```{code-block} python
:class: thebe

Figure(
    subgrounds=sg,
    traces=[
        Indicator(value=pair.token0Price),
    ],
)

```
## Examples

Here are some code examples demonstrating how to use the Subgrounds Plotly Wrapper:

Example 1: Creating a simple Indicator

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
Example 2: Creating Scatter and Bar plots using Subgrounds and Plotly Wrapper

```{code-block} python
:class: thebe

from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds, FieldPath
from subgrounds.contrib.plotly import Figure, Scatter, Bar
import pandas as pd
import plotly.graph_objects as go

sg = Subgrounds()

lido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')

usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(
    orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp,
    orderDirection='desc',
    first=30
)

lido_activity.UsageMetricsDailySnapshot.datetime = SyntheticField(
  lambda timestamp: pd.to_datetime(datetime.fromtimestamp(timestamp)),
  SyntheticField.FLOAT,
  lido_activity.UsageMetricsDailySnapshot.timestamp
)

# Create the Scatter trace with appropriate field paths
trace = Scatter(
    x=usage_daily_snapshot_30days.datetime,
    y= usage_daily_snapshot_30days.dailyActiveUsers,
)

# Create the Figure instance with the trace and display it
fig = Figure(
    subgrounds=sg,
    traces=trace,
    layout=dict(
        title="Daily Active Users vs Datetime",
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds, FieldPath
from subgrounds.contrib.plotly import Figure, Scatter, Bar
import pandas as pd
import plotly.graph_objects as go

sg = Subgrounds()

lido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')

usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(
    orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp,
    orderDirection='desc',
    first=30
)

lido_activity.UsageMetricsDailySnapshot.datetime = SyntheticField(
  lambda timestamp: pd.to_datetime(datetime.fromtimestamp(timestamp)),
  SyntheticField.FLOAT,
  lido_activity.UsageMetricsDailySnapshot.timestamp
)

# Create the Scatter trace with appropriate field paths
trace = Scatter(
    x=usage_daily_snapshot_30days.datetime,
    y= usage_daily_snapshot_30days.dailyActiveUsers,
)

# Create the Figure instance with the trace and display it
fig = Figure(
    subgrounds=sg,
    traces=trace,
    layout=dict(
        title="Daily Active Users vs Datetime",
        xaxis=dict(title="Datetime"),
        yaxis=dict(title="Daily Active Users")
))

# Create the Bar trace with appropriate field paths:

trace2 = Bar(
    x=usage_daily_snapshot_30days.datetime,
    y= usage_daily_snapshot_30days.dailyTransactionCount,
)
# Create the Figure instance with the trace and display it:

fig2 = Figure(
    subgrounds=sg,
    traces=trace2,
    layout=dict(
        title="Daily Transaction Count",
        xaxis=dict(title="Datetime"),
        yaxis=dict(title="Daily Transaction Count")
    )
)

# Show the figure:

fig.figure.show()

# Show the second figure:

fig2.figure.show()

```

In this example, we first load a subgraph and fetch data for the past 30 days. We then create a synthetic field to convert the timestamp into a datetime object. Next, we create a Scatter trace and a Bar trace with the appropriate field paths. Finally, we create two Figure instances and display them.

With the Subgrounds Plotly Wrapper, you can easily extend the provided classes to support more Plotly trace types and create custom visualizations for your subgraph data.