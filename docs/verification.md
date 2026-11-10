# Evidencia de verificación

Fecha: 2026-11-10.

## Herramientas

- `scripts/validate.py`: seis perfiles válidos, UUID del cuaderno y configuración TOML.
- `python -m unittest discover -s tests -v`: 13 casos locales; recuperación offline, contenido inmutable por ID, deduplicación remota, nombres de fuentes conservados por NotebookLM, rechazo de rutas externas, errores de CLI, configuración personal conservada, entorno virtual y paquete de traspaso.
- La skill `space-memory` pasó el validador de skill-creator.
- [Primera ejecución de CI](https://github.com/AESRJ/Agentes_Space_Ship/actions/runs/42906664513): pasó en Ubuntu y Windows, incluyendo dependencias, los 12 casos de esa revisión y análisis sintáctico PowerShell. Revisar Actions para las ejecuciones posteriores.

## NotebookLM real

Se inicializó el adaptador usando un cliente MCP por stdio y se descubrieron sus cinco herramientas. `memory_status` confirmó el cuaderno del proyecto. `memory_ask` recuperó fuentes y distinguió correctamente que motor y número definitivo de roles siguen pendientes. `memory_checkpoint` guardó el registro inicial y confirmó `synced` con fuente `e244663f-c9d9-4b32-ad3c-be14edbaa9b2`.

La comprobación real detectó que la subida de archivos puede conservar el nombre del archivo aunque se indique otro título. Se ajustó la deduplicación para reconocer ambas formas y el formato inicial, y se añadió prueba de regresión. No se borraron fuentes para corregirlo.

## Límites

CI no inicia sesión en Google ni verifica los permisos de compañeros. La incorporación completa con navegador y cuentas individuales en un equipo Windows sigue pendiente. No se ha probado ni implementado el videojuego. No se ha configurado protección de main ni enviado invitaciones: faltan las identidades del equipo.
