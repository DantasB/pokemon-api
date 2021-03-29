import os
from dotenv import load_dotenv, find_dotenv
import asyncio
import json
from flask import Flask, Response, jsonify
from SharedLibrary.parser import *
from SharedLibrary.utils import *
from Objects.crawler import *
from Objects.pokemon import *

app = Flask(__name__)

loop = asyncio.get_event_loop()


@app.route('/')
def get_all_pokemons() -> dict:
    """ This route receives no parameter, so it will return every pokemon information founded

    Returns:
        dict: a dictionary containing all the pokemons informations
    """
    pokemon_list = PokemonCrawler().get_pokemon_list(
        loop, PokemonCrawler().get_content, Pokemon.fill_object_with_json, json)
    pokemon_data = []
    for pokemon in pokemon_list:
        if(pokemon not in pokemon_data):
            get_extra_informations(pokemon, PokemonCrawler().get_second_html(
                loop, PokemonCrawler().get_content, "https://pokemondb.net/pokedex/" + pokemon.name))
            print(
                f"[Debug] All informations and extra informations for {pokemon.name} were captured")
            pokemon_data.append(pokemon)

    return change_pokemons_to_utf8(jsonify, pokemon_data)


@app.route('/<pokemon_name>')
def get_single_pokemon(pokemon_name: str) -> dict:
    """ This route receives no parameter, so it will return every pokemon information founded

    Args:
        pokemon_name (str): the pokemon to have the information returned

    Returns:
        dict: a dictionary containing the pokemon_name information
    """
    pokemon_list = PokemonCrawler().get_pokemon_list(
        loop, PokemonCrawler().get_content, Pokemon.fill_object_with_json, json)
    for pokemon in pokemon_list:
        if(pokemon.name.lower() != pokemon_name.lower()):
            continue

        get_extra_informations(pokemon, PokemonCrawler().get_second_html(
            loop, PokemonCrawler().get_pokemon_json, "https://pokemondb.net/pokedex/" + pokemon.name))

        print(
            f"[Debug] All informations and extra informations for {pokemon.name} were captured")
        return change_pokemon_to_utf8(Response, json, pokemon)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    debug = os.environ.get("DEBUG")
    app.run(debug=debug)
