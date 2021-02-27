import json

class Pokemon():

    def __init__(self, name, abilities, weakness, national_number, height, image_url, types):
        self.name            = name
        self.national_number = national_number
        self.local_numbers   = {}
        self.species         = None
        self.height          = height
        self.weight          = None
        self.types           = types
        self.abilities       = abilities
        self.weakness        = weakness
        self.base_stats      = {}
        self.max_stats       = {}
        self.pokedex_entries = {}
        self.image_url       = image_url

    def set_weight(self, weight):
        if(weight is not None):
            self.weight = weight

    def set_base_stats(self, key, stats):
        if((key is not None)and (stats is not None)):
            self.base_stats[key] = stats

    def set_max_stats(self, key, stats):
        if((key is not None)and (stats is not None)):
            self.max_stats[key] = stats

    def set_pokedex_entries(self, game, text):
        if((game is not None) and (text is not None)):
            self.pokedex_entries[game] = text

    def set_species(self, species):
        if(species is not None):
            self.species = species

    def set_local_numbers(self, game, number):
        if((game is not None) and (number is not None)):
            self.local_numbers[game] = number
    
    def serialize(self):
        return {"Name": self.name,
                "NationalNumber": self.national_number,
                "LocalNumber": self.local_numbers,
                "Species" : self.species,
                "Height": self.height,
                "Weight": self.weight,
                "Types": self.types,
                "Abilities": self.abilities,
                "Weakness": self.weakness,
                "BaseStats": self.base_stats,
                "MaxStats": self.max_stats,
                "PokedexEntries": self.pokedex_entries,
                "ImageUrl": self.image_url}

    def __eq__(self, other_pokemon):
        if(self.number == other_pokemon.number):
            return True
        return False

    def __repr__(self):
        return "Pokemon: {0}, Number: {1}".format(self.name, self.number)

    @classmethod
    def fill_object_with_json(cls, json):
        pokemons = []
        for pokemon in json:
            try:
                pokemons.append(cls(pokemon['name'], pokemon['abilities'], pokemon['weakness'], pokemon['number'], pokemon['height'], pokemon['ThumbnailImage'], pokemon['type']))
            except:
                raise
        print("All Pokemons are now Objects")
        return pokemons
    