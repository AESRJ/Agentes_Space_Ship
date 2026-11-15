# Incorporación de Sojo — relevo de Adrian

Publicado con el relevo ([ADR-0005](../decisions/0005-relevo-adrian-sojo.md)); preparado por coordinación y revisado contra los scripts del repositorio. La cuenta GitHub de Sojo y su sistema operativo están pendientes de confirmación; no se inventan identificadores ni accesos. Jorge autorizó que Sojo asuma las ocho tareas y el mantenimiento de Adrian. Los commits, PR y registros de autoría anteriores se conservan.

## Qué recibes

| ID | Responsabilidad actual de Sojo | Estado del traspaso |
| --- | --- | --- |
| T007 | Transporte host/cliente y asignación de roles | Implementada por Adrian, integrada; mantener y conocer |
| T008 | Estado de ronda y resultado autoritativo | Implementada por Adrian, integrada; mantener y conocer |
| T009 | Reloj del host y estimación cliente | Implementada por Adrian, integrada; mantener y conocer |
| T011 | Pruebas del contrato de sesión | Implementada por Adrian, integrada; mantener y conocer |
| T013 | Lobby, roles, listo y dificultad | Implementada por Adrian, integrada; mantener y conocer |
| T017 | Intentos validados por el host | Implementada por Adrian, integrada; mantener y conocer |
| **T030** | **Fácil = antena; normal = antena + código** | **Primera tarea de desarrollo**, tras familiarización y acceso; T013/T026 integradas |
| **T035** | Revancha coordinada y ronda nueva limpia | Después de T017/T030; no empezar antes de esa configuración |

También colaboras técnicamente con Gael en T039 (Internet), cuyo dueño sigue siendo Gael. Adrian permanece en el historial como autor anterior, sin asignaciones vigentes. El reemplazo no reabre las seis tareas integradas ni borra su evidencia.

## 1. Accesos previos

