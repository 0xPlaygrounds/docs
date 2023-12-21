# Exporting to Disk

Once you've done your work with `subgrounds`, it might be time to export your CSV to another platform. This is simply handled by {mod}`pandas` via {meth}`pandas.DataFrame.to_csv`.

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

df = sg.query_df(aave_v2.Query.marketDailySnapshots(first=1000))
df.head()  # show the first 5 rows
```

```{code-block} python
:caption: "Save this data into a CSV (won't be available through the docs)"
:class: thebe

df.to_csv("my_data.csv")
```

```{tip}
There are several other formats that can be exported described [here](https://pandas.pydata.org/docs/user_guide/io.html).
```

You can also easily load CSV files back into a {class}`pandas.DataFrame`.

```{code-block} python
:class: thebe

import pandas as pd

df2 = pd.read_csv("my_data.csv")
df2.head()
```
