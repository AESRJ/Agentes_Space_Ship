# Agentes Space Ship

Centro de agentes, investigación, diseño y memoria para seis integrantes. El videojuego se implementará después en otro repositorio. Aquí empezamos por nutrir y validar la idea.

## Incorporación desde Windows

Necesitas acceso a este repositorio, una cuenta con Codex y acceso al [cuaderno compartido](https://notebooklm.google.com/notebook/62c97db5-1c82-41bd-a443-2f1f98675ada). El propietario comparte el cuaderno por separado con cada integrante; clonar GitHub no concede permisos en Google.

Con Git instalado, abre PowerShell:

```powershell
git clone https://github.com/AESRJ/Agentes_Space_Ship.git
cd Agentes_Space_Ship
powershell -NoProfile -ExecutionPolicy Bypass -File .\Setup-Windows.ps1 -InstallPrerequisites -Login
```

También puedes descargar `Setup-Windows.ps1` desde GitHub y ejecutarlo fuera del repositorio: instalará Git/Python si faltan y clonará en `$env:USERPROFILE\source\Agentes_Space_Ship`. Usa `-Destination 'C:\ruta\Agentes_Space_Ship'` para otro destino. Si se ejecuta dentro de un clon usa ese clon. El acceso privado por HTTPS se autentica con Git Credential Manager; `-Transport SSH` utiliza una llave que ya hayas configurado.

El script requiere Python 3.11+, crea `.venv`, instala dependencias, genera `.codex/config.toml` local, permite iniciar sesión en Google y comprueba acceso real al cuaderno. No instala Codex: abre el repositorio con tu aplicación/CLI de Codex ya instalada y autenticada. `ExecutionPolicy Bypass` solo afecta esa ejecución, no cambia la política permanente de Windows. Revisa el script antes de ejecutarlo.

Para configurar identidad Git solo en este repositorio, añade `-GitName 'Tu nombre' -GitEmail 'Tu correo GitHub'`. No se copian identidades, claves SSH ni cookies entre compañeros. El script no hace pull sobre cambios existentes ni altera configuración global de Codex.

Abre una sesión nueva de Codex desde la carpeta del repositorio y acepta su confianza cuando la aplicación lo pida. Deben aparecer seis agentes y el MCP `space_ship_memory`. Prueba:

> Consulta la memoria de Space Ship, lee la visión y el alcance actuales y resume las decisiones abiertas. No implementes el juego.

Si falta Python o Git después de instalar, abre otra PowerShell y repite. Si Google rechaza acceso, el propietario debe compartir el cuaderno y después repites con `-Login`. Si falta el MCP, reinicia Codex y revisa la confianza del proyecto. Si ya existe configuración propia en `.codex/config.toml`, el instalador se detiene sin sobrescribirla: integra manualmente el bloque del servidor que produce `scripts/configure_codex.py`.

## Agentes

| Perfil | Uso |
| --- | --- |
| coordinacion | Delimitar tareas, dependencias y alcance |
| investigacion | Fuentes científicas/técnicas y límites de fidelidad |
| diseno | Puzzles cooperativos, niveles y contratos |
| implementacion | Herramientas autorizadas y cambios según especificación |
| pruebas | Comportamiento, integración y evidencia |
| memoria | Checkpoints, decisiones y coherencia del contexto |

Los perfiles heredan el modelo y permisos de la sesión; no requieren un modelo concreto. Los agentes no son servicios siempre encendidos: cada persona los usa desde su sesión con los mismos archivos versionados. [Configuración oficial de subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Ejemplos:

> Usa investigacion para proponer fenómenos verificables que puedan sustentar un puzzle de lanzamiento. Entrega fuentes, simplificaciones y preguntas abiertas.

> Usa diseno para convertir la investigación aprobada en una ficha de puzzle. Mantén como propuestas las reglas que aún no hayamos decidido.

> Usa pruebas para revisar si ambos roles son necesarios y si las consecuencias del puzzle coinciden con la ficha.

## Memoria recurrente

La skill `space-memory` y `AGENTS.md` indican consultar memoria al iniciar y guardar tras cada decisión, hito, bloqueo o cierre. `memory_checkpoint` escribe un registro durable y lo sube por MCP. Si falla, devuelve `pending`; `memory_sync` reintenta. `memory_publish_context` publica una instantánea identificada por hash y revisión Git; designen un integrador para esa operación.

No es un proceso permanente ni guarda cada mensaje automáticamente: el agente ejecuta el procedimiento durante la sesión. Conservamos resúmenes útiles, fuentes y evidencia, no chats completos. Los registros locales se comparten en Git mediante commit/push; las fuentes subidas ya se pueden consultar en el cuaderno, pero se distinguen de lo integrado en main.

CLI de recuperación (PowerShell):

```powershell
.\.venv\Scripts\python.exe scripts\project_memory.py status
.\.venv\Scripts\python.exe scripts\project_memory.py sync
.\.venv\Scripts\python.exe scripts\project_memory.py publish
.\.venv\Scripts\python.exe scripts\project_memory.py ask 'Que decisiones siguen pendientes?'
```

Git conserva versiones verificables; NotebookLM ayuda a recuperar contexto con referencias. Las respuestas del cuaderno no aprueban propuestas ni sustituyen los documentos vigentes. Las fuentes antiguas se conservan; no hay borrado automático al llegar a límites.

## Flujo del equipo

1. Actualizar main sin cambios locales y crear rama por tarea.
2. Leer [visión](docs/vision.md), [alcance](docs/scope.md), [estado](docs/state.md) y consultar NotebookLM.
3. Trabajar en el encargo; un escritor por archivo/escena.
4. Guardar checkpoint, verificar herramientas o diseño y abrir PR con evidencia.
5. Revisar e integrar; el integrador publica el contexto consolidado.

Ejemplo de rama: `git switch -c diseno/puzzle-001`. Antes de empezar, `git pull --ff-only` en main; si hay divergencias o cambios locales, resolverlos sin reset forzado.

La protección de main, revisores y permisos del equipo se configuran en GitHub cuando estén identificados los integrantes; este repositorio no presupone esas protecciones activadas.

## Verificar herramientas

```powershell
.\.venv\Scripts\python.exe scripts\validate.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

GitHub Actions contiene validación en Linux y Windows sin credenciales de Google. El login y el acceso real a NotebookLM se comprueban en cada equipo. Una ejecución de CI no prueba por sí sola el login interactivo de Windows.

## Linux/macOS

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/notebooklm login
.venv/bin/python scripts/configure_codex.py
.venv/bin/python scripts/project_memory.py status
```

Abre Codex en este repositorio y reinicia la sesión para cargar la configuración.

## Traspaso al repositorio del juego

```powershell
.\.venv\Scripts\python.exe scripts\export_project.py --output ..\space-ship-contexto
```

Genera un paquete revisable de documentos con revisión Git y hashes. No crea repositorios ni despliega. Cuando se acuerde el repositorio del juego, se incorpora allí el contexto seleccionado y se registra su URL en `memory/notebook.json`; este repositorio sigue conservando la historia de decisiones.

## Procedencia

MCP adaptado de [NotebookLM for Codex — knowingdoing](https://github.com/knowingdoing/notebooklm-codex), revisión `574caf973e4f7bc4ad002a0098e4cd3144618c02`, licencia MIT incluida. Consulta [cambios y límites de la adaptación](integrations/notebooklm/README.md). La automatización usa notebooklm-py no oficial y cada persona conserva su propia autenticación local.
