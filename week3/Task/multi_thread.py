# importing libraries
import requests
from program_timer import program_time
from concurrent.futures import ProcessPoolExecutor

# defining URL
URL = "https://jsonplaceholder.typicode.com/comments" # url for json data of comments 

# fetch_email function
def fetch_email(session, url):
    with session.get(url) as response:
        print(response.json()[0]['email']) # extracting the email of random email index 0
    

# execution time measurement
@program_time(1,1)

def main():
    with ProcessPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch_email, [session] * 500, [URL] * 500)
            executor.shutdown(wait=True)