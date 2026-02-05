import os  
from flask import Flask
from flask_cors import CORS
from controllers.routes import api
from db import criar_tabelas
from dotenv import load_dotenv   # type: ignore


load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(api)

criar_tabelas()

if __name__ == "__main__":
    
    token = os.getenv('INTERNAL_API_TOKEN')
    print(f"SISTEMA: Token '{token}' carregado com sucesso.")
    app.run(debug=True)
