import asyncio
from typing import Union
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    pkmn1 = requests.get("https://pokeapi.co/api/v2/pokemon/1").json()
    pkmn2 = requests.get("https://pokeapi.co/api/v2/pokemon/2").json()
    pkmn3 = requests.get("https://pokeapi.co/api/v2/pokemon/3").json()
    pkmn4 = requests.get("https://pokeapi.co/api/v2/pokemon/4").json()
    pkmn5 = requests.get("https://pokeapi.co/api/v2/pokemon/5").json()
    pkmn6 = requests.get("https://pokeapi.co/api/v2/pokemon/6").json()
    pkmn7 = requests.get("https://pokeapi.co/api/v2/pokemon/7").json()
    pkmn8 = requests.get("https://pokeapi.co/api/v2/pokemon/8").json()
    pkmn9 = requests.get("https://pokeapi.co/api/v2/pokemon/9").json()
    pkmn10 = requests.get("https://pokeapi.co/api/v2/pokemon/10").json()
    response = [pkmn1, pkmn2, pkmn3, pkmn4, pkmn5, pkmn6, pkmn7, pkmn8, pkmn9, pkmn10]
    return response


@app.get("/{page}")
async def read_root(page: int):
    page = page * 10
    pkmn1 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(1 + page)).json()
    pkmn2 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(2 + page)).json()
    pkmn3 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(3 + page)).json()
    pkmn4 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(4 + page)).json()
    pkmn5 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(5 + page)).json()
    pkmn6 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(6 + page)).json()
    pkmn7 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(7 + page)).json()
    pkmn8 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(8 + page)).json()
    pkmn9 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(9 + page)).json()
    pkmn10 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(10 + page)).json()
    response = [pkmn1, pkmn2, pkmn3, pkmn4, pkmn5, pkmn6, pkmn7, pkmn8, pkmn9, pkmn10]
    return response


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
#
# asyncio.run(main())
