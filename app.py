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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
