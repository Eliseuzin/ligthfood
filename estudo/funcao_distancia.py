from flask import Flask
from dotenv import load_dotenv
#precisa instalar requests
import os, requests


load_dotenv()
app=Flask(__name__)

GOOGLE_MAPS_API_KEY=os.getenv('GOOGLE_MAPS_API_KEY')
ENDERECO_LOJA_HAMBURGUERIA = os.getenv('ENDERECO_LOJA_HAMBURGUERIA')

def obter_distancia(endereco_cliente):
    resposta= requests.get(
        "https://maps.googleapis.com/maps/api/distancematrix/json",
        params={
            "origins": endereco_cliente,
            "destinations": ENDERECO_LOJA_HAMBURGUERIA,
            "key": GOOGLE_MAPS_API_KEY,
            "language": "pt-BR",
            "units": "metric"
        }
    )

    dados=  resposta.json()
    elemento= dados["rows"][0]["elements"][0]

    return{
        "distancia": elemento["distance"]["text"],
        "duracao": elemento["duration"]["text"],
        "metros": elemento["distance"]["value"]
    }

def calcular_frete(distancia_metros):
    if distancia_metros <= 2000:
        return 6.00
    elif distancia_metros <= 3000:
        return 7.00
    elif distancia_metros <= 4000:
        return 8.00
    elif distancia_metros <= 5000:
        return 9.00
    elif distancia_metros <= 6000:
        return 10.00
    elif distancia_metros <= 7000:
        return 11.00
 
    excedente = distancia_metros - 7000

    return round(10 + (excedente * 0.0016), 2)




