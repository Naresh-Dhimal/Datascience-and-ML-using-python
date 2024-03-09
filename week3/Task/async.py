# importing libraries
import asyncio
import aiohttp
from program_timer import program_time

# defining URL
URL  = "https://jsonplaceholder.typicode.com/comments" # url for json data of comments

# fetch_email function
async def fetch_email(session, url):
    async with session.get(url) as response:
        json_data =  await response.json()
        print(json_data[0]['email']) # extracting the email of random email indexing 0

# func function to create session
async def func():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_email(session, URL) for _ in range(500)]
        await asyncio.gather(*tasks)

# execution time measurement
@program_time(1,1)

# main function
def main():
    asyncio.run(func())