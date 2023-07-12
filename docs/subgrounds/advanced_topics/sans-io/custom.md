# Custom Client

Implementing your own `Subgrounds` client only requires you to subclass {class}`~subgrounds.client.SubgroundsBase`.

```{note}
You can also choose to subclass {class}`~subgrounds.Subgrounds` or {class}`~subgrounds.AsyncSubgrounds` as they contain a more natural interface to work with, especially for simply swapping the implementation of the http client.
```

## Methodology

The {class}`~subgrounds.client.SubgroundsBase` class streamlines the process of tracking subgraphs and applying transformations on paginated queries by handling all of the buisness logic while the implementor of the class injects the actual querying logic (the IO) via these methods:

{func}`~subgrounds.client.SubgroundsBase._load`
: This deals with caching and loading subgraph schema data. If subgraph data is successfully loaded from a cache, the actual request execution will be skipped (via a {class}`StopIteration` exception).

{func}`~subgrounds.client.SubgroundsBase._execute`
: This is the main entry point for executing queries via {class}`~subgrounds.query.DataRequest` and returning responses via {class}`~subgrounds.query.DataResponse`. Implementing `execute` allows you to 
