from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
import os

# Adicionando o diretório base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Configuração básica
app.config["DEBUG"] = True

# Configuração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smartlogistics.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Rota inicial para teste
@app.route("/")
def home():
    return {"message": "Bem-vindo ao Smart Logistics Hub"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Criação de tabelas dentro do contexto da aplicação
    app.run(debug=True)


