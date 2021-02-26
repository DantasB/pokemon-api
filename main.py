import asyncio
from Objects import *

crawler = crawler.PokemonCrawler()

loop = asyncio.get_event_loop()
loop.run_until_complete(crawler.get_pokemon_json("https://www.pokemon.com/br/api/pokedex/kalos"))
loop.close()