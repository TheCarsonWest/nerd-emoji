## [[Multiprocessing]] in Python

### Explanation
 [[Multiprocessing]] provides a way to create multiple processes, each of which can run concurrently to perform different tasks. It is a more advanced form of parallelism than multithreading, which operates on a single processor. [[Multiprocessing]] allows different tasks to be executed in parallel on different CPUs, improving the overall speed of execution.

### How to Use [[Multiprocessing]]
To use multiprocessing in Python, you need to create a `Process` object for each task, and then start the process by calling the `start()` method. The `Process` object has the following attributes and methods:

- `target`: The function to be executed by the process.
- `name`: The name of the process (optional).
- `args`: A tuple of arguments to be passed to the target function.
- `kwargs`: A dictionary of keyword arguments to be passed to the target function.
- `start()`: Starts the process.
- `join()`: Waits for the process to finish and returns the result.

### Code Examples
```python
import multiprocessing

def worker(num):
 """thread worker function"""
 print(f'Worker: {num}')

if __name__ == '__main__':
 jobs = []
 for i in range(5):
 p = multiprocessing.Process(target=worker, args=(i,))
 jobs.append(p)
 p.start()
 for j in jobs:
 j.join()
```

### Related Python Concepts
- [[Concurrency and Multithreading]]: [[Multiprocessing]] is an extension of multithreading that allows processes to run on different CPUs.
- [[Functions]]: [[Multiprocessing]] uses functions as targets for processes to execute.
- [[Function Parameters]]: Arguments and keyword arguments can be passed to target functions in multiprocessing.
- [[Return Values]]: The `join()` method of a `Process` object can be used to retrieve the return value of the target function.
- [[Threading]]: Multithreading is another way of achieving concurrency in Python, but it operates on a single CPU.
# [[Python 1 Home]]