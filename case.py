import base64
import requests

client_id = "6486c8e0c59741eeabf1c681451a0f55"
client_secret = "CHAVE DE ACESSO AQUI"

# Codifica a string "client_id:client_secret" no formato base64
base64_auth = base64.b64encode(f"{client_id}:{client_secret}".encode("ascii")).decode("ascii")

# Define os parâmetros da requisição
params = {
    "grant_type": "client_credentials"
}

# Define os headers da requisição
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {base64_auth}"
}

# Faz a requisição POST
response = requests.post("https://accounts.spotify.com/api/token", data=params, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == requests.codes.ok:
    # Define o token de acesso retornado pela API
    access_token = response.json()["access_token"] 
else:
    # Exibe o erro retornado pela API
    print("error")
    print(response.text)

# Defini a lista de artistas/ids
artists = {
    "Ed Sheeran" : "6eUKZXaKkcviH0Ku9w2n3V",
    "Queen": "1dfeR4HaWDbWqFHLkxsg1d",
    "Ariana Grande" : "66CXWjxzNUsdJxJ2JdwvnR",
    "Maroon 5" : "04gDigrS5kc9YWfZHwBETP", 
    "Imagine Dragons" : "53XhwfbYqKCa1cC15pYq2q",
    "Eminem": "7dGJo4pcD2V6oG8kP0tJRR",
    "Lady Gaga" : "1HY2Jd0NmPuamShAr6KMms",
    "Cold Play" : "4gzpq5DPGxSnKTe4SA8HAU",
    "Beyonce" : "6vWDO969PvNqNYHIOW5v0m",
    "Bruno Mars" : "0du5cEVh5yTK9QJze8zA0C",
    "Rihanna" : "5pKCCKE2ajJHZ9KAiaK11H",
    "Shakira" : "0EmeFodog0BfCgMzAIvKQp",
    "Justin Bieber" : "1uNFoZAHBGtllmzznpCI3s",
    "Demi Lovato" : "6S2OmqARrzebs0tKUEyXyp",
    "Taylor Swift" : "06HL4z0CvFAxyc27GXpf02"
}

# Definir o endpoint da API do Spotify
url = "https://api.spotify.com/v1/artists/"

followers_data = []
popularity_data = []

# Fazer uma requisição para cada artista/id
for artist, artist_id in artists.items():

    endpoint = f"https://api.spotify.com/v1/artists/{artist_id}"
     
    # Definir os cabeçalhos da requisição
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Fazer a requisição HTTP usando a biblioteca requests
    response = requests.get(endpoint, headers=headers)
    
    # Analisar os dados retornados
    if response.status_code == 200:
        data = response.json()
        # Pega o nome do artista e o respectivo numero de seguidores
        followers = {
            'artist_name': data["name"],
            'followers':str(data["followers"]["total"])
        }
        # Adiona em followers_data os dados selecionados
        followers_data.append(followers)
        # Pega o nome do artista e o respectivo indice de popularidade
        popularity = {
            'artist_name': data["name"],
            'popularity': str(data["popularity"])
        }
        # Adiona em popularity_data os dados selecionados
        popularity_data.append(popularity) 
    else:
        data = response.json()
        print(f"Erro ao buscar dados do artista {artist}: {response.status_code} : {data}") 

# Faz o ranking e pega os primeiros 7
sorted_followers_data_7 = sorted(followers_data, key=lambda x: x['followers'], reverse=True)[:7]
# Faz o ranking e pega os primeiros 5 
sorted_popularity_data_5 = sorted(popularity_data, key=lambda x: x['popularity'], reverse=True)[:5] 

# Coloca no formato pedido no case
my_case_resolution = {
'github_url' : 'https://github.com/CaioFaldoni/case_raccoon_se_automation.git',
'name' : 'Caio Dorta Faldoni',
'follower_ranking' : sorted_followers_data_7,
'popularty_ranking': sorted_popularity_data_5
}
