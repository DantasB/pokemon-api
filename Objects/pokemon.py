import json


class Pokemon():
    """
    The object Pokemon relates to all pokemon basics information.

    Args:
        name (str): pokemon name
        abilities (list): list of pokemon abilities
        weakness (list): list of pokemon weakness
        national_number (int): number that acts like a pokemon id
        height (float): pokemon height
        image_url (str): pokemon image url
        types (list): list of pokemon types
    """

    def __init__(self, name: str, abilities: list, weakness: list, national_number: int, height: float, image_url: str, types: list) -> object:
        self.name = name
        self.national_number = national_number
        self.local_numbers = {}
        self.species = None
        self.height = height
        self.weight = None
        self.types = types
        self.abilities = abilities
        self.weakness = weakness
        self.base_stats = {}
        self.max_stats = {}
        self.pokedex_entries = {}
        self.image_url = image_url

    def set_weight(self, weight: float) -> None:
        if(weight is not None):
            self.weight = weight

    def set_base_stats(self, key: str, stats: str) -> None:
        if((key is not None) and (stats is not None)):
            self.base_stats[key] = stats

    def set_max_stats(self, key: str, stats: str) -> None:
        if((key is not None) and (stats is not None)):
            self.max_stats[key] = stats

    def set_pokedex_entries(self, game: str, text: str) -> None:
        if((game is not None) and (text is not None)):
            self.pokedex_entries[game] = text

    def set_species(self, species: list) -> None:
        if(species is not None):
            self.species = species

    def set_local_numbers(self, game: str, number: str) -> None:
        if((game is not None) and (number is not None)):
            self.local_numbers[game] = number

    def serialize(self) -> dict:
        """ We need to serialize the object before send it throught the api

        Returns:
            dict: the pokemon object serialized
        """
        return {"Name": self.name,
                "NationalNumber": self.national_number,
                "LocalNumber": self.local_numbers,
                "Species": self.species,
                "Height": self.height,
                "Weight": self.weight,
                "Types": self.types,
                "Abilities": self.abilities,
                "Weakness": self.weakness,
                "BaseStats": self.base_stats,
                "MaxStats": self.max_stats,
                "PokedexEntries": self.pokedex_entries,
                "ImageUrl": self.image_url}

    def __eq__(self, other_pokemon: object) -> bool:
        """ Instantiate an eq method that compares the pokemons national_number

        Args:
            other_pokemon (Pokemon) the pokemon object to be compared

        Returns:
            bool: return True if both pokemons have the same national_number
        """
        if(self.national_number == other_pokemon.national_number):
            return True
        return False

    def __repr__(self) -> str:
        return "Pokemon: {0}, Number: {1}".format(self.name, self.national_number)

    @classmethod
    def fill_object_with_json(cls, json: dict) -> list:
        """ A classmethod that generates Pokemon objects with the json informations

        Args:
            json (dict): a json that contains some pokemon informations

        Returns:
            list: a list containing Pokemon objects
        """
        pokemons = []
        for pokemon in json:
            try:
                pokemons.append(cls(pokemon['name'], pokemon['abilities'], pokemon['weakness'],
                                pokemon['number'], pokemon['height'], pokemon['ThumbnailImage'], pokemon['type']))
            except:
                raise
        print("All Pokemons are now Objects")
        return pokemons
