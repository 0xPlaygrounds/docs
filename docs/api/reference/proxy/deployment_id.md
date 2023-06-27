# Deployment ID
{bdg-info-line}`/v1/proxy/`

## `deployments/id/:deployment_id/`

### {bdg-dark}`POST` 
Make a graphql request to the subgraph identified by the id `deployment_id`.

<br>

#### URL Parameters
<div class='sd-bg-secondary' style='width: 95%; height: 1px; margin: 0em 0em 0.1em 0em'></div>

{bdg-primary-line}`deployment_id` <code class="sd-text-secondary">string</code>
The decentralized network deployment ID you are querying

<br>

#### Request Body (JSON)
<div class='sd-bg-secondary' style='width: 95%; height: 1px; margin: 0em 0em 0.1em 0em'></div>

{bdg-primary-line}`query` <code class="sd-text-secondary">string</code>
The GraphQL query itself

{bdg-primary-line}`variables` <code class="sd-text-secondary">dict?</code>
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


## `deployments/id/:deployment_id/:toplevel_field`

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
```
