from flask import Flask, render_template_string
 
app = Flask("hospital")
 
# Documentos requeridos segun el checklist de cada perfil/puesto.
# Valores de prueba, hasta recibir las plantillas reales de RRHH.
DOCUMENTOS_ADMINISTRATIVO = 5
DOCUMENTOS_MEDICO = 8
 
# Color asociado a cada estado
COLORES = {
    "sin iniciar": "#9e9e9e",       # gris
    "incompleto": "#f4b400",        # amarillo
    "completo": "#34a853",          # verde
    "perfil no reconocido": "#ea4335"  # rojo
}
 
PLANTILLA = """
<html>
<head><title>Estado del expediente</title></head>
<body style="font-family: Arial; text-align:center; margin-top:60px;">
    <h2>Expediente de {{ nombreEmpleado }}</h2>
    <p>Perfil: {{ perfil }}</p>
    <div style="display:inline-block; padding:15px 30px; border-radius:8px;
                background-color:{{ color }}; color:white; font-size:22px;">
        {{ estado }}
    </div>
    {% if documentosRequeridos %}
    <p style="margin-top:20px;">
        Documentos subidos: {{ documentosSubidos }} / {{ documentosRequeridos }}
    </p>
    {% endif %}
</body>
</html>
"""
 
 
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
        estado = "perfil no reconocido"
        return render_template_string(
            PLANTILLA,
            nombreEmpleado=nombreEmpleado,
            perfil=perfil,
            estado=estado,
            color=COLORES[estado],
            documentosSubidos=None,
            documentosRequeridos=None
        ), 400
 
    # Paso 2: comparar lo subido contra el checklist
   if documentosSubidos >= documentosRequeridos:
        estado = "completo"
    elif documentosSubidos > 0:
        estado = "incompleto"
    else:
        estado = "sin iniciar"
 
    return render_template_string(
        PLANTILLA,
        nombreEmpleado=nombreEmpleado,
        perfil=perfil,
        estado=estado,
        color=COLORES[estado],
        documentosSubidos=documentosSubidos,
        documentosRequeridos=documentosRequeridos
    )
 
 
if __name__ == "__main__":
    app.run(debug=True)
