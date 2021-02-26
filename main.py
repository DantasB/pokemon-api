import asyncio

import json
from Objects import *


crawler = crawler.PokemonCrawler()

loop = asyncio.get_event_loop()
pokemon_json = loop.run_until_complete(crawler.get_pokemon_json("https://www.pokemon.com/br/api/pokedex/kalos"))
pokemon.Pokemon.fill_object_with_json(json.loads(pokemon_json.decode()))
loop.close()