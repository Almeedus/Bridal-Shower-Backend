from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_cors import CORS
import os



from database import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

Swagger(app)

from models import Item


@app.get('/')
def home():
    """
    Rota teste para validar a API
    ---
    responses:
        200:
            description: API funcionando
    """
    return 'funcionando'


@app.get('/items')
def get_items():
    """
    Rota responsável por carregar os registros do banco de dados
    ---
    responses:
        200:
            description: Registros encontrados
    """

    items = Item.query.all()

    return jsonify(
        [item.to_dict() for item in items]
    )

@app.patch('/items/<int:id>')
def update_item(id):
    """
    Rota responsável por atualizar o status de compra do item
    ---
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer

    responses:
      200:
        description: Item atualizado com sucesso
      404:
        description: Item não encontrado
    """

    item = Item.query.get(id)

    if not item:
        return jsonify({
            'message': 'Item not found'
        }), 404

    item.comprado = True

    db.session.commit()

    return jsonify({
        'message': 'Item updated successfully'
    })

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
