import asyncio
import requests
import aiohttp
from multi_proccessiny_timer import timer

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

URL = "https://httpbin.org/uuid"

async def fetch_uuid(session, url):
    with session.get(URL) as response:
        print(response.json()['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_uuid(session,URL) for _ in range(100)]
        await asyncio.gather(*tasks)
    
