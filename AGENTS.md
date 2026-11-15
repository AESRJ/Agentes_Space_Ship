# Space Ship: instrucciones compartidas

Este repositorio contiene agentes, investigación, diseño, decisiones y memoria del equipo activo de cinco personas. El juego está en https://github.com/AESRJ/LaunchControlGodot; Sojo se incorporó el 2026-11-15 y releva a Adrian (ADR-0005). No iniciar un juego ni desplegar producto por inferencia. Godot y la planificación con Spec Kit para Launch Control fueron solicitados explícitamente por Jorge; ver docs/plan-godot.md y ADR-0003.

## Contexto al iniciar

El primer paso de cada conversación de trabajo es que la persona se identifique por nombre: Gael, Sojo, Kevin, Isra o Jorge. Adrian está inactivo desde el relevo: conserva su historial y autoría, pero no inicia sesiones nuevas. Si aún no lo dijo en esta conversación, pregunta «¿Con cuál nombre del equipo te identificas?» antes de trabajar o consultar memoria. No omitas esta confirmación por existir una sesión local anterior ni deduzcas la persona del dueño del repositorio, de Git o del equipo utilizado. Si ya se identificó, no repitas la pregunta. Después lee `team/members.json`, confirma la tarea y ejecuta `python scripts/team_session.py status`; inicia o reanuda la sesión para esa persona y tarea según `docs/team-workflow.md`. No hagas commit/push sin identidad confirmada. Los seis perfiles de agentes son herramientas compartidas, no una asignación individual por integrante humano.

Lee `docs/vision.md`, `docs/scope.md` y `docs/state.md`, y después solo la documentación de la tarea. Usa la skill `.agents/skills/space-memory/SKILL.md` para consultar el MCP `space_ship_memory`. El cuaderno está fijado en `memory/notebook.json`; nunca uses otro cuaderno por estar activo globalmente.

Cuando alguien solicite sus tareas, consulta `specs/001-launch-control-godot/assignments.md`, `tasks.md`, `task-index.json` y `status.md`, filtra por el ID confirmado y muestra sus tareas activas con dependencias y la primera que pueda empezar. No rehagas el reparto ni marques dependencias como terminadas sin evidencia. Consulta también la guía docs/setup/team-readiness.md del repositorio del juego: una liberación técnica publicada y verificada permite iniciar las tareas indicadas aunque queden seguimientos individuales. No conviertas el acceso de Sojo o una prueba personal aún pendiente en bloqueo de los integrantes con base y permisos. Si la base no está publicada, indica esa dependencia real. Para ejecutar los comandos Spec Kit en un clon nuevo, selecciona esta funcionalidad mediante `SPECIFY_FEATURE_DIRECTORY=specs/001-launch-control-godot` en el entorno del comando; el puntero `.specify/feature.json` es local y no se comparte.

Git conserva decisiones y evidencia versionada; NotebookLM es la memoria consultable compartida. Una respuesta de NotebookLM necesita contraste con fuentes y archivos vigentes: no equivale a aprobación. Si hay discrepancia, identifica versiones y registra el conflicto. La documentación antigua puede describir propuestas ya sustituidas.

## Alcance y evidencia

Desde el 2026-11-15 (ADR-0005), Sojo es activo y asume las ocho tareas de Adrian (T007, T008, T009, T011, T013, T017, T030 y T035) y su apoyo técnico en T039. Adrian queda `inactive` y conserva su autoría e historial. Reparto actual: Jorge 9, Gael 9, Sojo 8, Kevin 8 e Isra 8; no uses repartos anteriores. La cuenta GitHub de Sojo está pendiente: no la infieras por su nombre ni declares su acceso. Guía de incorporación: `docs/setup/sojo.md`.

- Se ha autorizado montar este sistema de agentes y memoria. El diseño del juego sigue en exploración.
- Distingue propuesta, decisión aceptada por una persona, implementación y verificación. Una decisión aceptada indica quién la aprobó y dónde consta; no inventes aprobación.
- Conserva la cooperación astronauta/torre, el objetivo educativo y las consecuencias de decisiones. Para Launch Control se planifican astronauta y torre, Godot y dos PC por Internet; otros roles o modalidades requieren una decisión posterior.
- Todo puzzle usa `docs/puzzles/TEMPLATE.md` y conecta fuente científica, reparto de información, reglas, integración y pruebas. Señala simplificaciones; no inventes datos NASA, físicas ni APIs.
- No afirmes haber probado código o publicado cambios sin evidencia. Nunca guardes credenciales, cookies, conversaciones personales o logs completos en Git o NotebookLM.

## Selección de agentes

Los perfiles están en `.codex/agents/`. Usa coordinacion para descomponer encargos; investigacion para fuentes; diseno para puzzles/niveles; implementacion para cambios autorizados; pruebas para verificar; memoria para consolidar contexto. No hace falta invocar todos. Delega únicamente partes independientes con resultado concreto y archivos delimitados; un solo escritor por archivo/escena. El coordinador integra resultados y resuelve dependencias antes de continuar.

## Memoria durante y al cerrar

Tras una decisión, hito, bloqueo o antes de cerrar una tarea, llama `memory_checkpoint` con identificador único, resumen, evidencia y siguientes pasos. Los subagentes devuelven notas al coordinador; solo el coordinador registra el cierre, para evitar duplicados. Si el envío falla, conserva el registro local y reporta `pending`; reintenta con `memory_sync`. No declares memoria sincronizada por el mero hecho de escribir un archivo.

Actualiza `docs/state.md` cuando cambie el estado general. `memory_sync` sube los registros pendientes. `memory_publish_context` publica una instantánea de contexto: úsala al cambiar visión/alcance/decisiones y al consolidar un PR. Un integrante designado integra estas instantáneas; no hacerlo simultáneamente desde seis ramas. El trabajo local no se presenta como integrado en main.

## Trabajo y verificación

Usa `python scripts/team_session.py commit -m "descripción"` para commits de una sesión identificada; prepara antes solo los archivos de la tarea con `git add`. Conserva los trailers `Team-Member` y `AI-Assisted`, también al fusionar con squash. No inventes cuentas GitHub, correos ni coautores. Cada persona revisa el diff y la evidencia producidos con IA antes de publicar. La política propuesta permite que el autor fusione su PR con pruebas aprobadas sin revisión obligatoria de otra persona; no presupongas que las reglas remotas ya están configuradas.

Una rama por tarea, sin forzar pushes ni reescribir trabajo ajeno. Conserva los cambios del usuario. Ejecuta `python scripts/validate.py` y `python -m unittest discover -s tests -v` al modificar herramientas. Para documentación, verifica referencias y coherencia. Explica límites de pruebas (por ejemplo Windows no ejecutado). Antes de un PR, completa su plantilla y un registro de sesión.

## Futuro repositorio del juego

Usa `python scripts/export_project.py --output <carpeta-nueva>` cuando se pida preparar el traspaso. El resultado es un paquete de contexto con revisión y hashes, no un despliegue. No copia credenciales ni el historial Git. Conserva aquí la memoria y registra después el enlace al repositorio de implementación cuando el equipo lo proporcione.
