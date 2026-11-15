# Estado operativo — Launch Control

Actualizado: 2026-11-14 (tras #22). No sustituye criterios de aceptación ni declara terminado el juego.

## Estado vigente — relevo de Adrian por Sojo (2026-11-15)

**Decisión de Jorge ([ADR-0005](../../docs/decisions/0005-relevo-adrian-sojo.md)):** Sojo asume T007, T008, T009, T011, T013, T017, T030 y T035, más el apoyo técnico en T039 (dueño: Gael). Adrian queda inactivo y conserva la autoría de lo que implementó. Reparto: Jorge 9, Gael 9, Sojo 8, Kevin 8 e Isra 8. La cuenta GitHub de Sojo está **pendiente**: sin invitación ni acceso declarado. Guía: [docs/setup/sojo.md](../../docs/setup/sojo.md).

Juego: main `11d649b396ef6ec8c9f41bc54b24f40cb52d49d0`, CI 43743111583 (integración 43/43 y harness 21/21 en Linux y Windows). Entregas integradas desde el estado anterior:

| Entrega | PR | Commit | Nota |
| --- | --- | --- | --- |
| T020 cabina (Gael) | #16 | `adae9b3` | el rediseño de T020/T021 está en el #32 (abierto) |
| T021 oficina (Gael) | #17 | `46e07e4` | — |
| T019 evidencia de QA (Kevin) | #24 | `d02f979` | **no aceptada**: queda una incidencia del runner GUI y repetir Q05 |
| Issue #23: interrupción visible (Jorge) | #25 | `36a0efc` | relacionado con Q05; el issue sigue abierto |
| T026 regla de código (Kevin) | #26 | `71f3fc2` | — |
| T027 placa de código (Kevin) | #27 | `c2b8b88` | — |
| T036 reinicio de módulos (Kevin) | #28 | `b548759` | no implica revancha (T035) |
| README de escenas (Gael) | #31 | `961d642` | — |
| T022/T023 manual y HUD (Isra) | #34 | `11d649b` | — |

Abiertos (no se fusionan por este relevo): #32 (rediseño de T020/T021), #33 (T028/T029 de Isra), borradores #29/#30 (T033/T034). PR #8 de agentes, fuera de alcance.

| Persona | Siguiente | Dependencia real |
| --- | --- | --- |
| **Sojo** | **T030**: fácil = [antenna], normal = [antenna, code]; sin cambios durante la ronda; normal no gana con un solo módulo | T013 y T026 integradas. Base actual: `RULE_SCRIPTS` solo `antenna` y `difficulty_modules` solo `easy` |
| Sojo | T035: revancha y ronda limpia | T017 y **T030** |
| Kevin | T019: aceptar Q01–Q05 (incidencia del runner GUI, repetir Q05) | — |
| Isra | T028/T029 en revisión (#33) | T022 y T026 integradas |
| Jorge | T024 integración de puestos | T020–T023 integradas; los puestos finales dependen del #32 |
| Gael | #32 y, después, T025 | T024 |

Las seis tareas que implementó Adrian se mantienen, no se reimplementan. La disponibilidad por dependencias no equivale a aceptar T019.

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
