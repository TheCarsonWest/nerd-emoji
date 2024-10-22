## Async [[Generators]]

### Definition

Async generators are special types of generators that can be used to lazily generate a sequence of values asynchronously. They allow for the creation of asynchronous iterators, making it possible to handle data asynchronously while maintaining the ability to iterate over the generated sequence.

### How to Use Async [[Generators]]

Async generators are defined using the `async def` syntax, similar to regular generators. They have a `yield` statement to produce each value in the sequence. However, they use the `async for` syntax to be iterated over asynchronously.

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

- [[Async [[Generators]]: Async generators use async iterators to produce values asynchronously.
- [[Coroutines]]: Async generators are closely related to coroutines, as they allow for asynchronous iteration over a sequence of values.
- [[Generators]]: Async generators extend the concept of generators by allowing for asynchronous iteration.
- [[Asyncio]]: Async generators are typically used in conjunction with the asyncio library for asynchronous I/O.
- [[Concurrence and Multithreading]]: Async generators can be used to achieve concurrency in Python applications.
# [[Python 1 Home]]