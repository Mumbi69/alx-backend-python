# Python - Async
* async and await Syntax:
> * async is used to define asynchronous functions (coroutines) in Python. An asynchronous function can be paused at certain points during its execution to allow other tasks to run.
> * await is used within an asynchronous function to pause the execution of the function until the awaited task completes. It is often used with functions that return awaitable objects, such as other coroutines, asyncio Futures, or other objects that follow the asynchronous protocol.
* How to Execute an Async Program with asyncio:
> * To run an asynchronous program, you can use the asyncio.run() function, introduced in Python 3.7. This function takes an asynchronous coroutine as its argument and runs it until it completes.
> * The asyncio.run() function is typically used in the if __name__ == "__main__": block to ensure it only runs when the script is executed directly.
* How to Create asyncio Tasks:
> * An asyncio task is a way to execute a coroutine asynchronously. You can create tasks using the asyncio.create_task() function.
> * Tasks are similar to Futures but provide a higher-level interface for managing and canceling coroutines. They are commonly used for concurrent execution of multiple coroutines.
* How to Use the random Module:
> * The random module in Python provides functions for generating pseudo-random numbers. You can use random.uniform(a, b) to generate a random float in the range [a, b).

