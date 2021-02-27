import asyncio

import re
import json
from Objects import *
from scrapy import Selector


crawler = crawler.PokemonCrawler()

def get_each_stat(pokemon, data):
    content = data.strip().split(' ')
    if("Sp." in content[0]):
        pokemon.set_base_stats(content[0] + content[1], content[2])
        pokemon.set_max_stats(content[0] + content[1], content[4])
        return
    
    pokemon.set_base_stats(content[0], content[1])
    pokemon.set_max_stats(content[0], content[3])

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_all_line_brakers(text):
    clean = re.compile("\s+")
    return re.sub(clean, ' ', text)

def get_extra_informations(pokemon, html_content):
    html_document = Selector(text=html_content)
    get_pokemon_weight(pokemon, html_document.xpath("/html/body/main/div[3]/div[2]/div/div[1]/div[2]/table/tbody/tr[5]/td").extract_first())
    get_pokemon_base_stats(pokemon, html_document.xpath("/html/body/main/div[3]/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr").extract())
    
def get_pokemon_weight(pokemon, information):
    if information is None:
        return   
    weight = remove_html_tags(information)
    pokemon.set_weight(weight)

def get_pokemon_base_stats(pokemon, informations):
    for information in informations:
        information = remove_all_line_brakers(remove_html_tags(information))
        get_each_stat(pokemon, information)


loop = asyncio.get_event_loop()
pokemon_json = loop.run_until_complete(crawler.get_pokemon_json("https://www.pokemon.com/br/api/pokedex/kalos"))
pokemon_list = pokemon.Pokemon.fill_object_with_json(json.loads(pokemon_json.decode()))

for pokemons in pokemon_list:
    pokemon_html = loop.run_until_complete(crawler.get_pokemon_page("https://pokemondb.net/pokedex/" + pokemons.name))
    get_extra_informations(pokemons, pokemon_html)

loop.close()
