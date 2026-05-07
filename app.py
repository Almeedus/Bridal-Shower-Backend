from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    """
    Rota teste para validar a API
    ---
    responses:
        200:
            description: API funcionando
    """
    return 'funcionando'


if __name__ == '__main__':
    app.run()