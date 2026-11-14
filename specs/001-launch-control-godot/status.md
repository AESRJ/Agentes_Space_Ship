# Estado operativo — Launch Control

Actualizado: 2026-11-14. No sustituye criterios de aceptación ni declara terminado el juego.

## Auditoría de ramas y flujo (2026-11-14)

Jorge encargó revisar todas las ramas y fusionar solo lo conforme y probado. Informe completo: [auditoría](../../docs/reviews/2026-11-14-auditoria-ramas-y-flujo.md). El juego queda en main **`10241ca2e0f23d64fd092b02e236eb14083e4498`**, con CI Linux/Windows en verde en cada fusión.

| Tarea | PR | main | Evidencia principal (ejecutada por el auditor, Linux) |
| --- | --- | --- | --- |
| T007 Adrian | #9 | `793349d` | loopback de 3 procesos: emisor del transporte, rol exclusivo, sesión llena |
| T008 Adrian | #10 | `2122152` | round_controller_test |
| T009 Adrian | #11 | `0725d02` | server_clock_test; mutante del cero exacto detectado |
| T013 Adrian | #12 | `c700753` | lobby_loopback de 2 procesos |
| T011 Adrian | #13 | `bfebc54` | session_contract_runner 17/17 (24/24 tras T017) |
| T017 Adrian | #15 | `36f8386` | attempt_loopback; flujo multiproceso: host astronauta, timeout, caídas |
| T004 Gael | #3 | `824784a` | criterio de documento verificado |
| T015 Gael | #4 | `890c192` | antenna_view_check; captura 1280×720; vista real conectada a la regla |
| T006 Isra | #8 | `d7ac177` | coherencia con regla y contrato |
| T016 Isra | #14 | `10241ca` | página estática; captura 1280×720 |

T005/T010/T014 (Kevin) ya estaban integradas; sus pruebas pasan en cada paso. T020/T021 (Gael) son borradores y esperan T019. **Siguiente tarea liberada: T012 (Jorge)**, con T007–T010 integradas. T018 → T019 y el resto del corte dependen de ella.

**No probado:** LAN e Internet (solo loopback), pruebas de red y módulos en Windows (el CI solo ejecuta `check.ps1`), dos equipos o SC-006, ronda completa jugable (falta composición T012/T018), HUD, desenlaces y revancha.

## Base que libera el arranque

T001/T002: **base técnica publicada** en https://github.com/AESRJ/LaunchControlGodot, main `0ec8b6ac0fffa864f7549dd95f871efa96a12d58`, PR #1. CI Linux/Windows aprobado y comprobación Linux independiente OK. Los cinco activos tienen escritura. La prueba GUI del Windows personal de Jorge sigue como seguimiento; Sojo no está incorporado. Ninguno de esos seguimientos bloquea a los activos con base accesible.

Esta liberación técnica satisface el requisito previo de arranque de T003/T004/T005/T006/T007 aunque las casillas originales T001/T002 conserven seguimiento de aceptación final.

| Persona | Siguiente tarea | Estado real |
| --- | --- | --- |
| Jorge | T003: harness | PR #2 fusionado por solicitud explícita de Jorge; commit 3cf3de7, CI Linux/Windows aprobado para cabecera 11bab3a; no acredita puestos reales |
| Gael | T004: guía visual | fusionada (#3, `824784a`) tras auditoría |
| Adrian | T007: transporte | fusionada (#9, `793349d`) tras auditoría |
| Kevin | T005: definición de módulo | fusionada por Kevin (#5, `5cb6fd6`); pruebas OK en la auditoría |
| Isra | T006: contenido de manual | fusionada (#8, `d7ac177`) tras auditoría |

## Cierre de integración de T003

PR #2 fusionado con squash el 2026-11-14T23:19:38Z en `3cf3de79f9dd360013a4ed8fa41a27a81e6b7482`, con autorización explícita de Jorge y CI Linux/Windows 43652062713 aprobado para cabecera `11bab3a`. El historial siguiente corresponde a la revisión anterior, no a un bloqueo de fusión actual.

## Revisión anterior de T003 — historial

Cabecera revisada: `105a1e7d37aa0dc8dd0184ee57c3fc5d1c30113b`, PR #2 abierto. CI de esa revisión en verde, pero casos independientes detectan éxito falso cuando no se escribe registro, argumento frames inválido que no termina y resolución headless falsamente validada. Ver [revisión](../../docs/reviews/2026-11-14-claude-base-y-harness.md). Claude recibió instrucciones de corregir y añadir regresiones; la aprobación de CI previa no acredita esas correcciones.

Las demás tareas de Jorge esperan sus dependencias reales del índice. No se implementan tareas de compañeros para simular avance. Los cambios de estado se actualizan con revisión/PR/evidencia, no solo con una declaración del agente.
