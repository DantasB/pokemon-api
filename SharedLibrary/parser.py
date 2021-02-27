import asyncio

from Objects import *
from scrapy import Selector

from SharedLibrary import utils

def get_each_stat(pokemon, data):
    if("Sp." in data[0]):
        pokemon.set_base_stats(data[0] + data[1], data[2])
        pokemon.set_max_stats(data[0] + data[1], data[4])
        return
    
    pokemon.set_base_stats(data[0], data[1])
    pokemon.set_max_stats(data[0], data[3])

def get_extra_informations(pokemon, html_content):
    html_document = Selector(text=html_content)
    get_pokemon_weight(pokemon, html_document.xpath("/html/body/main/div[3]/div[2]/div/div[1]/div[2]/table/tbody/tr[5]/td").extract_first())
    get_pokemon_base_stats(pokemon, html_document.xpath("/html/body/main/div[3]/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr").extract())
    get_pokemon_pokedex_entries(pokemon, html_document.xpath("/html/body/main/div[8]/table/tbody/tr").extract())
    get_pokemon_species(pokemon, html_document.xpath("/html/body/main/div[3]/div[2]/div/div[1]/div[2]/table/tbody/tr[3]/td").extract_first())
    get_pokemon_local_numbers(pokemon, html_document.xpath("/html/body/main/div[3]/div[2]/div/div[1]/div[2]/table/tbody/tr[7]/td").extract_first())

def get_pokemon_weight(pokemon, information):
    if information is None:
        return   
    weight = utils.remove_html_tags(information).strip()
    pokemon.set_weight(weight)

def get_pokemon_base_stats(pokemon, informations):
    for information in informations:
        information = utils.remove_all_line_breakers(utils.remove_html_tags(information)).strip().split(' ')
        get_each_stat(pokemon, information)

def get_pokemon_pokedex_entries(pokemon, informations):
    for information in informations:
        information = utils.remove_html_tags(information).strip().split(" ", 1)
        pokemon.set_pokedex_entries(information[0], information[1])

def get_pokemon_species(pokemon, information):
    if information is None:
        return   
    species = utils.remove_html_tags(information).strip()
    pokemon.set_species(species)

def get_pokemon_local_numbers(pokemon, informations):
    informations = utils.remove_html_tags(informations).strip().split(')')
    informations = informations[:len(informations)-1]
    for information in informations:
        information = information.split('(')
        pokemon.set_local_numbers(information[1].strip(), information[0].strip())