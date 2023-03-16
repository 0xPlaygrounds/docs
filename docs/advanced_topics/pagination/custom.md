# Custom Strategies
Subgrounds allows developers to create their own pagination strategy by creating a class that implements the `PaginationStrategy` protocol:
```python
class PaginationStrategy(Protocol):
    def __init__(
        self,
        schema: SchemaMeta,
        document: Document
    ) -> None: ...

    def step(
        self,
        page_data: Optional[dict[str, Any]] = None
    ) -> Tuple[Document, dict[str, Any]]: ...
```

The class's constructor should accept a `SchemaMeta` argument which represents the schema of the subgraph API that the query is directed to and a `Document` argument which represents the query to be paginated on. If no pagination is required for the given document, then the constructor should raise a `SkipPagination` exception.

The class's `step` method is where the main logic of the pagination strategy is located. The method accepts a single argument, `page_data` which is a dictionary containing the response data of the previous query (i.e.: the previous page of data). The `step` method should return a tuple `(doc, vars)`, where `doc` is a `Document` representing the query to be made to fetch the next page of data. When pagination is over (e.g.: when all pages of data have been fetched), the `step` method should raise a `StopPagination` exception.

Below is the algorithm used by Subgrounds to paginate over a query document given a pagination strategy:
```python
def paginate(
    schema: SchemaMeta,
    doc: Document,
    pagination_strategy: Type[PaginationStrategy]
) -> dict[str, Any]:
    try:
        # Initialize the strategy
        strategy = pagination_strategy(schema, doc)

        data: dict[str, Any] = {}

        # Compute the query document and variables to get the first page of data
        next_page_doc, variables = strategy.step(page_data=None)

        while True:
            try:
                # Fetch a data page
                page_data = client.query(
                    url=next_page_doc.url,
                    query_str=next_page_doc.graphql,
                    variables=next_page_doc.variables | variables
                )

                # Merge the page with the data blob
                data = merge(data, page_data)

                # Compute the query document and variables to get the next page of data
                next_page_doc, variables = strategy.step(page_data=page_data)
            
            except StopPagination:
                break
            
            except Exception as exn:
                raise PaginationError(exn.args[0], strategy)

        return data

    except SkipPagination:
        # Excecute the query document as is if `SkipPagination` is raised
        return client.query(doc.url, doc.graphql, variables=doc.variables)
```
