import aiohttp


class PokemonCrawler():
    """
    The PokemonCrawler relates to all functions that access a pokemon website to get informations.
    """

    def __init__(self, proxy=None, timeout=120, headers=None):
        self.proxy   = proxy
        self.timeout = timeout
        self.headers = headers

    async def get_content(self, url):
        """ Gets the url html content if the status code is 200

        Args:
            url (string): the url to be crawlled

        Returns:
            bytes: the binary information containing the html content
        """
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=self.headers, proxy=self.proxy, timeout=self.timeout) as response:
                    if response.status == 200:
                        html_response = await response.read()
                        return html_response
            except:
                raise
            return ""

    def get_pokemon_list(self, loop, get_content, fill_object_with_json, json):
        """ An wrapper that gets the list of pokemon Objects filled with the json information

        Args:
            loop (object): asyncio object to run the async function
            get_content (function): function to access the url content
            fill_object_with_json (function): function that will generate the object with the json content
            json (class): json class used to load the json object

        Returns:
            list: a list containing Pokemon objects
        """
        pokemon_json = loop.run_until_complete(get_content("https://www.pokemon.com/br/api/pokedex/kalos"))
        pokemon_list = fill_object_with_json(json.loads(pokemon_json.decode()))
        return pokemon_list

    def get_second_html(self, loop, get_content, url):
        """ Access the url related to the specific pokemon

        Args:
            loop (object): asyncio object to run the async function
            get_content (function): function to access the url content
            url (string): pokemon url

        Returns:
            bytes: the binary information containing the html content
        """
        return loop.run_until_complete(get_content(url))
