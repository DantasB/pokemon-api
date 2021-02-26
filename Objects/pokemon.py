class Pokemon():
    def __init__(self, name, abilities, weakness, number, height, image_url, types):
        self.name      = name
        self.abilities = abilities
        self.weakness  = weakness
        self.number    = number
        self.height    = height
        self.image_url = image_url
        self.types     = types

    @classmethod
    def fill_object_with_json(cls, json):
        pokemons = []
        for pokemon in json:
            try:
                pokemons.append(Pokemon(pokemon.name, pokemon.abilities, pokemon.weakness, pokemon.number, pokemon.height, pokemon.ThumbnailImage, pokemon.type))
            except:
                raise
            
        return pokemons
    