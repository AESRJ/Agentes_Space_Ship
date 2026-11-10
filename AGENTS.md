# Space Ship: instrucciones compartidas

Este repositorio contiene agentes, investigación, diseño, decisiones y memoria de un equipo de seis personas. El juego tendrá otro repositorio; todavía no existe un destino acordado. No iniciar un juego, elegir motor ni desplegar producto por inferencia.

## Contexto al iniciar

Lee `docs/vision.md`, `docs/scope.md` y `docs/state.md`, y después solo la documentación de la tarea. Usa la skill `.agents/skills/space-memory/SKILL.md` para consultar el MCP `space_ship_memory`. El cuaderno está fijado en `memory/notebook.json`; nunca uses otro cuaderno por estar activo globalmente.

Git conserva decisiones y evidencia versionada; NotebookLM es la memoria consultable compartida. Una respuesta de NotebookLM necesita contraste con fuentes y archivos vigentes: no equivale a aprobación. Si hay discrepancia, identifica versiones y registra el conflicto. La documentación antigua puede describir propuestas ya sustituidas.

## Alcance y evidencia

- Se ha autorizado montar este sistema de agentes y memoria. El diseño del juego sigue en exploración.
- Distingue propuesta, decisión aceptada por una persona, implementación y verificación. Una decisión aceptada indica quién la aprobó y dónde consta; no inventes aprobación.
- Conserva la cooperación astronauta/torre, el objetivo educativo y las consecuencias de decisiones. El tercer rol, el motor y la modalidad de conexión siguen abiertos.
- Todo puzzle usa `docs/puzzles/TEMPLATE.md` y conecta fuente científica, reparto de información, reglas, integración y pruebas. Señala simplificaciones; no inventes datos NASA, físicas ni APIs.
- No afirmes haber probado código o publicado cambios sin evidencia. Nunca guardes credenciales, cookies, conversaciones personales o logs completos en Git o NotebookLM.

## Selección de agentes

Los perfiles están en `.codex/agents/`. Usa coordinacion para descomponer encargos; investigacion para fuentes; diseno para puzzles/niveles; implementacion para cambios autorizados; pruebas para verificar; memoria para consolidar contexto. No hace falta invocar todos. Delega únicamente partes independientes con resultado concreto y archivos delimitados; un solo escritor por archivo/escena. El coordinador integra resultados y resuelve dependencias antes de continuar.

## Memoria durante y al cerrar

Tras una decisión, hito, bloqueo o antes de cerrar una tarea, llama `memory_checkpoint` con identificador único, resumen, evidencia y siguientes pasos. Los subagentes devuelven notas al coordinador; solo el coordinador registra el cierre, para evitar duplicados. Si el envío falla, conserva el registro local y reporta `pending`; reintenta con `memory_sync`. No declares memoria sincronizada por el mero hecho de escribir un archivo.

Actualiza `docs/state.md` cuando cambie el estado general. `memory_sync` sube los registros pendientes. `memory_publish_context` publica una instantánea de contexto: úsala al cambiar visión/alcance/decisiones y al consolidar un PR. Un integrante designado integra estas instantáneas; no hacerlo simultáneamente desde seis ramas. El trabajo local no se presenta como integrado en main.

## Trabajo y verificación

Una rama por tarea, sin forzar pushes ni reescribir trabajo ajeno. Conserva los cambios del usuario. Ejecuta `python scripts/validate.py` y `python -m unittest discover -s tests -v` al modificar herramientas. Para documentación, verifica referencias y coherencia. Explica límites de pruebas (por ejemplo Windows no ejecutado). Antes de un PR, completa su plantilla y un registro de sesión.

## Futuro repositorio del juego

Usa `python scripts/export_project.py --output <carpeta-nueva>` cuando se pida preparar el traspaso. El resultado es un paquete de contexto con revisión y hashes, no un despliegue. No copia credenciales ni el historial Git. Conserva aquí la memoria y registra después el enlace al repositorio de implementación cuando el equipo lo proporcione.
