# Pokemon API

A simple API built using python made by Bruno Dantas.

This project was used to learn a little about flask and improve my python skills. The idea is to access some pokemon pages and join the informations in a single object.


## Important 
The Pokemon is actually offline, but you can run this project in your machine.


### Setup
Setting up the Pokemon API is a no-brainer, just follow the guide below:
1. Download all the files.
2. Install all the libraries located at the [requirements.txt](requirements.txt);
4. Run the [api.py](https://github.com/DantasB/Pokemon-API/blob/main/api.py);

### Routes
- *'/':* This route gets every pokemon information (actually there are about 900, according the pokemon main page).
- *'/<pokemon_name>':* This route, you need to pass a argument that's the pokemon name that you're looking for.


### Object
The [pokemon object](https://github.com/DantasB/Pokemon-API/blob/main/Objects/pokemon.py) is the information that the api returns. The information returned by the api are:
- name (string)
- national_number (string)
- local_numbers (dictionary)
- species (string)
- height (float)
- weight (string)
- types (list)
- abilities (list)
- weakness (list)
- base_stats (dictionary)
- max_stats (dictionary)
- pokedex_entries (dictionary)
- image_url (string)




If you still need help in how to run this project or doubts about flask and python, fell free to contact me on discord: BDantas#3692
