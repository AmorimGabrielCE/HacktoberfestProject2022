import random
import requests
import pandas as pd

def random_number(min:int, max:int):
    number = random.randint(min, max-1)
    return number

def Get_Random_Pokemon():
    get_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    get_pokemon = get_pokemon.json()
    number= random_number(0,1154)
    random_pokemon = get_pokemon['results'][number]['name']
    return random_pokemon

def Get_Type_Pokemon():
    pokemon_type = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    pokemon_type = pokemon_type.json()
    Random_pokemon_type = pokemon_type['types'][0]['type']['name']
    return Random_pokemon_type

def Get_All_Types():
    types = requests.get(f"https://pokeapi.co/api/v2/type/")
    types = types.json()
    number_of_types = types['count']
    list_all_types = []

    for i in range(number_of_types):
        list_all_types.append(types['results'][i]['name'])

    return list_all_types

def Get_Result(option):
    if (type(option) is int):
        if option > 19 or option < 0:
            print('\n*** Choose an option in range correctly! ***')
            user_option = int(input(f"\nCan you guess what type this pokemon is?\n ---[ {pokemon} ]---\n\nOptions:\n{listTypes}\nSelect: "))
            Get_Result(user_option)
        elif(listTypes[0][int(option)] == pokemon_type):
            print("\nYou're right, congratulations!\n")
        else:
            print("\nOh no! It's incorrect, sorry.\nTry again!")
            user_option = int(input(f"\nCan you guess what type this pokemon is?\n ---[ {pokemon} ]---\n\nOptions:\n{listTypes}\nSelect: "))
            Get_Result(user_option)

listTypes = pd.DataFrame(Get_All_Types())
pokemon = Get_Random_Pokemon()
pokemon_type = Get_Type_Pokemon()

print("\nWelcome to Guess Pokemon Game!\n")
user_option = int(input(f"\nCan you guess what type this pokemon is?\n ---[ {pokemon} ]---\n\nOptions:\n{listTypes}\nSelect: "))
Get_Result(user_option)