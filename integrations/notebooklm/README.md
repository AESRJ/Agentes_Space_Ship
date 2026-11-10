# Adaptación de NotebookLM for Codex

Origen: https://github.com/knowingdoing/notebooklm-codex
Revisión consultada: `574caf973e4f7bc4ad002a0098e4cd3144618c02`.
Licencia original: [MIT](LICENSE.knowingdoing).

`server.py` adapta el patrón FastMCP → CLI del proyecto original. `project_memory.py` aporta cuaderno explícito por operación, errores verificables, UTF-8 para Windows, checkpoints locales, deduplicación por título/hash, espera de fuentes y una lista limitada de documentos exportables. No expone borrado de fuentes ni cambios de permisos.

El original documenta macOS/Linux. El instalador PowerShell y las pruebas Windows de este repositorio son nuestra adaptación. Usa notebooklm-py no oficial; cambios del servicio pueden requerir mantenimiento. No se ha sustituido el servidor NotebookLM global del usuario.

Las fuentes se añaden como versiones inmutables. La deduplicación evita reintentos secuenciales y usa un bloqueo por copia de trabajo; NotebookLM no ofrece aquí una transacción entre seis equipos. Por eso el equipo designa un integrador para publicar instantáneas generales. Cada sesión usa ID propio.
