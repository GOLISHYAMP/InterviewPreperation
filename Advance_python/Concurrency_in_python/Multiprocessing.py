# from multiprocessing import Process
# import time

# def func(id):
#     time.sleep(1)
#     print(f"{id} function is running")

# if __name__ == "__main__":
#     start = time.time()
#     for i in range(10):
#         process = []
#         p = Process(target=func, args=(i,))
#         process.append(p)
#         p.start()

#     for p in process:
#         p.join()
#     print("all work done in : ",time.time()-start)


#####################################################################################

# from multiprocessing import Process, Queue
# import time

# def producer(queue):
#     for i in range(5):
#         time.sleep(0.5)
#         print(f"produced item-{i}")
#         queue.put(f"Item {i}")
#     queue.put(None)  # Sentinel to indicate completion

# def consumer(queue):
#     while True:
#         time.sleep(0.75)
#         item = queue.get()
#         if item is None:
#             break
#         print(f"Consumed {item}")

# if __name__ == "__main__":
#     queue = Queue()
#     p1 = Process(target=producer, args=(queue,))
#     p2 = Process(target=consumer, args=(queue,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
######################################################################

# from multiprocessing import Process, Pipe
# import time

# def sender(conn):
#     conn.send("Hello from Sender!")
#     message = conn.recv()
#     print('message recieved at sender process : ',message)
#     # conn.close()

# def receiver(conn):
#     message = conn.recv()
#     print(f"Received: {message}")
#     conn.send("Hii from the receiver")


# if __name__ == "__main__":
#     conn1, conn2 = Pipe()
#     p1 = Process(target=sender, args=(conn1,))
#     p2 = Process(target=receiver, args=(conn2,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

################################################################

# from multiprocessing import Process, Value
# import time

# def increment(shared_value):
#     for _ in range(1000):
#         shared_value.value += 1

# if __name__ == "__main__":
#     shared_value = Value('i', 0)  # 'i' indicates integer type
#     processes = [Process(target=increment, args=(shared_value,)) for _ in range(4)]
    
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()

#     print(f"Final Value: {shared_value.value}")

############################################################


# from multiprocessing import Process, Array

# def square_elements(shared_array, k):
#     for i in range(len(shared_array)):
#         shared_array[i] = shared_array[i] ** k

# if __name__ == "__main__":
#     shared_array = Array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 'i' indicates integer type
#     p1 = Process(target=square_elements, args=(shared_array,2))
#     p2 = Process(target=square_elements, args=(shared_array,3))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     print("Updated Array:", list(shared_array))


###########################################################################

# from multiprocessing import Pool

# def square(x):
#     return x * x

# if __name__ == "__main__":
#     # data = [1, 2, 3, 4, 5]
#     with Pool(processes=4) as p:
#         results = p.map(square, data)
#         # results = p.apply(square, args=(5, ))
#     print(results)

###############################################################################

# from multiprocessing import Process, Lock

# def critical_section(lock, task_id):
#     # with lock:  # Automatically acquires and releases the lock
#     print(f"Task {task_id} entering critical section")
#     print(f"Task {task_id} leaving critical section")

# if __name__ == "__main__":
#     lock = Lock()
#     processes = [Process(target=critical_section, args=(lock, i)) for i in range(4)]

#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()


################################################################################

# from multiprocessing import Process, Manager

# def update_shared_list(shared_list, value):
#     shared_list.append(value)

# if __name__ == "__main__":
#     with Manager() as manager:
#         shared_list = manager.list()  # Shared list
#         processes = [Process(target=update_shared_list, args=(shared_list, i)) for i in range(5)]

#         for p in processes:
#             p.start()
#         for p in processes:
#             p.join()

#         print("Updated shared list:", list(shared_list))

################################################################################

# from multiprocessing import Process
# import time

# def infinite_loop():
#     while True:
#         print("Running...")
#         time.sleep(1)

# if __name__ == "__main__":
#     p = Process(target=infinite_loop)
#     p.start()
#     time.sleep(5)  # Let the process run for 5 seconds
#     p.terminate()  # Terminate the process
#     print("Process terminated")


#################################################################


# from multiprocessing import Pool

# def divide(x, y):
#     return x / y

# if __name__ == "__main__":
#     with Pool(processes=4) as pool:
#         results = pool.apply_async(divide, args=(1, 0))
#         try:
#             print(results.get())  # This will raise a ZeroDivisionError
#         except ZeroDivisionError as e:
#             print(f"Caught exception: {e}")

# from multiprocessing import Process, Value
# import time

# def increment(shared_value):
#     # for _ in range(1000):
#     shared_value.value += 1

# if __name__ == "__main__":
#     shared_value = Value('i', 0)  # 'i' indicates integer type
#     processes = [Process(target=increment, args=(shared_value,)) for _ in range(4)]
    
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()

#     print(f"Final Value: {shared_value.value}")


##################################################################
from concurrent.futures import ThreadPoolExecutor
import time
def func(i):
    for i in range(100):
        i += 1
    return i

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = executor.map(func, range(10))
    time.sleep(5)
    # results = [future.result() for future in futures]
print(futures)