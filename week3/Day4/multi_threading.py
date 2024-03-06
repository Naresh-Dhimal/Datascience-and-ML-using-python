import requests
from timer import timer
from concurrent.futures import ThreadPoolExecutor

URL = "https://httpbin.org/uuid"

def fetch_uuid(session, url):
    with session.get(URL) as response:
        print(response.json()['uuid'])



@timer(1,5)

def main():
    with ThreadPoolExecutor(max_workers=100) as executer:
        with requests.Session() as session:
            executer.map(fetch_uuid,[session]*100, [URL]*100)
            executer.shutdown(wait=True)
