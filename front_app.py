from flask import Flask, render_template, request
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base


# Banco de dados
engine = create_engine('sqlite:///predicoes.db')
Base = declarative_base()

class Predicao(Base):
    __tablename__ = 'predicoes'
    id = Column(Integer, primary_key=True)
    Number = Column(Integer)
    Sex = Column(Integer)
    Hb = Column(Float)
    blue_pixel = Column(Float)
    green_pixel = Column(Float)
    red_pixel = Column(Float)
    resultado = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

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
    sessao = Session()
    try:
        predicoes = sessao.query(Predicao).order_by(Predicao.id.desc()).all()

        if not predicoes:
            return render_template('dashboard.html',
                campo1='-',
                campo2='-',
                campo3='-',
                campo4='-',
                campo5='-'
            )

        ultima = predicoes[0]

        return render_template('dashboard.html',
            campo1='Masculino' if ultima.Sex == 1 else 'Feminino',
            campo2=ultima.red_pixel,
            campo3=ultima.blue_pixel,
            campo4=ultima.green_pixel,
            campo5=ultima.Hb
        )
    except Exception as e:
        return f"Erro ao carregar o dashboard: {e}", 500
    finally:
        sessao.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
