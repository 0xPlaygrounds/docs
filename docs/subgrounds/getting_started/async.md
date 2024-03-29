# {{ new_bdg }} Async

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.7.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

{{ thebe_button }}

## The World of Async

Asynchronous programming in python allows us to **concurrently** perform operations. In the context of `Subgrounds`, it allows us to perform multiple queries at the same time -- we won't need to wait for one query to finish before producing another one.

```{code-block} python
:class: thebe
:caption: An example of an async function which waits for 5 seconds.

import asyncio

async def my_async_function():
    await asyncio.sleep(5)
```

Since Python 3.5, functions can be defined with `async def` instead of `async` and statements can be preceded with an `await`. This allows python (and it's bundled async runtime, `asyncio`) to execute a different piece of code while waiting on a response back from a server.

```{note}
For more information on async programming in Python, see FastAPI's [concurrent burgers](https://fastapi.tiangolo.com/async/) article.
```

```{hint}
While working with `async` in python, it can be helpful to have an active async environment. An easy way to do so, is to run your code in a:

- [`python -m asyncio`](https://docs.python.org/3.11/library/asyncio.html#module-asyncio) shell
- An [`IPython`](https://ipython.readthedocs.io/en/stable/) shell
- A [Jupyter](https://jupyter.org) notebook server
  - *The executable cells in these docs are using a notebook server in the background*

This allows you to use `await` at the top-most level. Otherwise, `await` is only allowed **inside** an `async` function.
```

## {class}`~subgrounds.AsyncSubgrounds`

To leverage `async` within subgrounds, we will need to use an alternative client, {class}`~subgrounds.AsyncSubgrounds`.

```{code-block} python
:class: thebe
:caption: Making queries with async

from subgrounds import AsyncSubgrounds
import time

sg = AsyncSubgrounds()

curve = await sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/convex-community/volume-mainnet")

t0 = time.perf_counter()
pools = await sg.query_df(curve.Query.pools)
candles = await sg.query_df(curve.Query.candles)
t1 = time.perf_counter()

print(f"{t1-t0:0.2f}s elapsed")
```

Unfortuntely, making a secondary query here would *not* automatically parallelize the queries — we can use {py:func}`asyncio.gather` for this!

```{code-block} python
:class: thebe
:caption: An example of making two queries **concurrently** (and timing them)

import asyncio

t0 = time.perf_counter()
pools, candles = await asyncio.gather(
    sg.query_df(curve.Query.pools), 
    sg.query_df(curve.Query.candles),
)
t1 = time.perf_counter()

print(f"{t1-t0:0.2f}s elapsed")
```
