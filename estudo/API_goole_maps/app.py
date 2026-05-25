#  Ative o ambiente virtual
#python -m venv venv para criar o ambiente virtual
# No terminal, digite:
# E:\bettersites\calculardistanciacomapigooglemaps\venv\Scripts\activate

# Você saberá que deu certo se o terminal mostrar algo como:
# (venv) PS E:\bettersites\calculardistanciacomapigooglemaps>

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

ENDERECO_LOJA = "R. Trinta e Sete, 81 - São Luiz, Ribeirão das Neves - MG, 33882-215"
 # Substitua por sua chave da API
GOOGLE_API_KEY = "AIzaSyC_QWX_U3N3X5UcKWX1pYZ-13Xr4shYv0w" 
#Distance Matrix API, temos que ativa ela no https://console.cloud.google.com e depois coloca nenhuma restricoes em APIs e serviços/credencias ou coloca autoriza Distance Matrix API, e devemos ativa routes APIs too


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    endereco_cliente = request.json.get('endereco')

    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": endereco_cliente,
        "destinations": ENDERECO_LOJA,
        "key": GOOGLE_API_KEY,
        "language": "pt-BR",
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()
  
    # print(data)  # <-- isso vai mostrar no terminal a resposta da API

    try:
        distancia = data['rows'][0]['elements'][0]['distance']['text']
        duracao = data['rows'][0]['elements'][0]['duration']['text']
        return jsonify({"distancia": distancia, "duracao": duracao})
    except:
        return jsonify({"erro": "Não foi possível calcular a distância."}), 400

if __name__ == '__main__':
    app.run(debug=True)
