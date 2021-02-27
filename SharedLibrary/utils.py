import re

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_all_line_breakers(text):
    clean = re.compile("\s+")
    return re.sub(clean, ' ', text)

def change_response_to_utf8(Response, json, pokemon):
    json_string = json.dumps(pokemon.serialize(), ensure_ascii=False)
    response    = Response(json_string, content_type="application/json; charset=utf-8")
    return response   