1. Da a Jorge tu usuario GitHub exacto. Jorge debe registrar esa cuenta y comprobar/invitar escritura en **AESRJ/Agentes_Space_Ship** y **AESRJ/LaunchControlGodot**. Acepta las invitaciones con tu cuenta; si el repositorio privado da 404, revisa esto antes de instalar.
2. Cada persona usa su propia cuenta y autenticación. No recibir tokens, cookies o llaves de otro integrante.
3. El acceso al cuaderno [Space Ship](https://notebooklm.google.com/notebook/62c97db5-1c82-41bd-a443-2f1f98675ada) se comparte por separado con tu cuenta Google. Es opcional para arrancar el juego: si falla memoria, trabaja con Git y registra el pendiente, sin borrar fuentes del equipo.
4. Ten disponible la herramienta de IA que vayas a usar y tu editor. El juego no requiere C#, .NET ni una API key compartida. No es necesario contratar otra herramienta de IA para compilarlo.

## 2. Instalar requisitos y clonar

Requisitos comunes: Git, Python **3.11+** (3.12 es la versión usada por el CI de agentes) y Godot **4.7.2 stable estándar**, Compatibility. Los scripts del proyecto descargan la versión fijada y comprueban su hash; no descargar otra versión por ser la más reciente.

### Windows 10/11 — PowerShell

Si faltan Git/Python y tienes winget:

```powershell
winget install --id Git.Git --exact
winget install --id Python.Python.3.12 --exact
```

Abre una PowerShell nueva y comprueba `git --version` y `python --version`. Si `python` abre la tienda y tienes el launcher instalado, usa `py -3` para crear el entorno.

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\source\LaunchControlEquipo" | Out-Null
Set-Location "$env:USERPROFILE\source\LaunchControlEquipo"
git clone https://github.com/AESRJ/Agentes_Space_Ship.git
git clone https://github.com/AESRJ/LaunchControlGodot.git
```

Git puede abrir el inicio de sesión de GitHub mediante Credential Manager. Inicia sesión con tu cuenta. Si ya existe un clon, consérvalo, revisa cambios y actualízalo sin reset ni clonarlo encima.

### Linux x86_64 — terminal

Instala con el gestor de tu distribución Git, Python 3.11+ con venv, curl y unzip; verifica sus versiones. Después:

```bash
mkdir -p "$HOME/source/LaunchControlEquipo"
cd "$HOME/source/LaunchControlEquipo"
git clone https://github.com/AESRJ/Agentes_Space_Ship.git
git clone https://github.com/AESRJ/LaunchControlGodot.git
```

Configura autenticación GitHub personal (Credential Manager, GitHub CLI o tu propia llave SSH) si HTTPS no funciona. Nunca pegues un token en una URL ni lo guardes en archivos del repositorio.

## 3. Instalar y comprobar el juego

### Windows

```powershell
Set-Location "$env:USERPROFILE\source\LaunchControlEquipo\LaunchControlGodot"
powershell -NoProfile -ExecutionPolicy Bypass -File tools\Setup-Windows.ps1 -Shortcut
$env:GODOT = Join-Path $env:LOCALAPPDATA 'Programs\Godot\4.7.2-stable\Godot_v4.7.2-stable_win64_console.exe'
powershell -NoProfile -ExecutionPolicy Bypass -File tools\integration_tests.ps1
```

`ExecutionPolicy Bypass` afecta solo esa ejecución. El instalador crea un acceso directo al editor. GODOT se define de nuevo en esta consola porque una variable del proceso hijo no vuelve a PowerShell.

### Linux

```bash
cd "$HOME/source/LaunchControlEquipo/LaunchControlGodot"
tools/setup-linux.sh
export GODOT="$HOME/.local/opt/godot-4.7.2-stable/Godot_v4.7.2-stable_linux.x86_64"
tools/integration_tests.sh
"$GODOT" --path . -e
```

Sobre main `11d649b` (2026-11-15), el CI de GitHub da 43/43 comprobaciones de integración y 21/21 del harness en Linux y Windows. Usa los resultados reales de tu revisión: la cantidad cambia con nuevas pruebas. No presentes un CI remoto como prueba en tu PC.

Abre `project.godot` con el editor y pulsa F5: debe mostrar el lobby. Ejecuta dos instancias en tu PC, una aloja y otra se une a `127.0.0.1`; elige roles diferentes y ambos Listo. Cambia quién aloja y prueba antena/manual/reloj. El juego principal todavía usa puestos provisionales; las escenas 3D publicadas se integrarán en T024.

Para otra ronda reinicia ambas instancias mientras T035 no esté implementada. Esto todavía no demuestra dos PC ni Internet.

## 4. Agentes, identidad, Spec Kit y memoria

El repositorio de agentes conserva planificación y memoria; el juego tiene otro clon. No cambies archivos en el clon equivocado.

Windows, desde `Agentes_Space_Ship`:

```powershell
Set-Location "$env:USERPROFILE\source\LaunchControlEquipo\Agentes_Space_Ship"
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts\validate.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
$env:SPECIFY_FEATURE_DIRECTORY = 'specs/001-launch-control-godot'
.\.venv\Scripts\python.exe .specify\scripts\python\check_prerequisites.py --json --require-tasks --include-tasks
```

Linux, desde `Agentes_Space_Ship`:

```bash
cd "$HOME/source/LaunchControlEquipo/Agentes_Space_Ship"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
export SPECIFY_FEATURE_DIRECTORY=specs/001-launch-control-godot
.venv/bin/python .specify/scripts/python/check_prerequisites.py --json --require-tasks --include-tasks
```

Las skills Spec Kit ya están versionadas en `.agents/skills/`, con scripts en `.specify/`; no hay que reinstalarlas desde otro GitHub. Lee `AGENTS.md` y `docs/team-workflow.md`. Cada conversación empieza con **«Soy Sojo»**, incluso en otra PC o con otra IA. Si usas Claude y no tiene comandos Spec Kit instalados, pídele leer el SKILL.md correspondiente; no supongas que un comando slash existe.

Para una sesión de documentación en agentes, usa el correo exacto de commits de tu cuenta (puede ser el noreply mostrado en GitHub → Settings → Emails):

```powershell
python scripts/team_session.py start --member sojo --task incorporacion --email "TU_CORREO_DE_COMMITS_GITHUB"
python scripts/team_session.py status
```

En Linux puedes usar `python3`. El comando crea `sojo/incorporacion` en **agentes**; no crea ni identifica una rama en el juego.

Memoria opcional, con acceso Google propio: Windows puede usar el instalador existente `powershell -NoProfile -ExecutionPolicy Bypass -File .\Setup-Windows.ps1 -Login`; Linux puede ejecutar `.venv/bin/python -m playwright install chromium`, `.venv/bin/notebooklm login` y `.venv/bin/python scripts/configure_codex.py`. Si ya hay configuración local propia, no la sobrescribas.

Después consulta `scripts/project_memory.py status` con el Python de la venv. Si falla el servicio o la capacidad, conserva registros en Git y reporta pending. Los fallos recientes de sincronización del equipo no se solucionan compartiendo credenciales o borrando fuentes sin acuerdo. No ejecutes `publish` simultáneamente con el coordinador.

## 5. Tu primera rama del juego

Cuando hayas comprobado acceso, versión y baseline, en el clon **LaunchControlGodot** con el árbol limpio:

```bash
git switch main
git pull --ff-only
git switch -c sojo/t030-dificultades
git config --local user.name "Sojo"
git config --local user.email "TU_CORREO_DE_COMMITS_GITHUB"
git config --local commit.template .gitmessage
```

Lee T030, `spec.md`, `data-model.md`, `contracts/session.md`, `autoload/session_service.gd`, `round_controller.gd`, `server_clock.gd`, las dificultades y las pruebas existentes. Conserva el código anterior de Adrian; aprende sus rutas y señales antes de cambiar contratos.

T030 debe conectar fácil con una antena y normal con antena+código, rechazando cambios durante la ronda. El controlador del baseline solo registra antena y fácil; coordina el registro de la regla de código y las definiciones necesarias. Normal no debe ganar al resolver un solo módulo. Registra parámetros propuestos como tales y prueba ambas modalidades con host torre y astronauta. No hagas por tu cuenta T028/T029 de Isra ni T031 de Jorge.

No escribas el estado de Kevin como aceptado: T019 mantiene una incidencia GUI en el informe vigente, aunque T013 y T026 ya están integradas y permiten preparar la configuración de T030. T035 espera T030 y trata ronda nueva, limpieza de readiness/estado/comandos antiguos y reloj nuevo; no se implementa con un simple botón que oculta el resultado.

## 6. Publicar cambios con tu nombre

En el juego, selecciona solo los archivos de tu tarea y crea commits con tu identidad local:

```bash
git diff
git add RUTAS_DE_TU_TAREA
git commit -m "[sojo] T030: configura dificultades" --trailer "Team-Member: sojo" --trailer "AI-Assisted: true"
git push -u origin sojo/t030-dificultades
```

Abre un PR hacia main con tarea, archivos, cómo probar, SHA, resultados y límites; espera CI Linux/Windows. En agentes usa `python scripts/team_session.py commit -m "..."` después de preparar sus propios archivos. No invoques esa herramienta desde otro clon suponiendo que cambia su raíz: actúa sobre el repositorio donde está el script.

No fuerces pushes ni subas `.godot/`, `.venv/`, sesiones locales, tokens, cookies o direcciones privadas. Para tocar una escena de otro integrante acuerda antes el alcance. Actualiza el estado con evidencia y entrega notas de memoria al coordinador.

## Mensaje inicial para tu IA

> Soy Sojo. Asumo las ocho responsabilidades transferidas de Adrian por Jorge. Lee AGENTS.md, el reparto y el registro del traspaso. Primero verifica mi acceso, versión de Godot y baseline; después trabaja solo T030 en mi rama. Usa Spec Kit, conserva autoría histórica y autoridad del host. No rehagas T007/T008/T009/T011/T013/T017, ya integradas; no marques T019 aceptada. Entrega un PR pequeño con pruebas y evidencia. T035 será después de T030.

## Lista de incorporación

- Cuenta GitHub confirmada, invitaciones aceptadas y ambos repositorios clonados.
- Godot 4.7.2 estándar importando y F5 funcionando en tu equipo.
- Comprobador e integración ejecutados localmente con resultados guardados.
- Identidad Sojo y correo personal de commits configurados por clon.
- Spec Kit localizable y dependencias T030 entendidas.
- Rama `sojo/t030-dificultades`, un escritor por archivo y ningún cambio en main directo.
- NotebookLM accesible o pendiente explícito, sin bloquear el desarrollo con Git.

Esta guía no se ha ejecutado en el PC de Sojo: sus comandos se revisaron contra `tools/` del juego y `scripts/` de agentes. Comunica a Jorge o al coordinador cualquier paso que falle en tu sistema.
