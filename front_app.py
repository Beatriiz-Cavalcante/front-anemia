from flask import Flask, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5001"}})

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        campo1 = request.form.get('campo1')
        campo2 = request.form.get('campo2')
        campo3 = request.form.get('campo3')
        campo4 = request.form.get('campo4')
        campo5 = request.form.get('campo5')
        # Se quiser exibir os dados inseridos após o envio
        return render_template('dashboard.html',
            campo1=campo1,
            campo2=campo2,
            campo3=campo3,
            campo4=campo4,
            campo5=campo5
        )
    return render_template('form.html')

@app.route('/dashboard')
def dashboard():
    try:
        response = requests.get("http://127.0.0.1:5000/consultar")
        dados = response.json()

        resultados = [item['resultado'] for item in dados]
        total = len(resultados)
        positivos = resultados.count(1)
        negativos = resultados.count(0)

        sexos = [item['Sex'] for item in dados]
        homens = sexos.count(1)
        mulheres = sexos.count(0)

        return render_template('dashboard.html',
            hbs=[item['Hb'] for item in dados],
            reds=[item['%Red Pixel'] for item in dados],
            greens=[item['%Green pixel'] for item in dados],
            blues=[item['%Blue pixel'] for item in dados],
            resultados=resultados,
            total=total,
            positivos=positivos,
            negativos=negativos,
            homens=homens,
            mulheres=mulheres
        )
    except requests.exceptions.RequestException as e:
        print("Erro ao buscar dados da API:", e)
        return "Erro ao carregar o dashboard.", 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
