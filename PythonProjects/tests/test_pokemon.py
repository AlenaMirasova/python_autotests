import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ТОКЕН'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18343'

'''def test_status_code():
  response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
  assert response.status_code == 200

def test_part_of_response():
  response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
  assert response_get.json()["data"][0]["name"] == 'Буль'
  
@pytest.mark.parametrize('key, value', [('name', 'Буль'), ('trainer_id', TRAINER_ID), ('id', '239299')])
def test_parametrize(key, value):
  response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
  assert response_parametrize.json()["data"][0][key] == value'''

def test_status_code_trainers():
  response_status_code_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
  assert response_status_code_trainers.status_code == 200

def test_name_trainer():
  response_name_trainer = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
  assert response_name_trainer.json()["data"][0]["trainer_name"] == 'Люци'