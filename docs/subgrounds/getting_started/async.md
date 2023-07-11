# {bdg-success-line}`NEW` Async

```{article-info}
:avatar-outline: muted
:author: "*New in version `1.7.0`*"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1 sd-text-muted
```

## The World of Async

Asynchronous programming in python allows us to **concurrently** perform operations. In the context of `Subgrounds`, it allows us to perform multiple queries at the same time -- we won't need to wait for 1 query to finish before producing another one.

```{code-block} python
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

```{thebe-button}
```

```{code-block} python
:caption: Making queries with async

from subgrounds import AsyncSubgrounds

sg = AsyncSubgrounds()

curve = await sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/convex-community/volume-mainnet")

await sg.query_df(curve.Query.pools)
await sg.query_df(curve.Query.candles)
```

Unfortuntely, making a secondary query here would *not* automatically parallelize the queries — we need to use [`tasks`](https://docs.python.org/3.11/library/asyncio-task.html).

```{code-block} python
:caption: An example of making two queries **concurrently** (and timing them)

import asyncio
import time

task1 = asyncio.create_task(
    sg.query_df(curve.Query.pools)
)

task2 = asyncio.create_task(
    sg.query_df(curve.Query.candles)
)

print(f"started at {time.strftime('%X')}")

asyncio.gather([task1, task2])

print(f"finished at {time.strftime('%X')}")

print(task1.result())
print(task2.result())
```

:::{hint}
If you are using Python 3.11 or higher, you can leverage a newer async api called {class}`TaskGroups <asyncio.TaskGroup>` alongside {doc}`query grouping <querying/grouping>`:

```{code-block} python

from asyncio import TaskGroup

with (sg, TaskGroup() as tg):
    tasks = [
        tg.create_task(
            sg.query_df(curve.Query.pools)
        ),
        tg.create_task(
            sg.query_df(curve.Query.candles)
        ),
    ]

for task in tasks:
    print(task.result())
```
:::
