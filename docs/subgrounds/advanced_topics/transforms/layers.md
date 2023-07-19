# Layers

```{caution}
# 🚧 **IN CONSTRUCTION** 🚧

This doc is **incomplete**, check back soon!
```

Transformations in `subgrounds` operate via layers, where one is applied after another. There are two types of transforms:

{class}`~subgrounds.transform.RequestTransform`
: This transform operates on a {class}`~subgrounds.query.DataRequest` and {class}`~subgrounds.query.DataResponse` which represent the total query being made via one operation of {class}`~subgrounds.client.SubgroundsBase._execute`.

{class}`~subgrounds.transform.DocumentTransform`
: This transform operates on a {class}`~subgrounds.query.Document` and {class}`~subgrounds.query.DocumentResponse` which (ignoring [pagination](/subgrounds/advanced_topics/pagination)) represent a part of the total query that will be made. Each {class}`~subgrounds.query.Document` cooresponds to a single subgraph server.

Each layer contains two important functions:

{func}`~subgrounds.transform.RequestTransform.transform_request` / {func}`~subgrounds.transform.DocumentTransform.transform_document`
: This transforms requests on-the-way towards `pagination`

{func}`~subgrounds.transform.RequestTransform.transform_response` / {func}`~subgrounds.transform.DocumentTransform.transform_response`
: This transforms responses backwards from `pagination`

When fully assembled, the layers act like an onion — 

```{mermaid}
:caption: "A top-level showcase on how a request turns into a response"

graph LR
    A[`execute`] --> |DataRequest| B[RequestTransform]
    B --> |DataRequest.documents| C(["DocumentTransform(s)"])
    C --> |Document| D[[`paginate`]]
    D --> |DocumentResponse| C
    C --> |"DataResponse.responses"| B
    B --> |"DataResponse"| A
```

## The Pipeline

`Subgrounds` supports any number of transformations for every query produced — something that ends up being quite complex to fufill! Generally, here are the steps we take when executing the transforms.

1. Convert all {class}`DocumentTransforms <subgrounds.transform.DocumentTransform>` to {class}`DocumentRequestTransform <subgrounds.transform.transforms.DocumentRequestTransform>`
   - This *greatly* simplifies the transform pipeline

2. sdohf