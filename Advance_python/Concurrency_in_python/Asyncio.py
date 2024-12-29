import asyncio
import time

# # Normal example
# async def say_hello():
#     print("Hello!")
#     await asyncio.sleep(1)
#     print("World!")

# async def main():
#     await say_hello()
#     print("all done")

# asyncio.run(main())  # This makes sure that the main coroutine is awaited.

###########################################################################
# #coroutines
# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("Done waiting")

# asyncio.run(main())

################################################################
# # Tasks
# async def func(id, sleep_time):
#     print(f"coroutine {id} executing")
#     await asyncio.sleep(sleep_time)
#     print(f'coroutine {id} done')

# async def main():
#     task1 = asyncio.create_task(func(1, 1))
#     task2 = asyncio.create_task(func(2, 3))
#     task3 = asyncio.create_task(func(3, 2))
#     await task1
#     await task2
#     await task3

# start = time.time()
# asyncio.run(main())
# print(time.time() - start)
# print("All tasks are done")

# Problem here is multiple create_task statements to be needed
# So to over come  this problem we come up with asyncio.gather()
############################################################################
# async def func(id, sleep_time):
#     print(f"coroutine {id} executing")
#     await asyncio.sleep(sleep_time)
#     print(f'coroutine {id} done')
#     return f"result of {id}"

# async def main():
#     results = await asyncio.gather(func(1,2), func(2,3), func(3,1))

#     for result in results:
#         print(f'Received Results : ', result) 

# asyncio.run(main())

# Problem with asyncio.gather is that if any of the coroutine has error
# it will halt all the coroutines causing problem to the overall workflow
# So, to overcome the problem of gather() we comeup with TaskGroup()
#########################################################################################
# TaskGroup doesnot need the await keyword to run the async functions

# async def func(id, sleep_time):
#     print(f"coroutine {id} executing")
#     await asyncio.sleep(sleep_time)
#     print(f'coroutine {id} done')
#     return f"result of {id}"

# async def main():
#     tasks = []
#     async with asyncio.TaskGroup() as tg:
#         for i, sleeptime in enumerate([1,2,3], 1):
#             task = tg.create_task(func(i, sleeptime))
#             tasks.append(task)

#     results = [task.result() for task in tasks]
#     for result in results:
#         print('Received Results : ', result)

# asyncio.run(main())

#################################################################################
# Future is just a another feature, which promises the result is coming soon.
# async def set_future_value(fut):
#     await asyncio.sleep(2)
#     fut.set_result("Future is done!")

# async def main():
#    future = asyncio.Future()
#    asyncio.create_task(set_future_value(future))
#    print(await future)

# asyncio.run(main())

##############################################################################
# Locking using the asyncio
# import Asyncio
# shared_resources = 0
# lock = asyncio.Lock()
# async def modify_shared_resources(id):
#     global shared_resources
#     async with lock:
#         print(f"Resources before modification : {shared_resources} by {id}")
#         shared_resources += 1
#         await asyncio.sleep(1)
#         print(f"Resources after modification : {shared_resources} by {id}")

# async def main():
#     await asyncio.gather(*(modify_shared_resources(i) for i in range(5)))

# asyncio.run(main())

#########################################################################
# Semaphore using asyncio 

# import Asyncio
# shared_resources = 0
# semaphore = asyncio.Semaphore(2)
# async def modify_shared_resources(id):
#     global shared_resources
#     async with semaphore:
#         print(f"Resources before modification : {shared_resources} by {id}")
#         shared_resources += 1
#         await asyncio.sleep(1)
#         print(f"Resources after modification : {shared_resources} by {id}")

# async def main():
#     await asyncio.gather(*(modify_shared_resources(i) for i in range(5)))

# asyncio.run(main())


###################################################################
# import asyncio
# async def waiter(event):
#     print('waiting for the event to be set')
#     await event.wait()
#     print('event has been set, continuing execution')

# async def setter(event):
#     await asyncio.sleep(2)
#     event.set()
#     print('Event has been set!')

# async def main():
#     event = asyncio.Event()
#     await asyncio.gather(waiter(event), setter(event))

# asyncio.run(main())