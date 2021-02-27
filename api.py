import asyncio
import json
from flask import Flask, jsonify
from SharedLibrary import *
from Objects import *

app = Flask(__name__)

loop = asyncio.get_event_loop()

@app.route('/')
def hello():
    request = crawler.PokemonCrawler()
    pokemon_json = loop.run_until_complete(request.get_pokemon_json("https://www.pokemon.com/br/api/pokedex/kalos"))
    pokemon_list = pokemon.Pokemon.fill_object_with_json(json.loads(pokemon_json.decode()))
    for pokemons in pokemon_list:
        pokemon_html = loop.run_until_complete(request.get_pokemon_page("https://pokemondb.net/pokedex/" + pokemons.name))
        parser.get_extra_informations(pokemons, pokemon_html)
        print(f"[Debug] All informations and extra informations for {pokemons.name} were captured")
    return jsonify(pokemon_list)


if __name__ == "__main__":
    app.run(debug=True)