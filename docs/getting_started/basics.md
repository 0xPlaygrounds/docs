# The Basics

::::{important}
This documentation is ✨ interactive ✨, allowing you to easily test and experiment with subgrounds. By clicking the "Run Code" button below, a Python server will be launched in the background using Jupyter Notebook. This will give you access to a Python environment where you can execute and interact with subgrounds code in real-time.

Once you click the button below, the code cells will visually change with 3 new buttons:

- Run
  - This executes the current cell
- Restart
  - This will restart the entire session
- Restart & Run All
  - This will restart the kernel and run every cell from top to bottom.

*Note: Based on server load, interactivity might take a second.*

```{thebe-button}
```

::::


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
aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

# Load a vanilla GraphQL API using its API URL
snapshot = sg.load_api('https://hub.snapshot.org/graphql')
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
