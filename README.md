# Pokemon-API

![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/825422342938820618/unknown.png)

## Tabela de conteúdos

<!--ts-->
   * [About](#about)
   * [Requirements](#requirements)
   * [How to use](#how-to-use)
      * [API Routes](#routes)
      * [Setting up Program](#program-setup)
      * [Response Object](#object)
   * [Technologies](#technologies)
<!--te-->

## About

A simple API built using python made by Bruno Dantas.

This project was used to learn a little about flask and improve my python skills. The idea is to access some pokemon pages and join the informations in a single object.

## Requirements

To run this repository by yourself you will need to install python3 in your machine and them install all the requirements inside the [requirements](requirements.txt) file

## How to use

### Routes

- *'/':* This route gets every pokemon information (actually there are about 900, according the pokemon main page).
- *'/<pokemon_name>':* This route, you need to pass a argument that's the pokemon name that you're looking for.

### Program Setup

```bash
# Clone this repository
$ git clone <https://github.com/DantasB/Pokemon-API>

# Access the project page on your terminal
$ cd Pokemon-API

# Install all the requirements
$ pip install -r requirements.txt

# Create a .env file
$ touch .env  

# Create the following parameters
 DEBUG #If the API is on debug mode or not, should be True or False

# Execute the main program
$ python api.py

# Them it's just wait for the code run and access the api local url
```
![demonstration](https://cdn.discordapp.com/attachments/539836343094870016/825919295947145236/unknown.png)

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


## Technologies

* Python3
* Flask
* Aiohttp


If you still need help in how to run this project or doubts about flask and python, fell free to contact me on discord: BDantas#3692