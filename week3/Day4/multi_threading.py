import requests
from thread_timer import timer
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

URL = "https://httpbin.org/uuid"

def fetch_uuid(session, url):
    with session.get(URL) as response:
        print(response.json()['uuid'])



@timer(1,5)

def main():
    with ProcessPoolExecutor(max_workers=61) as executer:
        with requests.Session() as session:
            executer.map(fetch_uuid,[session]*100, [URL]*100)
            executer.shutdown(wait=True)
