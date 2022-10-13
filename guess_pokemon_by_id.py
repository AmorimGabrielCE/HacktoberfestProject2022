import random
import requests

random_number = random.randint(0, 151)

def Get_Random_Pokemon():
    first_generation = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
    first_generation = first_generation.json()
    random_pokemon = first_generation['results'][random_number - 1]['name']
    return random_pokemon

pokemon = Get_Random_Pokemon()

def Get_Result(text):
    text = text.lower()
    if(text == pokemon):
        print("\nYou're right, congratulations!\n")
    else:
        print("\nOh no! It's incorrect, sorry.\n")
        user_guess = input(f"\nCan you guess what's pokemon number {random_number}?\n")
        Get_Result(user_guess)

print("\nWelcome to Guess Pokemon Game!\n")
user_guess = input(f"\nCan you guess what's pokemon number {random_number}?\n")
Get_Result(user_guess)