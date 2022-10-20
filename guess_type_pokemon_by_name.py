import random
import requests

def random_number(min:int, max:int):
    number = random.randint(min, max-1)
    return number

def Get_Random_Pikamon():
    first_generation = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    first_generation = first_generation.json()
    number= random_number(0,1154)
    random_pokemon = first_generation['results'][number]['name']
    return random_pokemon

pokemon = Get_Random_Pikamon()

print(pokemon)



def Get_Type_Pokemon():
    pokemon_type = requests.get(f"https://pokeapi.co/api/v2/pokemon/bulbasaur/")
    pokemon_type = pokemon_type.json()
    Random_pokemon_type = pokemon_type['types'][0]['type']['name']
    return Random_pokemon_type

print(Get_Type_Pokemon())

def Get_All_Types():
    types = requests.get(f"https://pokeapi.co/api/v2/type/")
    types = types.json()
    number_of_types = types['count']

    list_all_types = []
    for i in range(number_of_types):
        list_all_types.append(types['results'][i]['name'])

    for i in range(len(list_all_types)):
        print(f'{i+1} -- {list_all_types[i]}')

    return list_all_types

Get_All_Types()

#TODO Criar menu com todas as opções de tipos de pokemon
#Sair da pergunta somento quando o user acertar a pergunta
# Comparar tipo do pokemon com tipo do menu



# def Get_Result(text):
#     text = text.lower()
#     if(text == pokemon):
#         print("\nYou're right, congratulations!\n")
#     else:
#         print("\nOh no! It's incorrect, sorry.\n")
#         user_guess = input(f"\nCan you guess what's pokemon number {random_number}?\n")
#         Get_Result(user_guess)

# print("\nWelcome to Guess Pokemon Game!\n")
# user_guess = input(f"\nCan you guess what's pokemon number {random_number}?\n")
# Get_Result(user_guess)