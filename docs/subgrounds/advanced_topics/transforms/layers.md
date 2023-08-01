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
: This transforms requests on-the-way towards `pagination`.

{func}`~subgrounds.transform.RequestTransform.transform_response` / {func}`~subgrounds.transform.DocumentTransform.transform_response`
: This transforms responses backwards from `pagination`.

When fully assembled, the layers act like an onion.

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

`Subgrounds` supports any number of transformations for every query produced — something that ends up being quite complex to fufill! Generally, here are the steps we take when executing the transforms:

1. Convert all {class}`DocumentTransforms <subgrounds.transform.DocumentTransform>` to {class}`DocumentRequestTransform <subgrounds.transform.transforms.DocumentRequestTransform>`.
   - This *greatly* simplifies the transform pipeline.

2. Convert all transformation layers into a generator sandwich.
   - These "sandwiches" essentially create an generator that hold the context of {class}`~subgrounds.query.DataRequest` making it easier for us to transform both {class}`~subgrounds.query.DataRequest` and {class}`~subgrounds.query.DataResponse`.
   - Essentially, we store these in a stack allowing us to easily iterate through them.

3. Waterfall the first {class}`~subgrounds.query.DataRequest` through all of the generators in the stack.
   - The first request gets transformed through each generators within the stack.

4. Forward the final transformed {class}`~subgrounds.query.DataRequest` to pagination (and eventually execution).

5. Receive the raw {class}`~subgrounds.query.DataResponse` from pagination / execution.

6. In reverse, waterfall this {class}`~subgrounds.query.DataResponse` up the generator stack.

7. Return this {class}`~subgrounds.query.DataResponse` as the result of the transformation pipeline.

::::{admonition} See also the implementation of this in {func}`~subgrounds.transform.apply.apply_transforms`
:class: seealso admonition dropdown

This function is called within {func}`~subgrounds.client.SubgroundsBase._execute` to assemble and execution the transformation process. We use the generator design to help implement the "sans-io" approach which helps us separate this transformation pipeline from the actual execution of the request (from a call-stack POV).

```{code-include}
:link-at-bottom:
:link-to-documentation:

:func:`subgrounds.transform.apply.apply_transforms`
```

::::

## Visual Guide

<figcaption style="text-align: center; padding: 0.25em">This is the general flow of how a request gets tranformed through the pipeline.</figcaption>

<img src="https://app.eraser.io/workspace/CtIBJDofsGNpuNWBuMbP/preview?elements=e1GFA8BLmiF-rHdNsncf6g&type=embed" style="filter: invert(95%)" class="only-dark"/>

<img src="https://app.eraser.io/workspace/CtIBJDofsGNpuNWBuMbP/preview?elements=e1GFA8BLmiF-rHdNsncf6g&type=embed" class="only-light"/>
