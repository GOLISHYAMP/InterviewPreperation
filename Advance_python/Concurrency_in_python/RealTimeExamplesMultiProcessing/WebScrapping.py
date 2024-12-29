#While multithreading can be used for I/O-bound scraping, 
# multiprocessing is suitable when significant processing 
# is required after fetching the data.

from multiprocessing import Pool
import requests, time

def fetch_and_analyze(url):
    response = requests.get(url)
    return len(response.text)  # Analyze the response content

if __name__ == "__main__":
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    start = time.time()
    with Pool(processes=3) as pool:
        results = pool.map(fetch_and_analyze, urls)
    print(sum(results))
    print('time took : ', time.time() -  start)

    # sum = 0
    # for url in urls:
    #     sum += fetch_and_analyze(url)
    # print(sum)
