# Auditoría de ramas y flujo — Launch Control (2026-11-14)

> Informe histórico del 2026-11-14. Sus siguientes tareas y límites describen aquel corte; para el estado vigente consultar `docs/state.md` y `specs/001-launch-control-godot/status.md`. Se conserva la evidencia de autoría y pruebas, sin restaurar los estados antiguos del índice.

Encargo explícito de Jorge: revisar todas las ramas de `AESRJ/LaunchControlGodot` y `AESRJ/Agentes_Space_Ship`, verificar especificación y flujo, y fusionar a main solo lo conforme y probado, en orden de dependencias. Auditor: Claude (Claude Code), actuando por Jorge. Las herramientas de auditoría (orquestador de pruebas, flujo multiproceso, integración verificada por blobs) son locales y no se versionan; sus resultados se resumen aquí, sin rutas personales ni direcciones de red.

## Juego — `AESRJ/LaunchControlGodot`

| Orden | Rama / PR | Tarea · autor | Cabecera revisada | Dependencias | Archivos propios | Pruebas ejecutadas por mí (Linux) | CI de la cabecera | Decisión → commit en main |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | `kevin/t005…` #5, `t010` #6, `t014` #7 | T005/T010/T014 · Kevin | (fusionadas por Kevin antes de la auditoría) | T002 / T005 / T010 | `resources/modules/`, `scripts/modules/` | `test_module_definition`, `test_module_runtime`, `test_antenna_rule`: OK en la línea base y en cada paso | — | **CUBIERTA**: `5cb6fd6`, `0d81ddf`, `1c2e421`. Ramas ya borradas. Sin revisión de código profunda en esta auditoría; sus pruebas se ejecutaron en cada paso |
| — | `jorge/t003-harness-smoke` #2 | T003 · Jorge | `11bab3a` | T002 | `harness/`, `tools/` | 21/21 en cada paso | 43652062713 | **CUBIERTA**: `3cf3de7`. La rama remota se conserva (sin borrados manuales) |
| 1 | `adrian/t007-session-service` #9 | T007 · Adrian | `95e3c2b` | T002 | `autoload/session_service.gd`, `autoload/tests/` | `session_loopback` con 3 procesos: emisor tomado del transporte (el payload falso `sender:1/tower` se ignora), rol ocupado rechazado, tercer proceso rechazado, desconexión | verde | **FUSIONADA** → `793349d` |
| 2 | `adrian/t008-round-controller` #10 | T008 · Adrian | `8366b1b` | T007 | `autoload/round_controller.gd` | `round_controller_test` (duplicados, inactivos, resultado inmutable, rondas y revisiones viejas, `round_finished` único, interrupción) + T007 | verde | **FUSIONADA** → `2122152` |
| 3 | `adrian/t009-server-clock` #11 | T009 · Adrian | `3cae3b5` → `bf108e0` (*) | T008 | `autoload/server_clock.gd` (+ `round_controller`) | `server_clock_test` + **mutante `>=`→`>` detectado** (5 fallos, exit 1) + anteriores | 43654332055 | **FUSIONADA** → `0725d02` |
| 4 | `adrian/t013-lobby` #12 | T013 · Adrian | `0740864` → `6a22486` (*) | T007, T008 | `scenes/lobby/`, `round_controller` | `lobby_rules_test` + `lobby_loopback` con 2 procesos (torre rechazada por ocupada; ronda 1 easy → [antenna] y 180 s en ambos) | 43654495121 | **FUSIONADA** → `c700753` |
| 5 | `adrian/t011-session-contract-runner` #13 | T011 · Adrian | `878b719` → `21abe70` (*) | T007, T008, T009 | `harness/session_contract_runner.gd` | runner 17/17 (ROL/REV/EXP/INT). `ERROR unknown peer ID 4242` documentado como esperado | 43654597926 | **FUSIONADA** → `bfebc54` |
| 6 | `adrian/t017-submit-attempt` #15 | T017 · Adrian | `8263706` → `8b4959f` (*) | T009, T013, T014 | `autoload/*`, `harness/session_contract_runner.gd` | `attempt_loopback` con 2 procesos (host torre: not_allowed, sin pista; cliente: wrong, duplicado, stale, invalid, success, stale tras el final) + runner 24/24 + **flujo de auditoría** (host astronauta, timeout real, caída de cliente y de host) + **mutante sin comprobación de rol detectado** | 43654717353 | **FUSIONADA** → `36f8386` |
| 7 | `gael/t004-guia-visual` #3 | T004 · Gael | `8cf1ad2` | T002 | `docs/art/visual-guide.md` | documento: criterio de T004 (lista de recursos y bocetos de ambos puestos), coherencia con el contrato, referencias no copiadas | verde | **FUSIONADA** → `824784a` |
| 8 | `gael/t015-antenna-view` #4 | T015 · Gael | `6b3edaf` | T004, T010 | `scenes/modules/antenna_view*`, `assets/icons/` | `antenna_view_check` OK; captura con ventana a 1280×720 (pendiente / listo-bloqueado) con `visual_measurement_valid`; fixture con luz inválida → exit 1; **flujo `view_flow`**: vista real conectada a la sesión y la regla reales (error → pendiente, acierto → solved y bloqueada) | verde | **FUSIONADA** → `890c192`. Observación menor: el destello «NO» de un error anterior puede verse hasta 1 s tras el éxito |
| 9 | `isra/t006-manual-outline` #8 | T006 · Isra | `dea8c92` | T002 | `docs/manual/content-outline.md` | documento: dos filas de antena, tabla propia de código, aritmética 22..99 y 484..9801 verificada, coherente con `antenna_rule` y `manual_section_id` | verde | **FUSIONADA** → `d7ac177` |
| 10 | `isra/t016-antenna-page` #14 | T016 · Isra | `5168497` | T006 | `ui/manual/antenna_page.tscn` | página estática sin scripts ni sesión; captura con ventana a 1280×720 válida; regla igual a la de Kevin | verde (mismo SHA; la base pasó de `isra/t006` a `main` tras #8) | **FUSIONADA** → `10241ca`. Observaciones: tema oscuro frente al fondo claro de la guía; rótulos de ~13 px frente a los 18 px propuestos |
| — | `gael/t020-cockpit` #16 | T020 · Gael | `233f796` | T004, **T019** | `scenes/cockpit/`, fixture | `cockpit_check` OK; la simulación no rompe nada (16/16) | verde | **BORRADOR**: no se fusiona. Sigue siendo borrador y T019 no existe |
| — | `gael/t021-tower` #17 | T021 · Gael | `b9272a5` | T004, **T020** | `scenes/tower/`, fixture | `tower_check` OK; simulación 16/16 | verde | **BORRADOR**: no se fusiona. Apilada sobre #16 |

