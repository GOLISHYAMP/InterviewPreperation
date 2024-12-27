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
#     for _ in range(5):
#         time.sleep(0.5)
#         conn.send("Hello from Sender!")
#         message = conn.recv()
#         print('message recieved at sender process : ',message)
#     # conn.close()

# def receiver(conn):
#     for _ in range(5):
#         time.sleep(0.75)
#         message = conn.recv()
#         print(f"Received: {message}")
#         conn.send("Hii from the receiver")


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
#     shared_array = Array('i', [1, 2, 3, 4, 5])  # 'i' indicates integer type
#     p1 = Process(target=square_elements, args=(shared_array,2))
#     p2 = Process(target=square_elements, args=(shared_array,3))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     print("Updated Array:", list(shared_array))


###########################################################################

from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    with Pool(processes=4) as p:
        results = p.map(square, data)
    print(results)