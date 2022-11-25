import asyncio
import aiohttp


async def fetchPKMN(request, number):
    async with request.get(f'https://pokeapi.co/api/v2/pokemon/{number+1}') as r:
        if r.status != 200:
            r.raise_for_status()
        return await r.json()


async def fetchAllPKMN(request, pkmn_ids):
    tasks = []
    for pkmn_id in pkmn_ids:
        task = asyncio.create_task(fetchPKMN(request, pkmn_id))
        tasks.append(task)
    allPKMN = await asyncio.gather(*tasks)
    return allPKMN


async def main():
    pkmn_ids = list(range(10))
    async with aiohttp.ClientSession() as request:
        pkmns = await fetchAllPKMN(request, pkmn_ids)
        print(pkmns)

asyncio.run(main())
