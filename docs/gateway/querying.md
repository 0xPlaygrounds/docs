# Querying through the Gateway
Once you have your API key, you can use our proxy API endpoint to query the Graph's decentralized network.

To query a decentralized network subgraph with id `subgraph-id`, you can make a POST request to the Playgrounds proxy endpoint:
```
https://api.playgrounds.network/v1/proxy/subgraphs/id/[subgraph-id]
```

The POST request itself will have to contain the Playgrounds API key you generated earlier as the value of the `Playgrounds-Api-Token` header. The rest of the request will be the same as the request you would usually make to the Graph's decentralized network. Here is an example of Playgrounds Gateway request sent using `curl`:

```bash
curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    -d '{"query":"{protocols {id}}"}'
```

Note: This endpoint mirrors the Graph's decentralized network gateway endpoint (see below) with one key difference: the API key is not part of the URL.

```
https://gateway.thegraph.com/api/[api-key]/subgraphs/id/[subgraph-id]
```

## Finding a decentralized subgraph ID
A decentralized network subgraph's can easily be obtained from The Graph's decentralized network [explorer](https://thegraph.com/explorer).

![](/_static/assets/graph-explorer-id.png)
