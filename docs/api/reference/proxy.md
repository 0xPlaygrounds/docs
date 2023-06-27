# Subgraph Proxy
{bdg-info-line}`/v1/proxy/`

---

The proxy endpoints provide access to subgraphs hosted on The Graph's decentralized network without the need to manage GRT tokens or interact with smart contracts.

The proxy endpoint gets its name from the fact that all endpoints originating from it mirror an equivalent endpoint available on The Graph.

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

---

::::{grid} 1 2 2 2
:gutter: 3

```{grid-item-card}
:link: proxy/subgraph_id
:link-type: doc

<h3 class='gradient-text card-heading'>
    Subgraph ID
</h3>

{bdg-info-line}`/v1/proxy/subgraphs/id`
```

```{grid-item-card}
:link: proxy/deployment_id
:link-type: doc

<h3 class='gradient-text card-heading'>
    Deployment ID
</h3>

{bdg-info-line}`/v1/proxy/deployments/id`
```

::::


```{toctree}
:caption: API Reference
:hidden:

proxy/subgraph_id
proxy/deployment_id
```
