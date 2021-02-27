import asyncio
import json
from flask import Flask, jsonify, Response
from SharedLibrary import *
from Objects.crawler import *
from Objects.pokemon import *

app = Flask(__name__)

loop = asyncio.get_event_loop()


@app.route('/')
def hello():
    pokemon_list = PokemonCrawler().get_pokemon_list(loop, PokemonCrawler().get_pokemon_json, Pokemon.fill_object_with_json, json)
    for pokemon in pokemon_list:
        parser.get_extra_informations(pokemon, PokemonCrawler().get_second_html(loop, PokemonCrawler().get_pokemon_json, "https://pokemondb.net/pokedex/" + pokemon.name))
        
        print(f"[Debug] All informations and extra informations for {pokemon.name} were captured")

        return utils.change_response_to_utf8(Response, json, pokemon)


if __name__ == "__main__":
    app.run(debug=True)