# Launch Control — plan vigente y arranque del equipo

Actualizado: 2026-11-14. Jorge solicita terminar la base con Claude para liberar el trabajo. Desde el 2026-11-15, Sojo releva a Adrian ([ADR-0005](decisions/0005-relevo-adrian-sojo.md)); los repartos anteriores quedan como historia. [ADR-0004](decisions/0004-cinco-activos-y-arranque.md) registra la instrucción.

Juego privado: https://github.com/AESRJ/LaunchControlGodot. La base tiene PR #1 y validación Linux/Windows; su guía docs/setup/team-readiness.md es la referencia de publicación y arranque. El repositorio de agentes conserva decisiones y memoria; el código se escribe en el juego.

| Integrante activo | Área | Tareas |
| --- | --- | --- |
| Jorge | Base, composición e integración; validación inicial y aceptación | T001, T002, T003, T012, T018, T024, T031, T038, T040 |
| Gael | Escenarios 3D, animaciones y verificación visual | T004, T015, T020, T021, T025, T033, T034, T037, T039 |
| Sojo (relevo de Adrian, autor de T007–T017) | Red, roles, reloj, estado y verificación del contrato | T007, T008, T009, T011, T013, T017, T030, T035 |
| Kevin | Reglas/módulos y verificación de antena | T005, T010, T014, T019, T026, T027, T036, T041 |
| Isra | Manual, interfaz, calculadora y verificación de dificultad | T006, T016, T022, T023, T028, T029, T032, T042 |

Se mantienen los 42 IDs: 9/9/8/8/8 tareas, sin afirmar igualdad de horas ni experiencia. [Reparto](../specs/001-launch-control-godot/assignments.md) y [tareas](../specs/001-launch-control-godot/tasks.md) contienen el detalle. Al liberar técnicamente la base arrancaron Jorge T003, Gael T004, Adrian T007 (hoy Sojo), Kevin T005 e Isra T006 (histórico). La verificación personal del PC Windows es un seguimiento, no una prueba ya realizada ni un bloqueo general.

El primer corte sigue siendo antena, manual, reloj y resultado compartido; la ampliación propone módulo numérico y herramienta. Las capturas son referencias y no assets del ejecutable. Godot es la elección vigente; valores como 180 segundos son propuestas. No se ha probado el gameplay ni Internet entre dos PCs.

Las tareas posteriores de integración de Jorge requieren los componentes de otros dueños: no se implementan esas partes ajenas para marcar todo como terminado. La memoria conserva evidencia de base técnica, publicación y pendientes reales por separado.
