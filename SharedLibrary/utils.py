import re

def remove_html_tags(text):
    """ Remove all html tags

    Args:
        text (string): the content that will have the html tags removed

    Returns:
        string: text withouth html tags
    """
    if(text is None):
        return
    
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_all_line_breakers(text):
    """ Remove all line breakers

    Args:
        text (string): the content that will have the line breakers removed

    Returns:
        string: text withouth line breakers
    """
    clean = re.compile("\s+")
    return re.sub(clean, ' ', text)

def change_pokemon_to_utf8(Response, json, pokemon):
    """ Gets the pokemon object and changes it to utf-8

    Args:
        Response (function): function to generate a Response object (necessary to use on flask returns)
        json (class): function do generates a dump of the information
        pokemon (object): the pokemon that will have the information serialized

    Returns:
        response: [description]
    """
    json_string = json.dumps(pokemon.serialize(), ensure_ascii=False)
    response    = Response(json_string, content_type="application/json; charset=utf-8")
    return response   

def change_pokemons_to_utf8(jsonify, pokemons):
    """ Gets the pokemons list and changes it to a serialized object

    Args:
        jsonify (function): function do generates a serialized information
        pokemons (list): the pokemons that will have the information serialized

    Returns:
        dictionary: a dictionary containing all the serialized information
    """
    result = []
    for pokemon in pokemons:
            result.append(pokemon.serialize())

    return jsonify(result)