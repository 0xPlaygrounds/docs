# Subgraph ID
{bdg-info-line}`/v1/proxy/`

## `subgraphs/id/:subgraph_id`

### {bdg-dark}`POST`
Make a graphql request to the subgraph identified by the id `subgraph_id`.

```{important}
This endpoint only works with subgraphs deployed on The Graph's Ethereum decentralized service and **not** the Arbitrum decentralized service.

If you want to query a subgraph hosted on the Arbitrum decentralized service, use the [proxy by deployment id](deployment_id.md) endpoint.
```

<br>

#### URL Parameters
<div class='sd-bg-secondary' style='width: 95%; height: 1px; margin: 0em 0em 0.1em 0em'></div>

{bdg-info-line}`subgraph_id` <code class="sd-text-secondary">string</code>
The decentralized network subgraph ID you are querying

<br>

#### Request Body (JSON)
<div class='sd-bg-secondary' style='width: 95%; height: 1px; margin: 0em 0em 0.1em 0em'></div>

{bdg-info-line}`query` <code class="sd-text-secondary">string</code>
The GraphQL query itself

{bdg-info-line}`variables` <code class="sd-text-secondary">dict?</code>
Values for the variables used within the GraphQL query *(if any)*

<br>

#### Example
<div class='sd-bg-secondary' style='width: 95%; height: 1px; margin: 0em 0em 0.1em 0em'></div>

```bash
curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    -d '{"query":"{protocols {name totalPoolCount}}"}'
```

Response:
```json
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

<!-- 

## `subgraphs/id/:subgraph_id/:toplevel_field`

### {bdg-dark}`GET` 

<br>

#### URL Parameters


<br>

#### Request Body (JSON)

<br>

#### Example
```bash

```

Response:
```json
{}
``` -->
