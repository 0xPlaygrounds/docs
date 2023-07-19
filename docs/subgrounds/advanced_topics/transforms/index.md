# Transforms

```{article-info}
:avatar-outline: muted
:author: "*Updated in version `1.7.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

The `subgrounds` leverages an internal transformation pipeline that allows us to manipulate the GraphQL AST alongside responses returned from the subgraph — serving as the backbone of [synthetic fields](/subgrounds/getting_started/synthetic_fields). Currently, only a small percentage of the functionalty is exposed via our top-level API, but we are working on leverage this toolchain to it's fullest potential!

## A Visual Intro

<figcaption style="text-align: center; padding: 0.25em">A simple example of how a <code>subgrounds</code> query gets transformed from a high-level</figcaption>

<img src="https://app.eraser.io/workspace/CtIBJDofsGNpuNWBuMbP/preview?elements=uFEznbs0RcPKxT5mc3Wdyw&type=embed" style="filter: invert(95%)" class="only-dark"/>

<img src="https://app.eraser.io/workspace/CtIBJDofsGNpuNWBuMbP/preview?elements=uFEznbs0RcPKxT5mc3Wdyw&type=embed" class="only-light"/>


```{toctree}
:caption: Transforms

layers
```
