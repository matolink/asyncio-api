import asyncio
import aiohttp

from fastapi import FastAPI

app = FastAPI()


async def fetchPKMN(session, number):
    async with session.get(f'https://pokeapi.co/api/v2/pokemon/{number+1}') as request:
        if request.status != 200:
            request.raise_for_status()
        return await request.json()


async def fetchAllPKMN(session, pkmn_ids):
    tasks = []
    for pkmn_id in pkmn_ids:
        task = asyncio.create_task(fetchPKMN(session, pkmn_id))
        tasks.append(task)
    allPKMN = await asyncio.gather(*tasks)
    return allPKMN


async def noPage():
    pkmn_ids = list(range(10))
    async with aiohttp.ClientSession() as session:
        pkmns = await fetchAllPKMN(session, pkmn_ids)
        return pkmns


async def withPage(number: int):
    pkmn_ids = list(range(10))
    for i in range(len(pkmn_ids)):
        pkmn_ids[i] = pkmn_ids[i] + (number * 10)
    async with aiohttp.ClientSession() as session:
        pkmns = await fetchAllPKMN(session, pkmn_ids)
        return pkmns


@app.get("/")
async def read_root():
    return await noPage()


@app.get("/{page}")
async def pageRoute(page: int):
    return await withPage(page)
