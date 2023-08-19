import requests
import pytest 

token ='1d1d97ad9393b319bfbc2e4789e6336a'  #токен аторизации
host = 'https://api.pokemonbattle.me:9104' #хост прода покемонов

def test_status_code():
    response =  requests.get(f'{host}/trainers', params={ "trainer_id" : 2028})
    assert response.status_code == 200
def test_name():
    response =  requests.get(f'{host}/trainers', params={ "trainer_id" : 2028})
    assert response.json()['trainer_name'] == 'EWqwE'