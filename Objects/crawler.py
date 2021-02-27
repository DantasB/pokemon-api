import aiohttp


class PokemonCrawler():
    def __init__(self, proxy=None, timeout=120, headers=None):
        self.proxy   = proxy
        self.timeout = timeout
        self.headers = headers

    async def get_pokemon_json(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=self.headers, proxy=self.proxy, timeout=self.timeout) as response:
                    if response.status == 200:
                        json_content = await response.read()
                        return json_content
            except:
                raise
            return ""
    
    async def get_pokemon_page(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=self.headers, proxy=self.proxy, timeout=self.timeout) as response:
                    if response.status == 200:
                        html_content = await response.read()
                        return html_content
            except:
                raise
            return ""

    def get_pokemon_list(self, loop, get_pokemon_json, fill_object_with_json, json):
        pokemon_json = loop.run_until_complete(get_pokemon_json("https://www.pokemon.com/br/api/pokedex/kalos"))
        pokemon_list = fill_object_with_json(json.loads(pokemon_json.decode()))
        return pokemon_list

    def get_second_html(self, loop, get_pokemon_page, url):
        return loop.run_until_complete(get_pokemon_page(url))
