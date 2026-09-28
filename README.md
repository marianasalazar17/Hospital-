# Tarea 2: Estructuras de decisión - Expedientes Digitales (Hospital de Diagnóstico)

Programa en Flask que evalúa el estado de un expediente digital de un empleado según los documentos del checklist correspondiente a su perfil. Forma parte del reto "Expedientes digitales: modernizando el ingreso de personal en RRHH".

**Integrantes:** [Mariana Salazar] ([marianasalazar17]) y [Fiorella Funes] ([usuario GitHub 2])

## Requisitos

- Python 3
- Flask

```bash
pip install -r requirements.txt
```

## Cómo ejecutarlo

```bash
python app.py
```

El servidor queda en `http://127.0.0.1:5000`.

## Ruta

```
/expediente/<nombreEmpleado>/<perfil>/<documentosSubidos>
```

| Parámetro | Descripción |
|---|---|
| `nombreEmpleado` | Nombre del empleado |
| `perfil` | Perfil/puesto: `administrativo` o `medico` |
| `documentosSubidos` | Número entero de documentos subidos al expediente |

## Lógica de decisión

Primero se determina el checklist según el perfil y luego se compara con los documentos subidos, usando `if/elif/else`.

| Estado | Condición |
|---|---|
| `sin iniciar` | documentos subidos = 0 |
| `incompleto` | 0 < subidos < requeridos |
| `completo` | subidos ≥ requeridos |
| `perfil no reconocido` | el perfil no tiene checklist definido (respuesta HTTP 400) |

Documentos requeridos por perfil (valores de prueba, hasta recibir las plantillas de RRHH):

| Perfil | Documentos requeridos |
|---|---|
| `administrativo` | 5 |
| `medico` | 8 |

## Ejemplos de prueba

| URL | Estado |
|---|---|
| `/expediente/Ana/administrativo/0` | sin iniciar |
| `/expediente/Luis/medico/3` | incompleto |
| `/expediente/Marta/administrativo/5` | completo |
| `/expediente/Carlos/medico/8` | completo |
| `/expediente/Sofia/administrativo/4` | incompleto |
| `/expediente/Pedro/conserje/2` | perfil no reconocido |

Ejemplo de respuesta para `/expediente/Luis/medico/3`:

```json
{
  "documentosRequeridos": 8,
  "documentosSubidos": 3,
  "empleado": "Luis",
  "estado": "incompleto",
  "perfil": "medico"
}
```
