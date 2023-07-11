# The Basics

::::{important}
This documentation is ✨ interactive ✨, allowing you to easily test and experiment with subgrounds. By clicking the "Run Code" button below, a Python server will be launched in the background using Jupyter Notebook. This will give you access to a Python environment where you can execute and interact with subgrounds code in real-time.

Each code block acts like a cell within a Jupyter notebook which means they are **connected**. So {class}`~subgrounds.Subgrounds` created in an earlier cell can be reused in lower ones.

Once you click the "Run Code" button, the code cells will visually change with 3 new buttons:

| Command           | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| Run               | This executes the current cell                                      |
| Restart           | This will restart the kernel                                        |
| Restart & Run All | This will restart the kernel and run every cell from top to bottom. |

The *easiest* way to interact with the docs is via the "Restart & Run All" button as it ensures that all the python state is loaded corrected. Then you can feel free to edit a cell and click "Run" to play around as you please.

```{thebe-button}
```

::::

```{warning}
After you click "Run Code", interactivity will begin to hydrate the page and **This takes time**. In some cases, you might need to refresh the page and try again.

This feature is best used on the **latest** Chrome-based browsers, feel free to report any issues on other browsers to our [Discord](https://discord.gg/v4r4zhBAh2).
```


## Subgrounds


The {class}`~subgrounds.Subgrounds` class provides the top level API and most users will be using this class exclusively. This class is used to load (i.e.: introspect) GraphQL APIs (subgraph **or** vanilla GraphQL APIs) as well as execute querying operations. Moreover, this class is meant to be used as a singleton, i.e.: initialized once and reused throughout a project.

The code cell below demonstrates how to initialize your {class}`~subgrounds.Subgrounds` object and load a GraphQL API.

> Both {class}`~subgrounds.Subgrounds.load_subgraph` and {class}`~subgrounds.Subgrounds.load_api` result in similar structures except subgraphs provide better optics since there's more schema data to explore.

```{code-block} python
:class: thebe
:caption: Loading Aave v2 and snapshot api sources

from subgrounds import Subgrounds

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
aave_v2 = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")

# Load a vanilla GraphQL API using its API URL
snapshot = sg.load_api("https://hub.snapshot.org/graphql")
```

## Getting the Data

Once you load in your subgraphs (or vanilla APIs), you can start gathering data via {func}`~subgrounds.Subgrounds.query`.

```{code-block} python
:class: thebe
:caption: Gathering the names of the latest markets in Aave

sg.query([
    aave_v2.Query.markets.name
])

```

```{code-block} python
:class: thebe
:caption: Gathering the titles and scores of the latest proposals from snapshot

sg.query([
    snapshot.Query.proposals.title,
    snapshot.Query.proposals.scores_total,
])
```
