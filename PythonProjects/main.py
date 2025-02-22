import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ТОКЕН'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "feim.aletka@yandex.ru",
    "password": "ecx593HgNzsjJ-v"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Буль",
    "photo_id": 547
}
body_edit_name = {
    "pokemon_id": "239330",
    "name": "New Буль",
    "photo_id": 547
}
body_add_pokeball = {
    "pokemon_id": "239295"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_edit_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit_name)
print(response_edit_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)



'''message = response_create.json()['message']
print(message)'''