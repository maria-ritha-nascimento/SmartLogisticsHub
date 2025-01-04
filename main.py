from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
import os
import sys

# Adicionando o diretório base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.models import db
from app.views import api_namespace

app = Flask(__name__)

# Configuração básica
app.config["DEBUG"] = True

# Configuração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smartlogistics.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Configuração do Swagger
api = Api(app, version="1.0", title="Smart Logistics Hub API", description="APIs para gerenciamento logístico")
api.add_namespace(api_namespace, path="/packages")

# Rota inicial para teste
@app.route("/")
def home():
    return {"message": "Bem-vindo ao Smart Logistics Hub"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Criação de tabelas dentro do contexto da aplicação
    app.run(debug=True)
