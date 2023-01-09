# 0x01-python_async_function

In this project, I learned about:
+ async and await syntax
+ How to execute an async program with asyncio
+ How to run concurrent coroutines
+ How to create asyncio tasks
+ How to use the random module

## Tasks 
+ [0. The basics of async](https://github.com/Yosef-S-A/alx-backend-python/blob/main/0x01-python_async_function/0-basic_async_syntax.py):
   - Asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
+ [1. Let's execute multiple coroutines at the same time with async](https://github.com/Yosef-S-A/alx-backend-python/blob/main/0x01-python_async_function/1-concurrent_coroutines.py)
   - A Python script that run multiple coroutines from **Task 0** and return list of delay seconds.
 + [2. Measure the runtime](https://github.com/Yosef-S-A/alx-backend-python/blob/main/0x01-python_async_function/2-measure_runtime.py)
   - A Python script that measure the total time of exectuion of **Task 1** and return runtime per execution in seconds.
  + [3. Tasks](https://github.com/Yosef-S-A/alx-backend-python/blob/main/0x01-python_async_function/3-tasks.py)
     - A function that returns asyncio.Task
  + [4. Tasks](https://github.com/Yosef-S-A/alx-backend-python/blob/main/0x01-python_async_function/4-tasks.py)
     - A functio that return list of delay seconds using **Task 3** function
