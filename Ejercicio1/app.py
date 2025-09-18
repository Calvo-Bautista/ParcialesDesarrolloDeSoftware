from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
# Lista para almacenar objetos
lista_objetos = []


@app.route("/metodopost", methods=["POST"])
def metodopost():
    """
    Agregar objeto a la lista
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          example:
            nombre: "Juan"
            edad: 25
            ciudad: "Buenos Aires"
    responses:
      201:
        description: Objeto agregado exitosamente
        schema:
          type: object
          properties:
            mensaje:
              type: string
            objeto:
              type: object
    """
    objeto = request.get_json()
    lista_objetos.append(objeto)
    return jsonify({"mensaje": "Objeto agregado", "objeto": objeto}), 201


if __name__ == "__main__":
    app.run(debug=True)
