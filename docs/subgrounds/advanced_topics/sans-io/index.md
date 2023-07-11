# {bdg-success-line}`NEW` Sans-IO

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.7.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

In the process of introducing [async](/subgrounds/getting_started/async) querying to `Subgrounds`, a large amount of refactoring was needed to reduce code duplication. We decided to embrace the technique of [sans-io](https://sans-io.readthedocs.io/), a methodology to decouple the libraries' buisness logic from "IO" logic (making and sending requests).

The result of this work has led us to the {mod}`subgrounds.client` subpackage and the {class}`~subgrounds.client.SubgroundsBase` class as an access point to all the logic encapsulated by `subgrounds`. We've implemented two clients as apart of the `subgrounds` package: {class}`~subgrounds.Subgrounds` and {class}`~subgrounds.AsyncSubgrounds` — leveraging [`httpx`](https://www.python-httpx.org/) to actually make requests.

Alternatively, you can subclass {class}`~subgrounds.client.SubgroundsBase` (or even {class}`~subgrounds.Subgrounds` / {class}`~subgrounds.AsyncSubgrounds`) and implement your own choice of requests library (`requests`, `aiohttp`, etc.) with 10 lines of code — `Subgrounds` is completely unentangled with the IO.

```{toctree}
:caption: Sans-IO
:hidden:

custom
```
