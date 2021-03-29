import re
from typing import Callable


def remove_html_tags(text: str) -> str:
    """ Remove all html tags

    Args:
        text (str): the content that will have the html tags removed

    Returns:
        str: text withouth html tags
    """
    if(text is None):
        return

    clean = re.compile(r'<.*?>')
    return re.sub(clean, '', text)


def remove_all_line_breakers(text: str) -> str:
    """ Remove all line breakers

    Args:
        text (str): the content that will have the line breakers removed

    Returns:
        str: text withouth line breakers
    """
    clean = re.compile(r"\s+")
    return re.sub(clean, ' ', text)


def change_pokemon_to_utf8(Response: Callable, json: object, pokemon: object):
    """ Gets the pokemon object and changes it to utf-8

    Args:
        Response (function): function to generate a Response object (necessary to use on flask returns)
        json (class): function do generates a dump of the information
        pokemon (object): the pokemon that will have the information serialized

    Returns:
        response: the pokemon response
    """
    json_string = json.dumps(pokemon.serialize(), ensure_ascii=False)
    response = Response(
        json_string, content_type="application/json; charset=utf-8")
    return response


def change_pokemons_to_utf8(jsonify: Callable, pokemons: list) -> dict:
    """ Gets the pokemons list and changes it to a serialized object

    Args:
        jsonify (function): function do generates a serialized information
        pokemons (list): the pokemons that will have the information serialized

    Returns:
        dict: a dictionary containing all the serialized information
    """
    result = []
    for pokemon in pokemons:
        result.append(pokemon.serialize())

    return jsonify(result)
