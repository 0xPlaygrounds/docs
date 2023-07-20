# Exporting Data

Once you've done your work with `subgrounds`, it might be time to export your CSV to another platform. This can be simply handled by {mod}`pandas` via {func}`pandas.DataFrame.to_csv`.

{{ thebe_button }}

## Example

In this example, we'll export some curve data for further analysis.

```{code-block} python
:caption: Gathering some daily snapshots from the aave-v2 subgraph
:class: thebe

from subgrounds import Subgrounds

sg = Subgrounds()
aave_v2 = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")

df = sg.query_df(aave_v2.Query.market_DailySnapshots(first=1000))
df.head()  # show the first 5 rows
```

```{code-block} python
:caption: Save this data into a CSV (won't be available through the docs)
:class: thebe

df.to_csv("my_data.csv")
```

```{tip}
There are several other formats that can be exported, all describes [here](https://pandas.pydata.org/docs/user_guide/io.html).
```

You can also easily load CSV files back into {mod}`pandas`.

```{code-block} python

import pandas as pd

df2 = pd.read_csv("my_data.csv)
df2.head()
```
