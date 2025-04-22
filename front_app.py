from flask import Flask, render_template, request
from flask_cors import CORS

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
        # Atenção: você está usando campo6 sem declarar
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
   
    return render_template('dashboard.html',)
                

if __name__ == '__main__':
    app.run(debug=True, port=5001)
