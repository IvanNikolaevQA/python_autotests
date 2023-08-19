import requests

token ='1d1d97ad9393b319bfbc2e4789e6336a'  #токен аторизации
host = 'https://api.pokemonbattle.me:9104' #хост прода покемонов

response_once = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers={'Conteny-type' : 'application/json' , 'trainer_token' : token }), 

response_edit = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6281",
    "name": "GabeN",
    "photo": "https://dolnikov.ru/pokemons/albums/111.png"
      }, headers= { 'Content-Type' : 'application/json' , "trainer_token" : token} )

response_add = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6281"
},headers={'Conteny-type' : 'application/json' , 'trainer_token' : token }) 

print(response_add.text)
print(response_edit.text)   