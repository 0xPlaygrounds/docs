# {bdg-success-line}`NEW` Custom Clients

Implementing your own `Subgrounds` client only requires you to subclass {class}`~subgrounds.client.SubgroundsBase`.

```{note}
You can also choose to subclass {class}`~subgrounds.Subgrounds` or {class}`~subgrounds.AsyncSubgrounds` as they contain a more natural interface to work with, especially for simply swapping the implementation of the http client.
```

## Methodology

The {class}`~subgrounds.client.SubgroundsBase` class streamlines the all of the buisness logic neccessary to manage and make subgraph queries. Inheriting this class allows you to **purely** implement IO logic (making the actual request to the server). There's two main functions that allow you to 

{func}`~subgrounds.client.SubgroundsBase._load`
: This deals with caching and loading subgraph schema data. If subgraph data is successfully loaded from a cache, the actual request execution will be skipped (via a {class}`StopIteration` exception).

{func}`~subgrounds.client.SubgroundsBase._execute`
: This is the main entry point for executing queries via {class}`~subgrounds.query.DataRequest` and returning responses via {class}`~subgrounds.query.DataResponse`. Implementing `execute` allows you to 

Both of these methods are implemented as [**generators**](https://docs.python.org/3.11/tutorial/classes.html#generators) as they provide us the utilities to lazily produce and consume values. The buisness logic produces objects to send to IO functions and then data is sent back into the buisness logic to continually transform until finally returned.

```{dropdown} More on Generators
## *Wait, it's all generators?*

Yes! Generators in Python are quite fancy. While they are generally seen as an easier way to create iterators, they also have the ability to consume values. Generators are the backbone for {mod}`asyncio` in Python as the keywords `async` and `await` are merely syntatical sugar for various forms of `yield` statements.

## *How are you using it?*

We use generators via manually running `next()` and `.send()` functions to resume the generator state. Essentially, the buisness logic needs to step out and receive and send information to IO to compute. `yield` statements essentially allow us to "pause" the internal context while a different function implemented by a {class}`~subgrounds.client.SubgroundsBase` subclass to actually compute.

## *But why?*

The approach, known as [sans-io](https://sans-io.readthedocs.io/), we've chosen here has allowed us to reduce a large amount of code duplication when producing an `async` version of our API. It also disentangles the IO aspect of the library with the buisness logic allowing anyone to write in their own IO with very little work.

## *Where can I learn more?*

- [Basics on Sans-IO](https://sans-io.readthedocs.io/)
- [Generators as Pipelines](http://www.dabeaz.com/generators/)
- [Concurrency via Generators](http://www.dabeaz.com/coroutines/)
- [Generators beyond Iteration](http://www.dabeaz.com/finalgenerator/)
```

## Usage

Most implementations using these generators will match the following pattern:

```{code-block} python
:linenos:
:caption: "`next` and `.send` essentially wrap the IO work in `do_something` here"

try:
    my_generator = self.generator(...)

    values = next(my_generator)
    new_values = do_something(values)
    my_generator.send(new_values)

except StopIteration as e:
    return e.value
```

- `[#2]` - We instantiate our generator object
- `[#3-5]` - We produce a value, transform it, and send it back to the generator
- `[#1-8]` - Every thing is wrapped in a `try-except` to catch `StopIteration`:
- `[#9]` - `StopIteration.value` is our actual return value!

Alternatively, you can host a `while` loop if you have an unknown number of producing and consuming to do:

```{code-block} python
:linenos:
:caption: "Infinite generators, `.send` will also advance the generator like `next`."

try:
    my_generator = self.generator(...)

    values = next(my_generator)

    while True:
        new_values = do_something(values)
        values = my_generator.send(new_values)

except StopIteration as e:
    return e.value
```


### `load`
Here is an example for implementing `load` from {func}`Subgrounds.load <subgrounds.Subgrounds.load>`

```{code-include}
:link-at-bottom:
:link-to-documentation:

:func:`subgrounds.client.Subgrounds.load`
```

### `execute`
Here is an example for implementing `execute` from {func}`Subgrounds.execute <subgrounds.Subgrounds.execute>`

```{code-include}
:link-at-bottom:
:link-to-documentation:

:func:`subgrounds.client.Subgrounds.execute`
```
