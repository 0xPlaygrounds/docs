# {{ new_bdg }} Grouping

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.7.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

Query grouping allows you to effectively manage multiple queries to communicate more effectively with servers. It uses the idea of sessions and/or clients (in libraries like `httpx` or `requests`) to keep networking connections open which makes multiple or dependent queries more efficient and quicker.

This feature is easily usable via context managers and the `with` statement:

```{thebe-button}
```

```{code-block} python
:class: thebe
:caption: Gathering data from aave maarkets

from subgrounds import Subgrounds

sg = Subgrounds()
with sg:
    aave_v2 = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum"
    )

    aave_markets = aave_v2.Query.markets(
        first=3,
        orderBy=aave_v2.Market.totalValueLockedUSD,
        orderDirection="desc",
        where=[
            aave_v2.Market.createdBlockNumber > 14720000
        ]
    )

    data = sg.query([
        aave_markets.name,
        aave_markets.totalValueLockedUSD,
    ])

    raw_data = sg.query_json([
        aave_markets.name,
        aave_markets.totalValueLockedUSD,
    ])

print(data, "\n", raw_data)
```

Within the context of `with`, using the same {class}`~subgrounds.Subgrounds` object will ensure all queries are made with open and reusable connections!

::::{note}
You can also immediately use the {class}`~subgrounds.Subgrounds()` inside your context manager. This *will* leave `sg` only available within the `with` block which would be inconvenient for larger scripts or projects, but could be useful with quick testing.

```py
with Subgrounds() as sg:
    sg.load_subgraph(...)
```
::::
