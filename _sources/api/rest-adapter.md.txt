# Playgrounds Subgraph REST Adapter
The Playgrounds API offers users to query data from subgraphs hosted on The Graph's decentralized network through REST-like endpoints via a service we call the REST adapter.

The Playgrounds REST Adapter allows users to query toplevel GraphQL API fields (with any arguments that those fields accept in GraphQL) via a REST-like endpoint of the following form:
```
GET /v1/proxy/subgraphs/id/:subgraph_id/:toplevel_field?arg1=value1&arg2=value2&...
```
Where `subgraph_id` is the ID of the decentralized network subgraph, `toplevel_field` is the toplevel field being queried and `arg1`, `arg2`, `value1` and `value2` are the arguments and their values to use while querying the toplevel field.

Under the hood, the Playgrounds REST Adapter will make the following GraphQL request to the decentralized network subgraph with ID `subgraph_id`:
```graphql
query {
    toplevel_field(
        arg1=value1,
        arg2=value2,
        ...
    ) {
        // Auto select all non-list fields
    }
}
```

```{note}
There is no fixed set of toplevel field or arguments that the REST Adapter accepts, as the field and arguments are inserted as-in the GraphQL query made to the underlying subgraph. Therefore, the supported arguments will vary based on the subgraph itself.
```

