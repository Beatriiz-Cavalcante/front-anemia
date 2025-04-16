
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        campo1 = request.form.get('campo1')
        campo2 = request.form.get('campo2')
        campo3 = request.form.get('campo3')
        campo4 = request.form.get('campo4')
        campo5 = request.form.get('campo5')
        return render_template('dashboard.html', campo1=campo1, campo2=campo2, campo3=campo3,campo4=campo4, campo5=campo5)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
