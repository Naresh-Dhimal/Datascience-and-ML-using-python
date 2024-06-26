import requests
from timer import timer

URL = "https://httpbin.org/uuid"


def fetch_uuid(session, url):
   with session.get(url) as response:
      print(response.json()['uuid'])

@timer(1,1)
def main():
    with requests.session() as session:
        for _ in range(100):
            fetch_uuid(session, URL)  