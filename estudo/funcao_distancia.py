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
            "origins": endereco_cliente,
            "destinations": ENDERECO_LOJA_HAMBURGUERIA,
            "key": GOOGLE_MAPS_API_KEY,
            "language": "pt-BR",
            "units": "metric"
        }
    
    response = requests.get(url, params=params)
    data=  response.json()
    # print(data) isso vai mostrar no terminal a resposta da API


    try:
        distancia= data['rows'][0]['elements'][0]['distance']['text']
        distancia_metros=data['rows'][0]['elements'][0]['distance']['value']
        duracao= data['rows'][0]['elements'][0]['duration']['text']
        return jsonify({"distancia": distancia, "distancia_metros": distancia_metros, "duracao": duracao})
    except:
        return jsonify({"erro": "Não foi possível calcular a distãncia."
                        }),400


# def calcular_frete(distancia_metros):
#     if distancia_metros <= 2000:
#         return 6.00
#     elif distancia_metros <= 3000:
#         return 7.00
#     elif distancia_metros <= 4000:
#         return 8.00
#     elif distancia_metros <= 5000:
#         return 9.00
#     elif distancia_metros <= 6000:
#         return 10.00
#     elif distancia_metros <= 7000:
#         return 11.00
 
#     excedente = distancia_metros - 7000

#     return round(10 + (excedente * 0.0016), 2)

# o próximo passo era colocar estado e cidade do cliente, pois para calcular_frete com precisão