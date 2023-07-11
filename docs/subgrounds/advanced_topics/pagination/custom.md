# Custom Strategies
Subgrounds allows developers to create their own pagination strategy by creating a class that implements the {class}`~subgrounds.pagination.PaginationStrategy` protocol:

```{code-include}
:link-at-bottom:
:link-to-documentation:

:class:`subgrounds.pagination.strategies.PaginationStrategy`
```


The class's constructor should accept a {class}`~subgrounds.schema.SchemaMeta` argument which represents the schema of the subgraph API that the query is directed to and a {class}`~subgrounds.query.Document` argument which represents the query to be paginated on. If no pagination is required for the given document, then the constructor should raise a {class}`~subgrounds.pagination.strategies.SkipPagination` exception.

The class's `step` method is where the main logic of the pagination strategy is located. The method accepts a single argument, `page_data` which is a dictionary containing the response data of the previous query (i.e.: the previous page of data). The `step` method should return a tuple `(doc, vars)`, where `doc` is a {class}`~subgrounds.query.Document` representing the query to be made to fetch the next page of data. When pagination is over (e.g.: when all pages of data have been fetched), the `step` method should raise a {class}`~subgrounds.pagination.strategies.StopPagination` exception.

Below is the algorithm used by {class}`~subgrounds.Subgrounds` to paginate over a query document given a pagination strategy:

```{code-include}
:link-at-bottom:
:link-to-documentation:

:func:`subgrounds.pagination.pagination.paginate`
```
