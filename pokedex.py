import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_detail(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to get data {response.status_code}")

pokemon_name = "ditto"

pokemon_info = get_pokemon_detail(pokemon_name)

if pokemon_info:
    type = [t['type']['name'] for t in pokemon_info['types']]
    print(f"Id : {pokemon_info["id"]}")
    print(f"Name : {pokemon_info["name"]}")
    print(f"Typing : {','.join(type)}")
    print(f"Height : {pokemon_info["height"]}")
    print(f"Weigth : {pokemon_info["weight"]}")
    