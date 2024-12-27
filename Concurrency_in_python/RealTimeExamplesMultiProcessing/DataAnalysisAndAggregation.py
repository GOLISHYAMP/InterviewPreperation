from multiprocessing import Pool
import time
def compute_statistics(data_chunk):
    return sum(data_chunk) / len(data_chunk)

if __name__ == "__main__":
    data = [range(100000000000), range(10000000000, 2000000000), range(20000000000, 3000000000)]
    # with Pool(processes=4) as pool:
    #     averages = pool.map(compute_statistics, data)
    # print(averages)
    start = time.time()
    for dat in data:    
        print(compute_statistics(dat))
    print('time took : ',time.time() - start)