# [[Async Generators]]
# [[Asyncio]] Notes

[[Asyncio]] is Python's built-in library for asynchronous programming.  It allows you to write concurrent code using the `async` and `await` keywords.  This is particularly useful for I/O-bound operations (like network requests or file operations) where you don't want your program to block while waiting for a response.

Key Concepts:

* **`async` and `await`:** These keywords are fundamental to asyncio.  `async` defines a coroutine function, and `await` pauses execution of the coroutine until a future (an object representing an ongoing operation) completes.

```python
import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)  # Simulate an I/O operation
    print("Coroutine finished")

async def main():
    await my_coroutine()

asyncio.run(main())
```

* **Event Loop:** The event loop is the heart of asyncio. It manages the execution of coroutines, switching between them as they wait for I/O operations to complete.  This allows for efficient concurrency without the overhead of threads.

* **Futures and Tasks:**  Futures represent the eventual result of an asynchronous operation.  Tasks are futures that are scheduled to run on the event loop.

```python
async def fetch_data():
    # Simulate fetching data from a network resource
    await asyncio.sleep(2)
    return "Data fetched!"

async def main():
    task = asyncio.create_task(fetch_data()) #schedule a task 
    print("Fetching data...")
    result = await task # wait for the task to complete
    print(f"Result: {result}")

asyncio.run(main())
```

* **Concurrency vs. Parallelism:**  [[Asyncio]] achieves concurrency (multiple tasks seemingly running at the same time), but not necessarily parallelism (multiple tasks running simultaneously on multiple CPU cores).  It's particularly efficient for I/O-bound operations where waiting dominates CPU usage. For CPU-bound operations, multiprocessing might be more appropriate. [[Concurrency vs Parallelism]]

* **[[Error Handling]]:**  Use `try...except` blocks within your coroutines to handle potential exceptions.

```python
async def might_fail():
    try:
        # some operation that might fail
        raise Exception("Something went wrong!")
    except Exception as e:
        print(f"Error: {e}")

async def main():
  await might_fail()
asyncio.run(main())
```


* **`asyncio.gather`:** This function runs multiple coroutines concurrently and returns their results in a list.

```python
async def coroutine1():
    await asyncio.sleep(1)
    return 1

async def coroutine2():
    await asyncio.sleep(2)
    return 2

async def main():
  results = await asyncio.gather(coroutine1(), coroutine2())
  print(f"Results: {results}")

asyncio.run(main())
```

[[Advanced Asyncio Techniques]]  [[Asyncio and Databases]] [[Asyncio and Web Servers]]