(*) Merge de integración de Jorge añadido a la rama del autor (solo avance, sin reset ni force push). Los squash crean commits nuevos, así que cada rama apilada de Adrian chocaba en add/add con su propio contenido ya integrado. El script de integración solo hace commit y push si:
1. los archivos en conflicto en `main` tienen el mismo blob que el commit previo de la cadena;
2. el delta resultante frente a `main` es exactamente `previo..cabecera`;
3. esos archivos tienen el mismo blob que la cabecera del autor.

No hay cambios de comportamiento.

## Agentes — `AESRJ/Agentes_Space_Ship`

| Rama | Estado frente a main | Contenido | Decisión |
| --- | --- | --- | --- |
| `jorge/liberar-equipo` (#7), `jorge/launch-control-godot` (#6), `kevin/registra-cuenta-github` (#5), `jorge/identidad-y-flujo-ia` (#3), `plan/unity-base` (#1) | ancestros de main, 0 commits por delante | ya integradas | **CUBIERTAS** |
| `desarrollo` (`c2c38a0`, Kevin) | ancestro de main, 0 por delante | sin aportación pendiente | **CUBIERTA** |
| `adrian/registra-cuenta-github` (`d712170`) | 1 por delante, 9 por detrás, sin PR | registra `adrianbalderas373488` | **CUBIERTA en lo esencial**: main ya tiene la cuenta (registro de cinco activos de Codex). Fusionarla retrocedería `state.md` y `team-workflow.md` («faltan tres cuentas»). Solo su registro de sesión `docs/sessions/2026-11-14-adrian-cuenta-github.md` no está en main: lo puede incorporar Adrian o Codex si se quiere como procedencia |
| `gael/documenta-contexto-juego` (`acb63d2`) | 2 por delante, 11 por detrás, sin PR | visión ampliada (+418 líneas), PUZ-001/PUZ-002, sesiones del prototipo Unity y un bloque nuevo al principio de `state.md` | **NO CONFORME**: presenta Unity/C# como elección vigente y prototipos locales en `state.md`, en contra de la decisión de Godot (ADR-0003) y del alcance actual. Dueño: Gael. Acción: rebasar sobre main, marcar lo de Unity como histórico y separar lo aprovechable (PUZ-001/002 como investigación) en un PR |

## Incidencias de procedimiento (mías)

1. **`bf108e0`**: hice el push antes de que la verificación pasara. Mi comparación textual de diffs dio un falso «DIFIERE» por formato y no condicioné el commit a ella. Comprobé después por blobs que el resultado era exactamente el delta de T009. Desde entonces el push está condicionado .
2. **`21abe70`** (T011): el merge de integración no era necesario (no había conflicto), aunque es inocuo.
3. **#3 (`824784a`)**: el `Co-authored-by` del mensaje lleva un correo noreply supuesto para Gael. La autoría real del commit es correcta (su correo de commits). No se reescribe `main`. En las fusiones siguientes los correos salen de los commits de cada autor.
4. Primer intento de `gh pr merge 9` con SHA abreviado: GitHub lo rechazó sin efecto.

No hubo ninguna denegación de permisos en esta auditoría.

## Qué ejecuté, qué declara el autor y qué no se pudo probar

| # | Punto del encargo | Ejecutado por mí (evidencia) | Solo declarado / no probado |
| --- | --- | --- | --- |
| 1 | Arranque limpio | `rm -rf .godot` + importación headless, exit 0; `tools/check.sh` con las 21 regresiones de T003; CI de main en Linux y Windows en verde en los 10 commits nuevos (runs 43654181506 … 43655478917) | El CI de Windows solo ejecuta `check.ps1`: **las pruebas de red, ronda y módulos no se han ejecutado en Windows**. Sin prueba GUI en el PC de Jorge |
| 2 | Sesión con procesos separados | `session_loopback` con 3 procesos: emisor del transporte, payload falso ignorado, rol exclusivo, tercer proceso rechazado («sesión llena»), desconexión. Host como **torre** (pruebas del autor) y como **astronauta** (`host_astronaut`, mía) | Solo **loopback 127.0.0.1**: no es LAN ni Internet (T039) |
| 3 | Lobby y ronda | `lobby_loopback` con 2 procesos: no empieza con un solo listo, la dificultad del cliente se ignora, empieza con los dos listos; ronda 1, easy → [antenna], 180 s. `round_controller_test` y runner REV-01..04: revisión creciente, rondas y revisiones viejas rechazadas | La dificultad «normal» no existe (T030): se muestra deshabilitada como pendiente |
| 4 | Reloj | `server_clock_test` + EXP-01..04: timeout en el cero exacto antes de una resolución, ticks sin revivir la ronda, estimación del cliente solo visual. Mutante `>=`→`>` detectado. Flujo `timeout` (ronda de 2 s, procesos separados): `timeout` en ambos, estimación del cliente = 0, intento tardío → `expired` | Diferencia visual ≤1 s entre equipos sin medir (T019/T039). Aún no hay HUD que mostrar ni cambiar de página |
| 5 | Antena y manual | `attempt_loopback`; flujo `view_flow`: **la vista real de Gael** emite `attempt_requested` → `submit_attempt` → `AntennaRule` de Kevin en el host → `wrong` deja pendiente → acierto → `solved` y vista bloqueada. La página del manual de Isra da la misma regla (fija→luna, parpadeante→estrella) | La composición productiva (T012/T018) **no existe**: el cableado vista↔sesión de `view_flow` es solo de la auditoría y no se publicó |
| 6 | Permisos y asimetría | La torre (host o cliente) recibe `not_allowed` y **0 mensajes de pistas**; las acciones locales del host pasan por la misma validación (`host_astronaut`); módulo inactivo → `inactive` (runner). Mutante sin comprobación de rol detectado por mi flujo | Con `config.seed` (solo en pruebas) la semilla llega a la torre en el snapshot: observación menor |
| 7 | Mensajes adversos | `command_id` duplicado (misma respuesta, sin efecto), payload inválido, ronda vieja (`stale`), intento tras el final, revisiones repetidas o viejas, mensaje tardío tras terminal (runner EXP-04, REV-02..04) | — |
| 8 | Fallo e interrupción | Flujo `timeout`; `client_drop` y `host_drop`: `interrupted` una sola vez en ambos lados; desconexión tras el final sin cambiar `success` (`host_astronaut`) ni `timeout`; runner INT-01..04 | No hay pantalla de interrupción (T033/T034) |
| 9 | Presentación real | Capturas con ventana, `--fixed-viewport`, 1280×720, `visual_measurement_valid:true`, 60 FPS (vsync), en una Iris Xe: placa de antena (pendiente con LUNA seleccionada; LISTO ✓ bloqueada) y página del manual. Color siempre con forma y texto | La placa sola no tiene cámara (se mostró dentro de la demo de Gael mediante una escena temporal no versionada). Cabina y torre (#16/#17) son borradores. No hay prueba de ratón real en el puesto completo |
| 10 | Repetición y fases posteriores | — | Revancha y retorno al lobby (T035), dificultad normal (T030), código (T026), calculadora y HUD (T022/T023/T028) **no existen**. **No hay ronda completa jugable**: falta T012/T018 |

## Ejecución final en el clon nuevo de `main` `10241ca`

```
batería completa (clon nuevo)      → 16 PASS / 0 FAIL
  import limpio; tools/check.sh (21 casos); test_antenna_rule; test_module_definition;
  test_module_runtime; round_controller_test; server_clock_test; lobby_rules_test;
  session_contract_runner (24/24); session_loopback [host, client, extra];
  lobby_loopback [host, client]; attempt_loopback [host, client]
antenna_view_check                       → OK
flujo de auditoría (5 escenarios × 2 procesos) → 10/10 PASS
pgrep Godot                              → sin procesos colgados
```

## Validación de las pruebas (no tautológicas)

- `server_clock_test` contra el mutante `is_expired: now > deadline`: 5 fallos, exit 1.
- `audit_flow` contra el mutante sin `role_of(sender) != astronaut`: falla `host_astronaut [client]` («torre pudo intentar»).
- Las regresiones T003 contra la cabecera anterior `105a1e7`: 5/21 (registro anterior).

## Brechas que deja el flujo

1. **T012 (Jorge)** ya tiene todas sus dependencias integradas (T007–T010). Sin ella no hay escena principal compuesta ni autoloads registrados en `project.godot`, y nadie llama a `submit_attempt` desde la vista en el juego real.
2. El CI no ejecuta las pruebas de Adrian ni de Kevin. Se recomienda que Jorge añada a `tools/check.*` un ejecutor de pruebas, de modo que haya evidencia también en Windows.
3. LAN e Internet (T039), dos equipos (SC-006), HUD y presentación de desenlaces: pendientes por diseño de fases.
