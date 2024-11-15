## Async [[Generators]]

### Definition

Async [[Generators]] are special types of [[Generators]] that can be used to lazily generate a sequence of values asynchronously. They allow for the creation of asynchronous iterators, making it possible to handle data asynchronously while maintaining the ability to iterate over the generated sequence.

### How to Use Async [[Generators]]

Async [[Generators]] are defined using the `async def` syntax, similar to regular [[Generators]]. They have a `yield` statement to produce each value in the sequence. However, they use the `async for` syntax to be iterated over asynchronously.

```python
async def generate_numbers():
 for i in range(10):
 yield i
```

To iterate over an async generator asynchronously, use the `async for` syntax:

```python
async for number in generate_numbers():
 print(number)
```

### Code Examples

#### Generator Example

```python
async def generate_numbers():
 for i in range(10):
 await asyncio.sleep(1)
 yield i
```

#### Async For Example

```python
async def main():
 async for number in generate_numbers():
 print(number)
```

### Related Python Concepts

- [[Async [[Generators]]: Async [[Generators]] use async iterators to produce values asynchronously.
- [[Coroutines]]: Async [[Generators]] are closely related to [[Coroutines]], as they allow for asynchronous iteration over a sequence of values.
- [[Generators]]: Async [[Generators]] extend the concept of [[Generators]] by allowing for asynchronous iteration.
- [[Asyncio]]: Async [[Generators]] are typically used in conjunction with the asyncio library for asynchronous I/O.
- [[Concurrence and Multithreading]]: Async [[Generators]] can be used to achieve concurrency in Python applications.
# [[Python 1 Home]]