from flask import Flask
from routes import api
from db import criar_tabelas

app = Flask(__name__)
app.register_blueprint(api)

criar_tabelas()

if __name__ == "__main__":
    app.run(debug=True)