## Example
To understand how to use the REST Adapter, let's look at an example. Consider Messari's Uniswap V3 Ethereum [subgraph](https://thegraph.com/explorer/subgraphs/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7?view=Overview&chain=mainnet) hosted on the decentralized network. This subgraph contains multiple entity types, so let us focus on just one: the `LiquidityPool` entity type. There are two toplevel fields that you can use to query data about liquidity pools on the subgraph: the `liquidityPool` field that returns a specific pool, and the `liquidityPools` field that returns a list of pools.

```{note}
In the code samples below, we are passing query parameters to curl via its `--data-urlencode` flag. This is strictly to make the samples more readable. When making requests yourself, you can specify query parameters using the `endpoint?arg1=value1&arg2=value2&...` method.
```

### Querying the `liquidityPool` field
:::::{tab-set}

::::{tab-item} Playgrounds API
```{code-block} bash
:class: thebe
:caption: Querying a subgraph via a REST adapter endpoint

# This command fetches the details of a specific liquidity pool using its id.
# '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' is the id of the liquidity pool.
# Replace 'PG_API_KEY' with your own Playgrounds API Key.
# Make sure to url-encode the data.

curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7/liquidityPool \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    --data-urlencode id="0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640" \
    -G
```
::::

::::{tab-item} Equivalent GraphQL
```{code-block} graphql
:caption: This is the GraphQL that the REST Adapter runs

query {
  liquidityPool(id: "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640") {
    id
    protocol {
      id
    }
    name
    symbol
    outputToken {
      id
    }
    isSingleSided
    createdTimestamp
    createdBlockNumber
    totalValueLockedUSD
    cumulativeSupplySideRevenueUSD
    cumulativeProtocolSideRevenueUSD
    cumulativeTotalRevenueUSD
    cumulativeVolumeUSD
    outputTokenSupply
    outputTokenPriceUSD
    stakedOutputTokenAmount
  }
}
```
::::

::::{tab-item} Response
```{code-block} json
:caption: The is the response (at time of writing)

[
    {
        "liquidityPool_id": "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", 
        "liquidityPool_protocol_id": "0x1f98431c8ad98523631ae4a59f267346ea31f984", 
        "liquidityPool_name": "Uniswap V3 USD Coin/Wrapped Ether 0.05%", 
        "liquidityPool_symbol": "USD Coin/Wrapped Ether", 
        "liquidityPool_outputToken_id": null, 
        "liquidityPool_isSingleSided": false, 
        "liquidityPool_createdTimestamp": 1620250931, 
        "liquidityPool_createdBlockNumber": 12376729, 
        "liquidityPool_totalValueLockedUSD": 232121148.97514996, 
        "liquidityPool_cumulativeSupplySideRevenueUSD": 188397590.89276817, "liquidityPool_cumulativeProtocolSideRevenueUSD": 0.0, 
        "liquidityPool_cumulativeTotalRevenueUSD": 188397590.89276817, 
        "liquidityPool_cumulativeVolumeUSD": 376795181785.5363, 
        "liquidityPool_outputTokenSupply": null, 
        "liquidityPool_outputTokenPriceUSD": null, 
        "liquidityPool_stakedOutputTokenAmount": null
    }
]
```
::::

:::::

### Querying the `liquidityPools` field
:::::{tab-set}

::::{tab-item} Playgrounds API
```{code-block} bash
:class: thebe
:caption: Querying a subgraph via a REST adapter endpoint

# This command fetches the details of a list of liquidity pools ordered by their .
# '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' is the id of the liquidity pool.
# Replace 'PG_API_KEY' with your own Playgrounds API Key.
# Make sure to url-encode the data.

curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7/liquidityPools \
    -H 'Content-Type: application/json' \
    -H 'Playgrounds-Api-Key: PG_API_KEY' \
    --data-urlencode orderBy="totalValueLockedUSD" \
    --data-urlencode orderDirection="desc" \
    --data-urlencode first=5 \
    -G
```
::::

::::{tab-item} Equivalent GraphQL
```{code-block} graphql
:caption: This is the GraphQL that the REST Adapter runs

query {
  liquidityPools(
    orderBy: totalValueLockedUSD,
    orderDirection: desc,
    first: 5
  ) {
    id
    protocol {
      id
    }
    name
    symbol
    outputToken {
      id
    }
    isSingleSided
    createdTimestamp
    createdBlockNumber
    totalValueLockedUSD
    cumulativeSupplySideRevenueUSD
    cumulativeProtocolSideRevenueUSD
    cumulativeTotalRevenueUSD
    cumulativeVolumeUSD
    outputTokenSupply
    outputTokenPriceUSD
    stakedOutputTokenAmount
  }
}
```
::::

::::{tab-item} Response
```{code-block} json
:caption: The is the response (at time of writing)

[
    {
        "liquidityPools_id": "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
        "liquidityPools_protocol_id": "0x1f98431c8ad98523631ae4a59f267346ea31f984",
        "liquidityPools_name": "Uniswap V3 USD Coin/Wrapped Ether 0.05%",
        "liquidityPools_symbol": "USD Coin/Wrapped Ether",
        "liquidityPools_outputToken_id": null,
        "liquidityPools_isSingleSided": false,
        "liquidityPools_createdTimestamp": 1620250931,
        "liquidityPools_createdBlockNumber": 12376729,
        "liquidityPools_totalValueLockedUSD": 232283647.6876603,
        "liquidityPools_cumulativeSupplySideRevenueUSD": 188398595.81588522,
        "liquidityPools_cumulativeProtocolSideRevenueUSD": 0.0,
        "liquidityPools_cumulativeTotalRevenueUSD": 188398595.81588522,
        "liquidityPools_cumulativeVolumeUSD": 376797191631.77045,
        "liquidityPools_outputTokenSupply": null,
        "liquidityPools_outputTokenPriceUSD": null,
        "liquidityPools_stakedOutputTokenAmount": null
    },
    {
        "liquidityPools_id": "0xcbcdf9626bc03e24f779434178a73a0b4bad62ed",
        "liquidityPools_protocol_id": "0x1f98431c8ad98523631ae4a59f267346ea31f984",
        "liquidityPools_name": "Uniswap V3 Wrapped BTC/Wrapped Ether 0.3%",
        "liquidityPools_symbol": "Wrapped BTC/Wrapped Ether",
        "liquidityPools_outputToken_id": null,
        "liquidityPools_isSingleSided": false,
        "liquidityPools_createdTimestamp": 1620158974,
        "liquidityPools_createdBlockNumber": 12369821,
        "liquidityPools_totalValueLockedUSD": 230238593.9919836,
        "liquidityPools_cumulativeSupplySideRevenueUSD": 65753789.13643069,
        "liquidityPools_cumulativeProtocolSideRevenueUSD": 0.0,
        "liquidityPools_cumulativeTotalRevenueUSD": 65753789.13643069,
        "liquidityPools_cumulativeVolumeUSD": 21917929712.143562,
        "liquidityPools_outputTokenSupply": null,
        "liquidityPools_outputTokenPriceUSD": null,
        "liquidityPools_stakedOutputTokenAmount": null
    },
    {
        "liquidityPools_id": "0x5777d92f208679db4b9778590fa3cab3ac9e2168",
        "liquidityPools_protocol_id": "0x1f98431c8ad98523631ae4a59f267346ea31f984",
        "liquidityPools_name": "Uniswap V3 Dai Stablecoin/USD Coin 0.01%",
        "liquidityPools_symbol": "Dai Stablecoin/USD Coin",
        "liquidityPools_outputToken_id": null,
        "liquidityPools_isSingleSided": false,
        "liquidityPools_createdTimestamp": 1636771503,
        "liquidityPools_createdBlockNumber": 13605124,
        "liquidityPools_totalValueLockedUSD": 107819924.35568458,
        "liquidityPools_cumulativeSupplySideRevenueUSD": 1622101.1642873317,
        "liquidityPools_cumulativeProtocolSideRevenueUSD": 0.0,
        "liquidityPools_cumulativeTotalRevenueUSD": 1622101.1642873317,
        "liquidityPools_cumulativeVolumeUSD": 16221011642.873318,
        "liquidityPools_outputTokenSupply": null,
        "liquidityPools_outputTokenPriceUSD": null,
        "liquidityPools_stakedOutputTokenAmount": null
    },
    {
        "liquidityPools_id": "0x4585fe77225b41b697c938b018e2ac67ac5a20c0",
        "liquidityPools_protocol_id": "0x1f98431c8ad98523631ae4a59f267346ea31f984",
        "liquidityPools_name": "Uniswap V3 Wrapped BTC/Wrapped Ether 0.05%",
        "liquidityPools_symbol": "Wrapped BTC/Wrapped Ether",
        "liquidityPools_outputToken_id": null,
        "liquidityPools_isSingleSided": false,
        "liquidityPools_createdTimestamp": 1620246230,
        "liquidityPools_createdBlockNumber": 12376387,
        "liquidityPools_totalValueLockedUSD": 101248927.14332195,
        "liquidityPools_cumulativeSupplySideRevenueUSD": 24675664.844030958,
        "liquidityPools_cumulativeProtocolSideRevenueUSD": 0.0,
        "liquidityPools_cumulativeTotalRevenueUSD": 24675664.844030958,
        "liquidityPools_cumulativeVolumeUSD": 49351329688.06192,
        "liquidityPools_outputTokenSupply": null,
        "liquidityPools_outputTokenPriceUSD": null,
        "liquidityPools_stakedOutputTokenAmount": null
    },
    {
        "liquidityPools_id": "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8",
        "liquidityPools_protocol_id": "0x1f98431c8ad98523631ae4a59f267346ea31f984",
        "liquidityPools_name": "Uniswap V3 USD Coin/Wrapped Ether 0.3%",
        "liquidityPools_symbol": "USD Coin/Wrapped Ether",
        "liquidityPools_outputToken_id": null,
        "liquidityPools_isSingleSided": false,
        "liquidityPools_createdTimestamp": 1620169800,
        "liquidityPools_createdBlockNumber": 12370624,
        "liquidityPools_totalValueLockedUSD": 92449711.12438808,
        "liquidityPools_cumulativeSupplySideRevenueUSD": 211586809.13452512,
        "liquidityPools_cumulativeProtocolSideRevenueUSD": 0.0,
        "liquidityPools_cumulativeTotalRevenueUSD": 211586809.13452512,
        "liquidityPools_cumulativeVolumeUSD": 70528936378.17505,
        "liquidityPools_outputTokenSupply": null,
        "liquidityPools_outputTokenPriceUSD": null,
        "liquidityPools_stakedOutputTokenAmount": null
    }
]
```
::::

:::::