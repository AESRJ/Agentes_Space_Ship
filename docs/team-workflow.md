# Identidad y trabajo del equipo con IA

## Estado vigente del equipo (2026-11-14)

Activos: Jorge (AESRJ), Gael (GaelFlores04), Adrian (adrianbalderas373488), Kevin (KVSO755) e Isra (issgg), con escritura comprobada en AESRJ/LaunchControlGodot. Sojo no está incorporado por instrucción de Jorge: registro pending, sin tareas activas. El reparto vigente son 42 tareas entre cinco: 9/9/8/8/8. Las referencias siguientes a seis personas describen el registro inicial y quedan sustituidas para la operación actual.

Registro canónico: `team/members.json`. Las cinco cuentas activas están confirmadas y la de Sojo sigue sin solicitarse mientras no esté incorporado. El registro inicial de seis se conserva en ADR-0002 y en Git como historia.

## Primer paso: identificarse por nombre en cada conversación

Antes de trabajar, cada persona dice «Soy Gael», «Soy Adrian», «Soy Kevin», «Soy Isra» o «Soy Jorge». Si no lo ha dicho en la conversación actual, la IA pregunta su nombre antes de consultar memoria o actuar. Una sesión local anterior no reemplaza esta confirmación; si ya lo dijo, no se le vuelve a preguntar.

Cada persona usa su cuenta GitHub, su propio clon o worktree y su propia autenticación Google. No compartan una carpeta de trabajo simultánea. Dentro de Codex puede escribir:

> Soy Gael. Mi tarea es investigar el lanzamiento. Lee AGENTS.md y el estado del proyecto, confirma mi sesión y trabaja solo en esta tarea. Usa mi correo de commits GitHub que te proporcionaré para iniciar la sesión.

La IA confirma a la persona declarada y no la deduce de una cuenta conectada; los vínculos Jorge ↔ AESRJ y Kevin ↔ KVSO755 están confirmados por sus titulares. La sesión queda en `.space-session.json`, ignorado por Git, y pertenece a una rama y tarea. Para una sesión nueva de Codex en la misma tarea se consulta `status`; para cambiar de tarea se inicia otra. La IA nunca asigna la identidad de una persona que no la haya declarado. Si se reanuda esa misma rama con cambios pendientes, `start --resume` permite registrar la identidad sin alterar los archivos; rechaza una rama de otra persona/tarea.

Ejemplo en PowerShell, después de instalar el proyecto y con el árbol de trabajo limpio:

```powershell
git switch main
git pull --ff-only
python scripts/team_session.py members
python scripts/team_session.py start --member gael --task investigar-lanzamiento --email "TU_CORREO_DE_COMMITS_GITHUB"
python scripts/team_session.py status
```

Reemplaza el correo por el de tu cuenta, preferentemente el `noreply` exacto mostrado en GitHub → Settings → Emails. No copies el correo de otra persona. El comando crea `gael/investigar-lanzamiento`; puede reanudar esa misma rama si ya está seleccionada. Para reanudar una rama existente, selecciónala primero con `git switch gael/investigar-lanzamiento` y ejecuta `start` con los mismos datos. No se cambia la identidad Git global ni la local; el correo de la sesión se aplica únicamente al crear cada commit con la herramienta.

En Linux/macOS se puede usar `python3` en lugar de `python`. Si las dependencias están solo en el entorno virtual, usa `.venv/bin/python` o `.\.venv\Scripts\python.exe` para las herramientas de memoria.

## Etiquetar cada cambio publicado

Selecciona archivos concretos y crea el commit:

```powershell
git diff
git add docs/mi-investigacion.md
python scripts/team_session.py commit -m "documenta condiciones del lanzamiento"
git log -1 --format=full
git push -u origin gael/investigar-lanzamiento
```

Resultado:

```text
[gael] documenta condiciones del lanzamiento

Team-Member: gael
AI-Assisted: true
```

El autor y committer Git son Gael con el correo que él declaró. GitHub relaciona el commit con su cuenta mediante un correo asociado a ella. `--without-ai` registra `AI-Assisted: false` cuando corresponda. Si varias personas contribuyeron realmente al mismo commit, agregar `Co-authored-by` con los datos que ellas indiquen; no atribuir trabajo a todo el equipo por defecto. El registro del equipo no guarda correos, aunque los commits sí contienen el correo elegido.

