# API Reference
The Playgrounds API is organized around REST and currently features only one top-level resource accessible with an API key: the `proxy` resource.

Our API accepts request parameters either via a JSON-encoded request body (for POST requests) or query parameters (for GET requests). Unless explicitly mentioned, all API endpoints return JSON-encoded responses.

## Authentication
The Playgrounds API uses API keys to authenticate requests. You can view and manage your API keys in the [Playgrounds App](https://app.playgrounds.network).

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

Authentication to the API is performed via the custom Playgrounds authorization header `Playgrounds-Api-Key`. To authenticate, include the following into the header of your request (replacing `pg-abcdefghijk` with your own)!

```py
Playgrounds-Api-Key: pg-abcdefghijk
```

```{note}
In `subgrounds`, you can set the `$PLAYGROUNDS_API_KEY` environment variable to your API key and use our endpoints — the library will handle all of the authentication on your behalf!
```

```{toctree}
:caption: API Reference
:hidden:

reference/proxy
```

## Endpoints

We currently only host a *single* endpoint.

::::{grid} 1 2 2 2
:gutter: 3

```{grid-item-card}
:link: reference/proxy
:link-type: doc

<h3 class='gradient-text card-heading'>
    Subgraph Proxy
</h3>

{bdg-info-line}`/v1/proxy`
```

::::
