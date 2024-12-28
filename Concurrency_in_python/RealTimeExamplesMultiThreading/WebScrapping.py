# When scraping data from multiple web pages or APIs, 
# each request can run on a separate thread to speed up the process.
import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} with status {response.status_code}")

urls = [
    "https://example.com",
    "https://openai.com",
    "https://python.org"
]

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
