# ADR-0004 — Cinco integrantes activos y liberación técnica de la base

Fecha: 2026-11-14. Instrucción de Jorge en esta conversación.

## Decisión

Jorge pide terminar sus tareas con Claude para que los demás empiecen. Al preguntar por la cuenta de Sojo, aclara: «De momento ignora este participante, no esta incorporado de momento en el equipo».

Se mantiene el registro histórico de Sojo con estado `pending`, sin tareas activas, sin pedir su cuenta ni bloquear al resto. Los activos son Jorge, Gael, Adrian, Kevin e Isra. Se conserva el desglose de 42 IDs, pero se reparten las siete tareas de verificación antes asignadas a Sojo:

| Tarea | Responsable actual |
| --- | --- |
| T003 | Jorge |
| T011 | Adrian |
| T019 | Kevin |
| T025 | Gael |
| T032 | Isra |
| T037 | Gael |
| T040 | Jorge |

Totales: Jorge 9, Gael 9, Adrian 8, Kevin 8 e Isra 8. No son estimaciones de horas. El historial del reparto inicial entre seis permanece intacto en los registros anteriores.

## Destino y accesos verificados

El repositorio privado del juego es `https://github.com/AESRJ/LaunchControlGodot`, autorizado por Jorge en su conversación con Claude y registrado en `docs/setup/repository.md` del juego. La API confirma escritura efectiva para `GaelFlores04`, `adrianbalderas373488`, `KVSO755` e `issgg`, además del propietario `AESRJ`; la lista de invitaciones pendientes está vacía. La confirmación de `issgg` como Isra consta en el commit `cc204c1` del juego; no se conserva como suposición el texto anterior desactualizado.

## Liberación de trabajo

La base técnica publicada en main, con versión fijada y comprobación Linux/Windows, permite iniciar las tareas de arranque de quienes tienen acceso. Se distingue ese estado de seguimientos personales de instalación/GUI. No se declara hecha una prueba que no ocurrió, pero tampoco se bloquea a todo el equipo por la incorporación futura de alguien o por una máquina personal.

Claude completa el PR de la base y la copia del reparto en el juego. Codex coordina el repositorio de agentes, los registros, las cuentas y NotebookLM. No editan los mismos archivos. Al quedar publicada la base: Jorge T003, Gael T004, Adrian T007, Kevin T005 e Isra T006. Las integraciones posteriores de Jorge siguen dependiendo de entregas reales de sus compañeros.

Este cambio no aprueba gameplay inexistente, no elimina la verificación y no permite marcar automáticamente T001/T002 como completadas sin sus evidencias. La guía del juego debe reflejar estado técnico y seguimientos por separado.
