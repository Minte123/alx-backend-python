# 0x02-python_async_comprehension

+ [0. Async Generator](https://github.com/Yosef-S-A/alx-backend-python/tree/main/0x02-python_async_comprehension/0-async_generator.py)
  - Function that executes 10 times and randomly generate number between 0 and 10 while asynchronously wait 1 second each time
+ [1. Async Comprehensions](https://github.com/Yosef-S-A/alx-backend-python/tree/main/0x02-python_async_comprehension/1-async_comprehension.py)
  - Imports ```async_generator``` from the previous task and then write a coroutine called ```async_comprehension``` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers in a list.
+ [2. Run time for four parallel comprehensions](https://github.com/Yosef-S-A/alx-backend-python/tree/main/0x02-python_async_comprehension/2-measure_runtime.py)
  - Imports async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using ```asyncio.gather```. ```measure_runtime``` measures the total runtime and return it.
