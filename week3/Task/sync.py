# importing libraries
import requests
from program_timer import program_time

# URL defining
URL = "https://jsonplaceholder.typicode.com/comments" # url for json data of comments 

# fetch_email function
def fetch_email(session, url):
    with session.get(url) as response:
        print(response.json()[0]['email']) # extracting the email of random email indexing 0

# execution time measurement
@program_time(1,1)

# main function
def main():
    with requests.Session() as session:
        for _ in range(500): # sending requests  for 500 times
            fetch_email(session, URL)