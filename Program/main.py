import aiohttp

class PokemonCrawler():
    def __init__(self, proxy=None):
        self.proxy = proxy
    
    async def get_pokemon_json(self, url):
        try:
            async with session.get(url, headers=self.set_headers(headers), proxy=self.set_proxy(proxy), params=params, timeout=timeout) as r:
                print (r.status)
                if r.status == 200:
                    obj = await r.read()
                    array.append(obj)
                    break
        except:
            pass
        return array