# Playgrounds Subgraph Proxy
After obtaining your API key, use our proxy API endpoint to query decentralized subgraphs. You can do this in two ways:

1. Via the subgraph id *(compatible with Ethereum only)*
2. Via the subgraph deployment id

## Query by Subgraph id

To query a subgraph by its id, send a POST request to the Playgrounds proxy endpoint:
```
https://api.playgrounds.network/v1/proxy/subgraphs/id/[subgraph-id]
```
For example, to access the latest Uniswap V3 subgraph data using its deployment id, use:
```
https://api.playgrounds.network/v1/proxy/deployments/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7
```

```{important}
This approach is for Ethereum-based subgraphs only. To query a subgraph hosted on Arbitrum, refer to the 'Query by Deployment ID' section [below](#query-a-decentralized-network-subgraph-by-deployment-id).
```

Your POST request must include your Playgrounds API key, used as the Playgrounds-Api-Token header value. The remainder of the request mirrors what you'd typically send to The Graph's decentralized network.<br> 

Here's an example request for the Uniswap V3 subgraph id (`ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7`) on The Graph's decentralized network:

:::::{tab-set}

::::{tab-item} cURL
```{code-block} bash
:class: thebe
:caption: Querying a subgraph via the proxy endpoint using cURL

curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    -d '{"query":"{protocols {name totalPoolCount}}"}'
```

::::

::::{tab-item} Python
```{code-block} python
:caption: Querying a subgraph via the proxy endpoint using Python
resp = requests.post(
    url="https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7",
    headers={
        "Content-Type": "application/json",
        "Playgrounds-Api-Key": "PG_API_KEY"
    },
    json={
        "query": "{protocols {name totalPoolCount}}"
    }
)

resp.json()
```
::::

::::{tab-item} Equivalent GraphQL
```{code-block} graphql
:caption: This is the GraphQL query being sent to the subgraph
query {
    protocols {
        name
        totalPoolCount
    }
}
```
::::

::::{tab-item} Response
```{code-block} json
:caption: The is the response (at time of writing)
{
    "data": {
        "protocols": [
            {
                "name": "Uniswap V3",
                "totalPoolCount": 13767
            }
        ]
    }
}
```
::::

:::::


```{important}
Unlike The Graph's endpoint where the Graph API key is inserted in the URL, Playgrounds API endpoints do **NOT** contain the user's API key in the URL itself. Instead, the API key is provided via a header value.
```

```{note}
This endpoint mirrors the Graph's decentralized network gateway endpoint (see below) with one key difference: the API key is not part of the URL.

https://gateway.thegraph.com/api/[api-key]/subgraphs/id/[subgraph-id]
```

### Finding a subgraph's ID
A decentralized network subgraph's ID can easily be obtained from The Graph's decentralized network [explorer](https://thegraph.com/explorer).

![](/_static/assets/graph-explorer-id.png)

## Query a decentralized network subgraph by deployment id

To query a decentralized network subgraph by its deployment ID, you can make a POST request to the following Playgrounds proxy endpoint:
```
https://api.playgrounds.network/v1/proxy/deployments/id/[deployment-id]
```

For example, to query the latest Uniswap V3 subgraph on the decentralized network by its deployment id, use the following URL:
```
https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ
```

Apart from the exact path, both endpoints work essentially the same way. Just like when querying a subgraph by its deployment ID, you will have to set the `Playgrounds-Api-Token` header's value to your API key and you will have to make a POST request containing your GraphQL query.

Here is an example querying the latest Uniswap V3 subgraph (deployment ID `QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ`) on The Graph's decentralized network:

:::::{tab-set}

::::{tab-item} cURL
```{code-block} bash
:class: thebe
:caption: Querying a subgraph via the proxy endpoint using cURL

curl https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    -d '{"query":"{protocols {name totalPoolCount}}"}'
```
::::

::::{tab-item} Python
```{code-block} python
:caption: Querying a subgraph via the proxy endpoint using Python
resp = requests.post(
    url="https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ",
    headers={
        "Content-Type": "application/json",
        "Playgrounds-Api-Key": "PG_API_KEY"
    },
    json={
        "query": "{protocols {name totalPoolCount}}"
    }
)

resp.json()
```
::::

::::{tab-item} Equivalent GraphQL
```{code-block} graphql
:caption: This is the GraphQL query being sent to the subgraph
query {
    protocols {
        name
        totalPoolCount
    }
}
```
::::

::::{tab-item} Response
```{code-block} json
:caption: The is the response (at time of writing)
{
    "data": {
        "protocols": [
            {
                "name": "Uniswap V3",
                "totalPoolCount": 13767
            }
        ]
    }
}
```
::::

:::::

### Finding a subgraph's deployment ID
A decentralized network subgraph's deployment ID can easily be obtained from The Graph's decentralized network [explorer](https://thegraph.com/explorer).

![](/_static/assets/graph-explorer-deployment-id.png)
