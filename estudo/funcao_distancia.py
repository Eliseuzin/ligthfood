from flask import Flask, jsonify, request
from dotenv import load_dotenv
#precisa instalar requests
import os, requests


load_dotenv()
app=Flask(__name__)

GOOGLE_MAPS_API_KEY=os.getenv('GOOGLE_MAPS_API_KEY')
ENDERECO_LOJA_HAMBURGUERIA = os.getenv('ENDERECO_LOJA_HAMBURGUERIA')

def calcular_distancia(endereco_cliente):
    # print(request.json)
    url= "https://maps.googleapis.com/maps/api/distancematrix/json"
    params={
            "origins": ENDERECO_LOJA_HAMBURGUERIA,
            "destinations":endereco_cliente,
            "key": GOOGLE_MAPS_API_KEY,
            "language": "pt-BR",
            "units": "metric"
        }
    
    response = requests.get(url, params=params)
    data=  response.json()
    # print(data) isso vai mostrar no terminal a resposta da API
    #isto é essencial, pois mostra se realmente estamos buscando o endereço pretendido
    # print("Origem:", ENDERECO_LOJA_HAMBURGUERIA)
    # print("Destino:", endereco_cliente)
    
    try:
        distancia= data['rows'][0]['elements'][0]['distance']['text']
        distancia_metros=data['rows'][0]['elements'][0]['distance']['value']
        duracao= data['rows'][0]['elements'][0]['duration']['text']
        return jsonify({"distancia": distancia, "distancia_metros": distancia_metros, "duracao": duracao})
    except:
        return jsonify({"erro": "Não foi possível calcular a distãncia."
                        }),400