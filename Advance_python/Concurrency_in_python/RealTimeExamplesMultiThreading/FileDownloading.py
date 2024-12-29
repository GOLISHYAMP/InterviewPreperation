#Downloading multiple files simultaneously can be faster using threads,
#  especially if the server allows concurrent connections.

import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

urls = [
    ("https://example.com/file1", "file1.txt"),
    ("https://example.com/file2", "file2.txt")
]

threads = []
for url, filename in urls:
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
