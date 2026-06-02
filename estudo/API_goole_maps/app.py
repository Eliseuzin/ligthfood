from flask import Flask, render_template, request, jsonify
import requests
import os   

app = Flask(__name__)

 # Substitua por sua chave da API
GOOGLE_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
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



@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        resultado = obter_distancia(request.json["endereco"])
        return jsonify(resultado)

    except Exception:
        return jsonify({
            "erro": "Não foi possível calcular a distância."
        }), 400