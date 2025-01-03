from flask import Flask
import sys
import os

# Adicionando o diretório base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Configuração básica
app.config["DEBUG"] = True

# Rota inicial para teste
@app.route("/")
def home():
    return {"message": "Bem-vindo ao Smart Logistics Hub"}

if __name__ == "__main__":
    app.run()
