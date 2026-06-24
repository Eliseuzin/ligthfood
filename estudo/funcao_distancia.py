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
    endereco_cliente = request.json.get('endereco')
    
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
        duracao= data['rows'][0]['elements'][0]['duration']['text']
        return jsonify({"distancia": distancia, "duracao": duracao})
    except:
        return jsonify({"erro": "Não foi possível calcular a distãncia."}),400







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



# <!DOCTYPE html>
# <html lang="pt-BR">
# <head>
#   <meta charset="UTF-8">
#   <title>Calculadora de Distância</title>
# </head>
# <body>
#   <h2>Calcular distância até a loja</h2>
#   <input type="text" id="endereco" placeholder="Digite seu endereço" />
#   <button onclick="calcular()">Calcular</button>
#   <p id="resultado"></p>

#   <script>
#     async function calcular() {
#       const endereco = document.getElementById("endereco").value;
#       const resposta = await fetch("/calcular", {
#         method: "POST",
#         headers: { "Content-Type": "application/json" },
#         body: JSON.stringify({ endereco: endereco })
#       });

#       const dados = await resposta.json();
#       const resultado = document.getElementById("resultado");

#       if (resposta.ok) {
#         resultado.innerText = `Distância: ${dados.distancia}, Tempo estimado: ${dados.duracao}`;
#       } else {
#         resultado.innerText = "Erro: " + (dados.erro || "não foi possível calcular.");
#       }
#     }
#   </script>
# </body>
# </html>













#  Ative o ambiente virtual
#python -m venv venv para criar o ambiente virtual
# No terminal, digite:
# E:\bettersites\calculardistanciacomapigooglemaps\venv\Scripts\activate

# Você saberá que deu certo se o terminal mostrar algo como:
# (venv) PS E:\bettersites\calculardistanciacomapigooglemaps>

# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# ENDERECO_LOJA = "R. Trinta e Sete, 81 - São Luiz, Ribeirão das Neves - MG, 33882-215"
#  # Substitua por sua chave da API
# GOOGLE_API_KEY = "" 
# #Distance Matrix API, temos que ativa ela no https://console.cloud.google.com e depois coloca nenhuma restricoes em APIs e serviços/credencias ou coloca autoriza Distance Matrix API, e devemos ativa routes APIs too

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/calcular', methods=['POST'])
# def calcular():
#     print(request.json)
#     endereco_cliente = request.json.get('endereco')

#     url = "https://maps.googleapis.com/maps/api/distancematrix/json"
#     params = {
#         "origins": endereco_cliente,
#         "destinations": ENDERECO_LOJA,
#         "key": GOOGLE_API_KEY,
#         "language": "pt-BR",
#         "units": "metric"
#     }

#     response = requests.get(url, params=params)
#     data = response.json()
#     print(data)
  
#     # print(data)  # <-- isso vai mostrar no terminal a resposta da API

#     try:
#         distancia = data['rows'][0]['elements'][0]['distance']['text']
#         duracao = data['rows'][0]['elements'][0]['duration']['text']
#         return jsonify({"distancia": distancia, "duracao": duracao})
#     except:
#         return jsonify({"erro": "Não foi possível calcular a distância."}), 400

# if __name__ == '__main__':
#     app.run(debug=True)