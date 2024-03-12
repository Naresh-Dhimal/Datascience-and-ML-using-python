import asyncio
import requests
import aiohttp
from multi_proccessiny_timer import timer

URL = "https://httpbin.org/uuid"

async def fetch_uuid(session, url):
   async with session.get(url) as response:
        json_data = await response.json()
        print(json_data['uuid'])


async def func():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_uuid(session,URL) for _ in range(100)]
        await asyncio.gather(*tasks)

@timer(1,1)
def main():
  asyncio.run(func())