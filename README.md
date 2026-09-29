# Tarea 2: Estructuras de decisión - Expedientes Digitales (Hospital de Diagnóstico)

Programa en Flask que evalúa el estado de un expediente digital de un empleado según los documentos del checklist correspondiente a su perfil/puesto. Forma parte del reto "Expedientes digitales: modernizando el ingreso de personal en RRHH".

**Integrantes:** [Nombre 1] ([usuario GitHub 1]) y [Nombre 2] ([usuario GitHub 2])

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

## Salida en color

La ruta ya no devuelve JSON: devuelve una página HTML con un recuadro de color según el estado del expediente, para que se identifique de un vistazo.

| Estado | Color |
|---|---|
| `sin iniciar` | Gris |
| `incompleto` | Amarillo |
| `completo` | Verde |
| `perfil no reconocido` | Rojo |

## Ejemplos de prueba

| URL | Estado | Color |
|---|---|---|
| `/expediente/Ana/administrativo/0` | sin iniciar | Gris |
| `/expediente/Luis/medico/3` | incompleto | Amarillo |
| `/expediente/Marta/administrativo/5` | completo | Verde |
| `/expediente/Carlos/medico/8` | completo | Verde |
| `/expediente/Sofia/administrativo/4` | incompleto | Amarillo |
| `/expediente/Pedro/conserje/2` | perfil no reconocido | Rojo |

Al abrir por ejemplo `http://127.0.0.1:5000/expediente/Marta/administrativo/5` se muestra el nombre del empleado, el perfil, el conteo de documentos y un recuadro verde con el texto "completo".

