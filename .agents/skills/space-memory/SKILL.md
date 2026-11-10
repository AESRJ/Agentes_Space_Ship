---
name: space-memory
description: Consultar y registrar la memoria del proyecto Space Ship en su cuaderno NotebookLM, al retomar trabajo, consolidar decisiones o cerrar hitos de investigación, diseño e implementación.
---

# Memoria de Space Ship

Usa el servidor MCP `space_ship_memory`, adaptación local de knowingdoing/notebooklm-codex. Si no aparece, ejecuta el instalador del repositorio y reinicia Codex. No sustituyas este cuaderno por el activo de otro servidor.

1. Al retomar: `memory_status` y `memory_ask` con una pregunta concreta; contrasta fuentes y versiones con los archivos de Git. Si faltan permisos o autenticación, continúa con documentos locales e indica que la consulta remota está pendiente.
2. Durante el trabajo: conserva decisiones y especificaciones en `docs/`. Tras un hito o bloqueo, `memory_checkpoint(record_id, summary, evidence, next_steps, kind, status)` guarda un registro local y trata de subirlo. El ID debe ser único por evento (fecha, tarea y sufijo); reutilízalo únicamente al reintentar el mismo contenido.
3. Al cerrar: verifica que el resultado indique `synced` y contenga `source_id`. Si indica `pending`, deja el registro intacto y comunica el pendiente. `memory_sync` reintenta registros de `docs/sessions/` sin borrar historial.
4. Al consolidar contexto: `memory_publish_context` añade una instantánea con hash. Las anteriores son históricas; no se borran automáticamente. Coordina un solo publicador de instantáneas a la vez. Git determina qué rama/revisión se integró; NotebookLM no decide cuál propuesta fue aprobada.

Las herramientas no necesitan recibir credenciales ni elegir cuaderno. Para cambiar de proyecto se configura otro repositorio/cuaderno; no se redirige esta memoria. No guardar chats completos ni información personal. Las credenciales de cada compañero son locales y el acceso al cuaderno se concede por separado del acceso a GitHub.

Cuando se exceda capacidad o haya errores, registra el bloqueo; no borres fuentes automáticamente. La compactación o eliminación de fuentes se decide con el equipo y conserva referencias al historial en Git.
