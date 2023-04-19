# Contrib

## What is this?
Contrib is a niche concept in some libraries that represent extra / contributed content to a library that may not fit in the main package. This might be due to the maintainer not willing to maintain said content, the content being deemed too experimental, or perhaps it's unknown whether it's a "good idea" or not.

> Relevant [Stackoverflow](https://softwareengineering.stackexchange.com/questions/252053/whats-in-the-contrib-folder) post

For us, `subgrounds.contrib` represents extra features and ideas with `subgrounds` that generally builds upon the core part of `subgrounds`. It allows us to add extensions or features to other libraries (such as `plotly`) without *relying* on the library as a dependency. We might add new concepts to this subpackage in the future, so look out!

## What's currently here?

### Plotly
Originally located in :module:`~subgrounds.plotly_wrappers`, :module:`~subgrounds.contrib.plotly` contains helpful wrappers on `plotly` objects that allow you to use `FieldPaths <subgrounds.FieldPath>` directly without creating a :class:`~pandas.DataFrame`.

### Dash
Originally located in :module:`~subgrounds.dash_wrappers`, :module:`~subgrounds.contrib.dash` contains helpful wrappers on `dash` objects that allow you to use other wrapped visualization objects (currently :module:`~subgrounds.contrib.plotly`) in `dash` apps without creating :class:`DataFrames <pandas.DataFrame>`.