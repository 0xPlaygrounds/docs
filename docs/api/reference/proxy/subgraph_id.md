# Subgraph ID
## {bdg-dark}`POST` `subgraphs/id/:subgraph_id/`
Make a graphql request to the subgraph identified by the id `subgraph_id`.

```{important}
This endpoint only works with subgraphs deployed on The Graph's Ethereum decentralized service and **not** the Arbitrum decentralized service.

If you want to query a subgraph hosted on the Arbitrum decentralized service, use the [proxy by deployment id](deployment_id.md) endpoint.
```

<div style="width:100%">

**Path parameters**<br>
| Name            | Type   | Description                       |
| --------------- | ------ | --------------------------------- |
| **subgraph_id** | String | Decentralized network subgraph ID |
</div>

<div style="width:100%">

**Request body (JSON)**<br>
| Name          | Type    | Description                                                 |
| ------------- | ------- | ----------------------------------------------------------- |
| **query**     | `str`   | GraphQL query                                               |
| **variables** | `dict?` | Values for the variables used in the GraphQL query (if any) |
</div>

**Example**<br>
```bash
curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    -d '{"query":"{protocols {name totalPoolCount}}"}'
```

Response:
```json
{
    "data":{
        "protocols":[
            {
                "name": "Uniswap V3",
                "totalPoolCount": 13767
            }
        ]
    }
}
```

## {bdg-dark}`GET` `/v1/proxy/subgraphs/id/:subgraph_id/:toplevel_field`
