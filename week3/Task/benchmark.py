from timeit import timeit

t1_multi_thread = timeit(
    """import requests
from program_timer import program_time
from concurrent.futures import ProcessPoolExecutor
URL = "https://jsonplaceholder.typicode.com/comments"  
def fetch_email(session, url):
    with session.get(url) as response:
        print(response.json()[0]['email']) 
def main():
    with ProcessPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch_email, [session] * 500, [URL] * 500)
            executor.shutdown(wait=True)""",
number=10000
)

t2_sync = timeit(
    """
import requests
from program_timer import program_time
URL = "https://jsonplaceholder.typicode.com/comments"  

def fetch_email(session, url):
    with session.get(url) as response:
        print(response.json()[0]['email']) 
def main():
    with requests.Session() as session:
        for _ in range(500): # sending requesting  for 100 times
            fetch_email(session, URL)""",
number=10000
)
print(f"multi_threading = {t1_multi_thread}")
print(f"Sync = {t2_sync}")