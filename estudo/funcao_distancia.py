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
        "duracao": elemento["duration"]["text"]
    }



