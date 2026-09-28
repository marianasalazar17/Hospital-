from flask import Flask, jsonify

app = Flask(__name__)

# Documentos requeridos segun el checklist de cada perfil/puesto.
# La ficha del reto indica que RRHH proporcionara las plantillas reales;
# estos valores son de prueba hasta recibirlas.
DOCUMENTOS_ADMINISTRATIVO = 5
DOCUMENTOS_MEDICO = 8


@app.route("/expediente/<nombreEmpleado>/<perfil>/<int:documentosSubidos>")
def evaluarExpediente(nombreEmpleado, perfil, documentosSubidos):
    # Recibe el expediente por la ruta y retorna su estado segun el
    # checklist de documentos del perfil/puesto del empleado.

    # Paso 1: determinar cuantos documentos exige el checklist del perfil
    if perfil == "administrativo":
        documentosRequeridos = DOCUMENTOS_ADMINISTRATIVO
    elif perfil == "medico":
        documentosRequeridos = DOCUMENTOS_MEDICO
    else:
        # Caso por defecto: el perfil no tiene checklist definido
        return jsonify({
            "empleado": nombreEmpleado,
            "perfil": perfil,
            "estado": "perfil no reconocido"
        }), 400

    # Paso 2: comparar lo subido contra el checklist
    if documentosSubidos == 0:
        estado = "sin iniciar"
    elif documentosSubidos < documentosRequeridos:
        estado = "incompleto"
    else:
        estado = "completo"

    return jsonify({
        "empleado": nombreEmpleado,
        "perfil": perfil,
        "documentosSubidos": documentosSubidos,
        "documentosRequeridos": documentosRequeridos,
        "estado": estado
    })


if __name__ == "__main__":
    app.run(debug=True)
