from flask import Flask, request, jsonify, session
from db import *

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'  # Cambia esto en producción

# ------------------ AUTENTICACIÓN ------------------

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if verificar_usuario(data['usuario'], data['password']):
        session['usuario'] = data['usuario']
        return jsonify({'mensaje': 'Login correcto'})
    return jsonify({'error': 'Credenciales inválidas'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)
    return jsonify({'mensaje': 'Logout exitoso'})

# ------------------ TAREAS ------------------

@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(obtener_tareas())

@app.route('/tareas', methods=['POST'])
def nueva_tarea():
    data = request.json
    crear_tarea(data['nombre'], data['descripcion'], data['fecha_limite'], data['prioridad'], data['creador_id'])
    return jsonify({'mensaje': 'Tarea creada'})

@app.route('/tareas/<int:id>', methods=['PUT'])
def editar_tarea(id):
    data = request.json
    modificar_tarea(id, data['nombre'], data['descripcion'], data['fecha_limite'], data['prioridad'])
    return jsonify({'mensaje': 'Tarea modificada'})

@app.route('/tareas/<int:id>', methods=['DELETE'])
def borrar_tarea(id):
    eliminar_tarea(id)
    return jsonify({'mensaje': 'Tarea eliminada'})

# ------------------ EVENTOS ------------------

@app.route('/eventos', methods=['GET'])
def listar_eventos():
    return jsonify(obtener_eventos())

@app.route('/eventos', methods=['POST'])
def nuevo_evento():
    data = request.json
    crear_evento(data['nombre'], data['fecha_evento'], data['hora_evento'], data['creador_id'])
    return jsonify({'mensaje': 'Evento creado'})

@app.route('/eventos/<int:id>', methods=['PUT'])
def editar_evento(id):
    data = request.json
    modificar_evento(id, data['nombre'], data['fecha_evento'], data['hora_evento'])
    return jsonify({'mensaje': 'Evento modificado'})

@app.route('/eventos/<int:id>', methods=['DELETE'])
def borrar_evento(id):
    eliminar_evento(id)
    return jsonify({'mensaje': 'Evento eliminado'})

# ------------------ SUBTAREAS ------------------

@app.route('/subtareas', methods=['GET'])
def listar_subtareas():
    return jsonify(obtener_subtareas())

@app.route('/subtareas', methods=['POST'])
def nueva_subtarea():
    data = request.json
    crear_subtarea(data['nombre'], data['descripcion'], data['fecha_limite'], data['tarea_padre_id'], data['creador_id'])
    return jsonify({'mensaje': 'Subtarea creada'})

@app.route('/subtareas/<int:id>', methods=['PUT'])
def editar_subtarea(id):
    data = request.json
    modificar_subtarea(id, data['nombre'], data['descripcion'], data['fecha_limite'])
    return jsonify({'mensaje': 'Subtarea modificada'})

@app.route('/subtareas/<int:id>', methods=['DELETE'])
def borrar_subtarea(id):
    eliminar_subtarea(id)
    return jsonify({'mensaje': 'Subtarea eliminada'})

# ------------------ INICIO ------------------

if __name__ == '__main__':
    app.run(debug=True)
