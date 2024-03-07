# from multiprocessing import Process
import requests
from multi_proccessiny_timer import timer
from multiprocessing import Pool, freeze_support


# print(multiprocessing.cpu_cunt())
URL = "https://httpbin.org/uuid"


def fetch_uuid(session, url):
   with session.get(url) as response:
      print(response.json()['uuid'])

@timer(1,1)
def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.map(fetch_uuid, [(session,URL) for _ in range(0,100)])

if __name__ == "__main__":
    freeze_support()
            
