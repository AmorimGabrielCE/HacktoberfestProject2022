import random
import requests
from PIL import Image

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

def choose_your_pokemon(name):
    name.lower()
    if name == "charmander":
        image = Image.open('src\images\\charmander.png')
        image.show()    
    elif name == "squirtle":
        image = Image.open('src\images\\squirtle.png')
        image.show()
    elif name == "bulbasaur":
        image = Image.open("src\images\\bulbasaur.png")
        image.show()

print("\nWelcome to Guess Pokemon Game!\n")
print("Game number pokemon: 1 - Chosse your pokemon: 2")
game_mode = int(input("Choose which game mode you want "))
if game_mode == 1:
    user_guess = input(f"\nCan you guess what's pokemon number {random_number}?\n")
    Get_Result(user_guess)
elif game_mode == 2: 
    print("Choose your starter pokemon: ")
    user_guess = str(input("Charmander,Bulbasaur or Squirtle ? "))
    choose_your_pokemon(user_guess)
else: 
    print("invalid option, retry")
    game_mode = int(input("Choose which game mode you want "))