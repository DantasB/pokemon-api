import asyncio
import json
from flask import Flask, jsonify, Response
from SharedLibrary import *
from Objects import *

app = Flask(__name__)

loop = asyncio.get_event_loop()

def get_pokemon_list():
    pokemon_json = loop.run_until_complete(crawler.PokemonCrawler().get_pokemon_json("https://www.pokemon.com/br/api/pokedex/kalos"))
    pokemon_list = pokemon.Pokemon.fill_object_with_json(json.loads(pokemon_json.decode()))
    return pokemon_list

def change_response_to_utf8(pokemon):
    json_string = json.dumps(pokemon.serialize(), ensure_ascii=False)
    response    = Response(json_string, content_type="application/json; charset=utf-8")
    return response

def parse_extra_information(pokemon):
        pokemon_html = loop.run_until_complete(crawler.PokemonCrawler().get_pokemon_page("https://pokemondb.net/pokedex/" + pokemon.name))
        parser.get_extra_informations(pokemon, pokemon_html)

@app.route('/')
def hello():
    pokemon_list = get_pokemon_list()
    for pokemon in pokemon_list:
        parse_extra_information(pokemon)
        print(f"[Debug] All informations and extra informations for {pokemon.name} were captured")

        return change_response_to_utf8(pokemon)


if __name__ == "__main__":
    app.run(debug=True)