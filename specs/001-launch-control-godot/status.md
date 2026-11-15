# Estado operativo — Launch Control

Actualizado: 2026-11-15 (T024 integrada y liberación de T025). No sustituye criterios de aceptación ni declara terminado el juego.

## Actualización — T030 integrada y T035 en revisión (Sojo, 2026-11-15)

T030 se fusionó en el juego mediante [PR #44](https://github.com/AESRJ/LaunchControlGodot/pull/44) (`404fc5a`), lo que libera T035 (dependencias T017 y T030 integradas). T035 está implementada en la rama `sojo/t035-revancha` sobre main `cf79aab`; Sojo revisó el diff y abrió el [PR #49](https://github.com/AESRJ/LaunchControlGodot/pull/49), sin fusionar. Evidencia local y límites: `docs/qa/t035-revancha.md` en esa rama. T037 y T039 siguen pendientes.

## Estado vigente — relevo de Adrian por Sojo (2026-11-15)

**Decisión de Jorge ([ADR-0005](../../docs/decisions/0005-relevo-adrian-sojo.md)):** Sojo asume T007, T008, T009, T011, T013, T017, T030 y T035, más el apoyo técnico en T039 (dueño: Gael). Adrian queda inactivo y conserva la autoría de lo que implementó. Reparto: Jorge 9, Gael 9, Sojo 8, Kevin 8 e Isra 8. Sojo usa **Sojito312**, confirmado por Jorge y con escritura comprobada por API en ambos repositorios. Su reporte de entorno no sustituye la prueba visual propia, todavía pendiente. Guía: [docs/setup/sojo.md](../../docs/setup/sojo.md).

Juego comprobado: main `d4cbdb36e091e483861f5f2e6b6763cec01786f6`. T024 fusionada en [PR #37](https://github.com/AESRJ/LaunchControlGodot/pull/37), cabecera revisada `49c3847`. CI 43752123390: 46/46 integración y 21/21 harness en Linux/Windows. Codex verificó el mismo código de producción localmente (46/46, 21/21 y runner de Kevin con ambos roles), y la corrección gráfica final en 20/20 procesos; luces fija/parpadeante, desconexiones y retorno al lobby. Claude registró además 32/32 procesos gráficos, con y sin carga. Windows GUI, F5 humano, dos PC/Internet y FPS finales no acreditados. Entregas integradas desde el estado anterior:

| Entrega | PR | Commit | Nota |
| --- | --- | --- | --- |
| T020 cabina (Gael) | #16 | `adae9b3` | rediseño #32 integrado en `a5ecf97` |
| T021 oficina (Gael) | #17 | `46e07e4` | — |
| T019 evidencia de QA (Kevin) | #24 | `d02f979` | **no aceptada**: runner corregido en #37; Kevin debe repetir y aceptar Q01–Q05 |
| Issue #23: interrupción visible (Jorge) | #25 | `36a0efc` | relacionado con Q05; el issue sigue abierto |
| T026 regla de código (Kevin) | #26 | `71f3fc2` | — |
| T027 placa de código (Kevin) | #27 | `c2b8b88` | — |
| T036 reinicio de módulos (Kevin) | #28 | `b548759` | no implica revancha (T035) |
| README de escenas (Gael) | #31 | `961d642` | — |
| T022/T023 manual y HUD (Isra) | #34 | `11d649b` | — |
| T028/T029 página de código y calculadora (Isra) | #33 | `e54858e` | integradas, sin aceptar T019 |
| Rediseño de T020/T021 (Gael) | #32 | `a5ecf97` | integrado |

T024 #37 fusionada en `d4cbdb3`. #29 (T033, `15b0e90`) y #39 (T034, `ab197bf`) se fusionaron por Gael durante la revisión. #30 cerrada sin fusionar, sustituida por #39. Son escenas adicionales sin cableado en main; no acreditan T025 ni Q11–Q12/T037. Se conserva su aceptación pendiente y sus dependencias. #32 y #33 están fusionados. PR #8 de agentes queda fuera de alcance.

| Persona | Siguiente | Dependencia real |
| --- | --- | --- |
| Sojo | T030 integrada: fácil = [antenna], normal = [antenna, code] | [#44](https://github.com/AESRJ/LaunchControlGodot/pull/44) `404fc5a` |
| **Sojo** | **T035**: revancha y ronda limpia, PR [#49](https://github.com/AESRJ/LaunchControlGodot/pull/49) abierto, sin fusionar | T017 y T030 integradas. No acredita Q11–Q12 (T037, Gael) ni Internet (T039) |
| Kevin | T019: repetir y aceptar Q01–Q05 con el runner actualizado en #37 | — |
| Isra | T032 después de T031; T028/T029 ya integradas (#33) | T031 pendiente |
| Jorge | T031: integración de dificultad y segundo módulo | T030 de Sojo pendiente; T024 y T027–T029 integradas |
| Gael | **T025 liberada**: Q06–Q07 y FPS en equipos identificados | T024 integrada en #37 |

Las seis tareas que implementó Adrian se mantienen, no se reimplementan. **T030 está técnicamente liberada para Sojo** sobre T013/T026 integradas; esto no equivale a aceptar T019 ni cambiar su responsable. [Decisión y alcance](../../docs/setup/t030-inicio-sojo.md).

## Estado anterior — corte de antena integrado (2026-11-14)

Juego: main **`29fe8cab0c544f0af58dc58116d7db94b8723643`** (PR #22). CI de main 43688574914: **36 PASS / 0 FAIL en Linux y Windows** (runners de GitHub). T003–T018 están integradas:

| Tarea | Dueño | PR | Commit en main |
| --- | --- | --- | --- |
| T003 harness | Jorge | #2 | `3cf3de7` |
| T004 guía visual | Gael | #3 | `824784a` |
| T005 ModuleDefinition | Kevin | #5 | `5cb6fd6` |
| T006 esquema del manual | Isra | #8 | `d7ac177` |
| T007 transporte | Adrian | #9 | `793349d` |
| T008 ronda | Adrian | #10 | `2122152` |
| T009 reloj | Adrian | #11 | `0725d02` |
| T010 ModuleRuntime | Kevin | #6 | `0d81ddf` |
| T011 runner de contrato | Adrian | #13 | `bfebc54` |
| T012 composición y autoloads | Jorge | #21 | `349282c` |
| T013 lobby | Adrian | #12 | `c700753` |
| T014 regla de antena | Kevin | #7 | `1c2e421` |
| T015 placa de antena | Gael | #4 + corrección H-04/H-05 #20 | `890c192`, `ca8515c` |
| T016 página de antena | Isra | #14 | `10241ca` |
| T017 submit_attempt | Adrian | #15 | `36f8386` |
| T018 corte vertical de antena | Jorge | #22 | `29fe8ca` |

**Sustitución temporal autorizada:** con autorización explícita de Jorge, Jorge adaptó **solo** las siete pruebas de Adrian (T008, T009, T011, T013, T017) para convivir con los autoloads de T012, en #21. Esas pruebas reutilizan el nodo existente y conservan su lógica y sus aserciones (`docs/qa/t012-adaptacion-pruebas.md` del juego). Adrian conserva sus componentes y sus tareas restantes.

**Evidencia de T018:** dos procesos en loopback con la escena principal real y ambos roles de host (solve, timeout, adversarial y drop; H-04 como aserción). Recorrido GUI con ventana y eventos sintéticos en Linux. Detalle en `docs/qa/t018-corte-antena.md` del juego.

**No acreditado:** F5 manual por una persona, Windows con interfaz gráfica, dos PC, LAN e Internet (T039). Solo hay loopback y CI headless.

| Persona | Siguiente | Dependencia real |
| --- | --- | --- |
| **Kevin** | **T019: Q01–Q05 con ambos roles de host** → `docs/qa/antenna-round.md` del juego; guía `docs/qa/t019-guia-kevin.md` | **liberada** (T011 y T018 integradas) |
| Gael | T020 cabina; después T021 torre | T019 aceptada; #16/#17 siguen como borradores y no se fusionan antes |
| Isra | T022 foco y navegación del laptop; después T023 HUD | T019 (T022); T022 (T023) |
| Kevin | T026 regla de código | T019 |
| Adrian | T030 dificultades | T013 y T026 |
| Jorge | T024 integración de puestos finales | T020, T021, T022 y T023 |

T001/T002: base técnica publicada; conservan el seguimiento de la prueba GUI personal de Jorge y de la aceptación final. Sojo no está incorporado.

## Historial

### Base que libera el arranque (histórico)

T001/T002: **base técnica publicada** en https://github.com/AESRJ/LaunchControlGodot, main `0ec8b6ac0fffa864f7549dd95f871efa96a12d58`, PR #1. CI Linux/Windows aprobado y comprobación Linux independiente OK. Los cinco activos tienen escritura. La prueba GUI del Windows personal de Jorge sigue como seguimiento; Sojo no está incorporado. Ninguno de esos seguimientos bloquea a los activos con base accesible.

Esta liberación técnica satisface el requisito previo de arranque de T003/T004/T005/T006/T007 aunque las casillas originales T001/T002 conserven seguimiento de aceptación final.

| Persona | Siguiente tarea | Estado real |
| --- | --- | --- |
| Jorge | T003: harness | PR #2 fusionado por solicitud explícita de Jorge; commit 3cf3de7, CI Linux/Windows aprobado para cabecera 11bab3a; no acredita puestos reales |
| Gael | T004: guía visual | liberada; sin evidencia de implementación aún |
| Adrian | T007: transporte | liberada; sin evidencia de implementación aún |
| Kevin | T005: definición de módulo | liberada; sin evidencia de implementación aún |
| Isra | T006: contenido de manual | liberada; sin evidencia de implementación aún |

## Cierre de integración de T003

PR #2 fusionado con squash el 2026-11-14T23:19:38Z en `3cf3de79f9dd360013a4ed8fa41a27a81e6b7482`, con autorización explícita de Jorge y CI Linux/Windows 43652062713 aprobado para cabecera `11bab3a`. El historial siguiente corresponde a la revisión anterior, no a un bloqueo de fusión actual.

## Revisión anterior de T003 — historial

Cabecera revisada: `105a1e7d37aa0dc8dd0184ee57c3fc5d1c30113b`, PR #2 abierto. CI de esa revisión en verde, pero casos independientes detectan éxito falso cuando no se escribe registro, argumento frames inválido que no termina y resolución headless falsamente validada. Ver [revisión](../../docs/reviews/2026-11-14-claude-base-y-harness.md). Claude recibió instrucciones de corregir y añadir regresiones; la aprobación de CI previa no acredita esas correcciones.

Las demás tareas de Jorge esperan sus dependencias reales del índice. No se implementan tareas de compañeros para simular avance. Los cambios de estado se actualizan con revisión/PR/evidencia, no solo con una declaración del agente.
