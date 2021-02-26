class Pokemon():
    def __init__(self, name, abilities, weakness, number, height, image_url, types):
        self.name      = name
        self.abilities = abilities
        self.weakness  = weakness
        self.number    = number
        self.height    = height
        self.image_url = image_url
        self.types     = types

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
        print("Success")
        return pokemons
    