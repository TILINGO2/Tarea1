from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# 1️ ESTRUCTURA DE DATOS:
# Los usuarios se almacenan en una lista de diccionarios (estructura en memoria, no base de datos)
# Cada usuario tiene un ID, un nombre y un email
usuarios = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

# 2️ ENDPOINTS DISPONIBLES:
# Este endpoint devuelve todos los usuarios registrados
@app.route('/api/users', methods=['GET'])
def get_users():
    # 3️ COMPORTAMIENTO SÍNCRONO:
    # Aquí se podría simular un procesamiento con time.sleep()
    # pero este endpoint responde inmediatamente
    return jsonify({"status": "success", "data": usuarios}), 200


# Este endpoint simula obtener un usuario por ID con un retardo de 2 segundos
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 3️ Simulación de procesamiento (bloqueante/síncrono)
    time.sleep(2)
    for user in usuarios:
        if user["id"] == user_id:
            # 4️⃣ RESPUESTA EXITOSA:
            # Devuelve un JSON con clave 'status' y 'data'
            return jsonify({"status": "success", "data": user}), 200

    # 4️ RESPUESTA DE ERROR:
    # Si el usuario no existe, responde con un mensaje y código 404
    return jsonify({"status": "error", "message": "Usuario no encontrado"}), 404


# Endpoint para crear un nuevo usuario (POST)
@app.route('/api/users', methods=['POST'])
def create_user():
    # Simula un pequeño retardo en la creación
    time.sleep(1)
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"status": "error", "message": "Datos incompletos"}), 400

    new_id = len(usuarios) + 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    usuarios.append(new_user)

    return jsonify({"status": "success", "data": new_user}), 201


if __name__ == '__main__':
    # Escuchar en todas las interfaces (no solo en localhost)
    app.run(host='0.0.0.0', port=5000, debug=True)

