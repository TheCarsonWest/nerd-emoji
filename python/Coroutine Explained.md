# [[Async Generators]]
# [[Coroutine Explained]] 
A coroutine is a specialized type of function that can be paused and resumed at various points.  Unlike regular functions which run to completion, coroutines can yield control back to the caller, and later resume execution from where they left off.  This is achieved using the `async` and `await` keywords (introduced in Python 3.5).

Key features:

* **`async def`:** Defines a coroutine function.  It's crucial to use this syntax to create a coroutine.  Regular functions won't work.

* **`await`:**  Used to pause execution of the coroutine until another coroutine (or asynchronous operation) completes.  It's important to note that `await` can only be used inside an `async def` function.


* **`yield`:** (In older approaches)  Could be used to pause and resume coroutines, but now largely superseded by `await`.


Example:

```python
import asyncio

async def my_coroutine(name):
    print(f"Coroutine {name} started")
    await asyncio.sleep([[1)  # Simulate some asynchronous operation
    print(f"Coroutine {name} finished")
    return f"Result from {name}"

async def main():
    coro1 = my_coroutine("A")
    coro2 = my_coroutine("B")

    result1 = await coro1
    result2 = await coro2

    print(f"Result [[1: {result1}")
    print(f"Result 2: {result2}")

if __name__ == "__main__":
    asyncio.run(main())
```

[[Asyncio Explained]]  This example uses `asyncio.sleep`, which is an asynchronous version of `time.sleep`.  The `asyncio` library is fundamental to working with coroutines effectively.  More details should be in [[Asyncio Explained]].

[[await Explained]]  Further explanation of the `await` keyword and its behaviour, particularly the implications of using it with different kinds of asynchronous objects is needed in [[await Explained]].

[[async def Explained]]  A more detailed examination of the `async def` syntax and its unique characteristics, such as how it interacts with other function types and decorators could go in [[async def Explained]].


Important points to remember:

* Coroutines are excellent for I/O-bound operations (network requests, file operations), where waiting doesn't block the entire program.
*  They enhance concurrency without needing multiple threads, making them more efficient in many cases.
*  Correctly using `async` and `await` is crucial for avoiding deadlocks and unexpected behaviour.