La herramienta comprueba identidad, rama y cambios preparados. Un `git commit` normal no recibe etiquetas automáticamente: utilicen el comando indicado. El workflow `Atribución del equipo` comprueba los commits no merge de cada PR; no reescribe el historial antiguo. Las etiquetas son declaraciones, no autenticación: para vincularlas a cuentas verificadas faltan los usuarios GitHub y una comprobación adicional. Los commits directos a main no pasan por este workflow de PR.

Un PR pertenece a una tarea y un responsable. Al usar squash, conservar `[gael]`, `Team-Member` y `AI-Assisted` en el mensaje final; esa edición final no la verifica el workflow del PR. Preferir un merge que conserve los commits si no quieren editar el mensaje. Para una autoría adicional real se siguen los [trailers de coautoría de GitHub](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors).

## Método recomendado: tareas pequeñas y flujo continuo

Es una propuesta adaptada al equipo, no una afirmación de que existe una metodología universalmente mejor ni una configuración remota ya aplicada.

1. **Elegir una tarea concreta.** Usar un issue con responsable, objetivo, archivos/área, dependencias y criterios observables de terminado. Mantener una tarea en curso por integrante como punto de partida. Tablero sugerido: Pendiente → En curso → Verificación → Integrado.
2. **Dar contexto a la IA.** Leer visión, alcance, estado y memoria; pedir una propuesta breve cuando haya incertidumbre. Un responsable humano decide alcance y criterios. Los perfiles de investigación, diseño, implementación y pruebas se eligen por necesidad, sin ejecutar seis agentes por obligación.
3. **Aislar el trabajo.** Una rama por tarea con el ID de la persona. Un escritor por archivo/escena; si dos tareas tocan lo mismo, acordar orden o separar archivos antes de empezar. Los agentes paralelos solo trabajan en partes independientes con alcance definido.
4. **Implementar y comprobar.** Cambios pequeños, pruebas relevantes y revisión del diff por el propio responsable. Una segunda revisión con IA puede detectar errores; no prueba por sí misma corrección ni aprueba decisiones del juego. Para herramientas ejecutar `python scripts/validate.py` y `python -m unittest discover -s tests -v`.
5. **Integrar pronto.** Abrir PR con identidad, objetivo, evidencia y límites. Para cambios rutinarios, el responsable puede fusionarlo cuando las comprobaciones pasan, sin esperar aprobación de otra persona. Si cambia alcance, contratos compartidos o una decisión abierta, acordarlo con los afectados antes de implementar; no es una aprobación obligatoria de todos los PR. Integrar con frecuencia y actualizar main antes de la siguiente tarea.
6. **Cerrar con memoria útil.** Registrar responsable, tarea, resultado, fuentes, pruebas y pendientes en un checkpoint. `project_memory.py` añade automáticamente `Integrante: <id>` desde la sesión válida, sin copiar el correo local; rechaza una sesión cuya rama no coincide. Los registros antiguos sin identidad se conservan como evidencia histórica, sin atribuirlos retroactivamente. Solo el integrador designado publica el contexto consolidado tras integrar. Reunión breve de coordinación cuando existan bloqueos y revisión semanal del proceso para ajustar lo que produzca conflictos.

En GitHub, el propietario puede configurar PR obligatorios, cero aprobaciones y comprobaciones de CI/atribución requeridas, si el plan y la visibilidad lo permiten. No se han modificado esas reglas. Evitar forzar pushes y no convertir la publicación a main en una carrera entre integrantes.

## Plantilla de encargo para IA

```text
Integrante: <id confirmado>
Tarea/issue: <enlace o identificador>
Objetivo y motivo: ...
Archivos/área y dependencias: ...
Criterios de terminado: ...
Fuera de alcance: ...
Verificación esperada: ...
Entrega: diff revisable, evidencia y checkpoint con responsable.
```

## Fundamento y límites de la investigación

Consulta: 2026-11-14. GitHub recomienda [tareas claras, acotadas y con criterios de aceptación, junto con un entorno donde el agente pueda validar](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results). También recomienda [evaluar y probar el resultado generado por IA](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-engineering). Estas fuentes sostienen las prácticas de alcance y verificación; el tablero, los límites de tareas y el flujo sin aprobación externa son una adaptación propuesta para este equipo. No requieren contratar Copilot: pueden aplicarse con las herramientas que ya utilizan.

Estado actual: cinco nombres activos y cuentas confirmadas; Sojo pending por instrucción de Jorge. Pendiente la comprobación personal de cada equipo. Los recibos y el historial Git distinguen preparación, publicación e integración; no se declaran pruebas inexistentes.
