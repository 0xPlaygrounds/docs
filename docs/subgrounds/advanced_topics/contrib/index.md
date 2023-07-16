# Contrib

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.0.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

## What is this?
Contrib is a niche concept in some libraries that represent extra / contributed content to a library that may not fit in the main package. This might be due to the maintainer not willing to maintain said content, the content being deemed too experimental, or perhaps it's unknown whether it's a "good idea" or not.

> Relevant [Stackoverflow](https://softwareengineering.stackexchange.com/questions/252053/whats-in-the-contrib-folder) post

For us, `subgrounds.contrib` represents extra features and ideas with `subgrounds` that generally builds upon the core part of `subgrounds`. It allows us to add extensions or features to other libraries (such as `plotly`) without *relying* on the library as a dependency. We might add new concepts to this subpackage in the future, so look out!

## What's currently here?

### [Plotly](plotly)
Originally located in `plotly_wrappers`, `subgrounds.contrib.plotly` contains helpful wrappers on `plotly` objects that allow you to use {class}`FieldPaths <subgrounds.FieldPath>` directly without creating a {class}`~pandas.DataFrame`.

### Dash
Originally located in `subgrounds.dash_wrappers`, `subgrounds.contrib.dash` contains helpful wrappers on `dash` objects that allow you to use other wrapped visualization objects (currently `subgrounds.contrib.plotly`) in `dash` apps without creating {class}`DataFrames <pandas.DataFrame>`.

### [Pyodide](pyodide)
This module only is activated in a WASM / pyodide environment.

```{warning}
The `contrib` subpackage of `subgrounds` does **not** follow the same semver patterns that `subgrounds` does. This means, there **can** be breaking changes between **minor** versions of the package. In the future, we *may* consider a stabilization route for `contrib`.

This is purely a place for us to experiment with new ideas, including enriching popular libraries with `subgrounds`.
```

```{toctree}
:caption: Advanced Topics
:hidden:

plotly
```
