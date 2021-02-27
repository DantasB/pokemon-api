import re

def remove_html_tags(text):
    if(text is None):
        return
    
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_all_line_breakers(text):
    clean = re.compile("\s+")
    return re.sub(clean, ' ', text)

def change_pokemon_to_utf8(Response, json, pokemon):
    json_string = json.dumps(pokemon.serialize(), ensure_ascii=False)
    response    = Response(json_string, content_type="application/json; charset=utf-8")
    return response   

def change_pokemons_to_utf8(Pokemon, Response, jsonify, pokemons):
    result = []
    for pokemon in pokemons:
            result.append(pokemon.serialize())

    return jsonify(result)