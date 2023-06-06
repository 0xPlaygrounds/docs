# Playgrounds Subgraph Proxy
Once you have your API key, you can use our proxy API endpoint to query the Graph's decentralized network. There are two ways to query a subgraph hosted on The Graph's decentralized network with our proxy endpoints:
1. Using the subgraph id *(only works for the Ethereum decentralized network)*
2. Using the subgraph deployment id

## Query a decentralized network subgraph by id

To query a decentralized network subgraph by its id, you can make a POST request to the following Playgrounds proxy endpoint:
```
https://api.playgrounds.network/v1/proxy/subgraphs/id/[subgraph-id]
```
For example, to query the latest Uniswap V3 subgraph on the decentralized network by its deployment id, use the following URL:
```
https://api.playgrounds.network/v1/proxy/deployments/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7
```

```{important}
This will only work for subgraphs deployed to the Ethereum decentralized network. If you want to use our proxy to query a subgraph hosted on the Arbitrum decentralized network, see [below](#query-a-decentralized-network-subgraph-by-deployment-id).
```

The POST request itself will have to contain the Playgrounds API key you generated earlier as the value of the `Playgrounds-Api-Token` header. The rest of the request will be the same as the request you would usually make to the Graph's decentralized network.<br> 

Here is an example querying the Uniswap V3 subgraph (subgraph ID `ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7`) on The Graph's decentralized network:

:::::{tab-set}

::::{tab-item} cURL
```{code-block} bash
:class: thebe
:caption: Querying a subgraph via the proxy endpoint using cURL

curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    -d '{"query":"{protocols {id}}"}'
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
        "query": "{protocols {id}}"
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
        id
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
            {"id": "0x1f98431c8ad98523631ae4a59f267346ea31f984"}
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
    -d '{"query":"{protocols {id}}"}'
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
        "query": "{protocols {id}}"
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
        id
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
            {"id": "0x1f98431c8ad98523631ae4a59f267346ea31f984"}
        ]
    }
}
```
::::

:::::

### Finding a subgraph's deployment ID
A decentralized network subgraph's deployment ID can easily be obtained from The Graph's decentralized network [explorer](https://thegraph.com/explorer).

![](/_static/assets/graph-explorer-deployment-id.png)