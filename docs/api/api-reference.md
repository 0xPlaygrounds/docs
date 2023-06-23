# API Reference
The Playgrounds API is organized around REST and currently features only one toplevel resources accessible with a Playgrounds API key: the `proxy` resource.

Our API accepts request parameters either via a JSON-encoded request body (for POST requests) or query parameters (for GET requests). Unless explicitely mentioned, all API endpoints return JSON-encoded responses.

## Authentication
The Playgrounds API uses API keys to authenticate requests. You can view and manage your API keys in the [Playgrounds App](https://app.playgrounds.network).

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

Authentication to the API is performed via the custom Playgrounds authorization header `Playgrounds-Api-Key`. To authenticate your request, 

## Endpoints
### Proxy
The proxy endpoints provide access to subgraphs hosted on The Graph's decentralized network without the need to manage GRT tokens or interact with smart contracts. The proxy endpoint gets its name from the fact that all endpoints originating from it mirror an equivalent endpoind available on The Graph.

For example, consider the following query URL:
```bash
https://gateway.thegraph.com/api/[api-key]/subgraphs/id/3nXfK3RbFrj6mhkGdoKRowEEti2WvmUdxmz73tben6Mb
```

The equivalent Playgrounds API URL going through our proxy endpoint would be:
```bash
https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7
```

```{note}
Notice that the URL is mirrored: both URLs contain the `subgraphs/id/3nXfK3RbFrj6mhkGdoKRowEEti2WvmUdxmz73tben6Mb` path!
```

```{important}
Unlike The Graph's endpoint where the Graph API key is inserted in the URL, Playgrounds API endpoints do not contain the user's API key in the URL itself. Instead, the API key is provided via a header value.
```

#### `POST /v1/proxy/subgraphs/id/:subgraph_id/`
Make a graphql request to the subgraph identified by the id `subgraph_id`.

```{important}
This endpoint only works with subgraphs deployed on The Graph's Ethereum decentralized service and **not** the Arbitrum decentralized service.

If you want to query a subgraph hosted on the Arbitrum decentralized service, use the [proxy by deployment id](#post-v1proxydeploymentsiddeployment_id) endpoint.
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
    -d '{"query":"{protocols {id}}"}'
```

Response:
```json
{
    "data":{
        "protocols":[
            {"id":"0x1f98431c8ad98523631ae4a59f267346ea31f984"}
        ]
    }
}
```

#### `GET /v1/proxy/subgraphs/id/:subgraph_id/:toplevel_field`


#### `POST /v1/proxy/deployments/id/:deployment_id/`
#### `GET /v1/proxy/deployments/id/:deployment_id/:toplevel_field`