# Launch Control — plan vigente y reparto en Godot

Actualizado: 2026-11-14. Encargo: Jorge. Estado: planificación del prototipo, sin implementación del videojuego. Publicado e integrado en main mediante [PR #6](https://github.com/AESRJ/Agentes_Space_Ship/pull/6); CI Linux/Windows y atribución aprobados.

El plan vigente está en [specs/001-launch-control-godot](../specs/001-launch-control-godot/spec.md), generado con Specify → Plan → Tasks. Sustituye Unity para este prototipo y excluye la metodología de `Etapa_1_final.md`. La decisión y sus límites constan en [ADR-0003](decisions/0003-launch-control-godot-speckit.md).

| Integrante | Área inicial | Tareas |
| --- | --- | --- |
| Jorge | Repositorio, base y composición/integración | T001, T002, T012, T018, T024, T031, T038 |
| Gael | Cabina/torre 3D, antena visual y desenlaces; prueba externa acompañada | T004, T015, T020, T021, T033, T034, T039 |
| Adrian | Red, roles, reloj, estado y validación autoritativa | T007, T008, T009, T013, T017, T030, T035 |
| Kevin | Reglas y recursos de módulos, código numérico y reinicio | T005, T010, T014, T026, T027, T036, T041 |
| Isra | Manual, laptop, HUD, calculadora y guía de demo | T006, T016, T022, T023, T028, T029, T042 |
| Sojo | Harness, validación de cortes y evidencia final | T003, T011, T019, T025, T032, T037, T040 |

Son siete tareas por persona, no una estimación de horas. El [reparto completo](../specs/001-launch-control-godot/assignments.md) indica cómo iniciar y trabajar con IA; [tasks.md](../specs/001-launch-control-godot/tasks.md) es la única lista ejecutable con dependencias, rutas y aceptación. `GAME/` representa el repositorio futuro del juego, no un proyecto existente aquí. No se crean tickets ni se contacta a integrantes.

Primer corte: elegir roles, dos puestos provisionales, antena, manual, tiempo y resultado compartido (hasta T019). Prototipo completo: puestos 3D, manual/herramienta, dos dificultades, presentaciones y comprobación externa (hasta T042). La segunda dificultad propone un módulo numérico original para que haya más componentes; no se implementa todo el catálogo de las capturas.

Las propuestas iniciales son Godot 4.7.2/GDScript, host ENet autoritativo, voz externa y 180 segundos. La decisión de Godot y el uso de Spec Kit sí fueron explícitos; los detalles son diseño a validar. Dos procesos locales no demuestran Internet. Las pruebas de juego, resultados de usuarios, FPS y builds siguen pendientes. La constitución de producto no está ratificada.

La memoria debe conservar el resumen de esta decisión y una instantánea del paquete Spec Kit, distinguiendo contenido local de una revisión integrada. El exportador histórico de `docs/` no incluye automáticamente `specs/`; el traspaso al juego debe copiar ese paquete expresamente.
