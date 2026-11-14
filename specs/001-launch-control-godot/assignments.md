# Reparto activo — Launch Control

Actualizado por instrucción de Jorge el 2026-11-14: **Sojo no está incorporado por ahora**. Se conserva su historial, pero no tiene tareas activas ni bloquea el arranque. Siguen los mismos 42 IDs y dependencias: **Jorge 9, Gael 9, Adrian 8, Kevin 8 e Isra 8**. Las antiguas tareas de validación de Sojo se redistribuyen, sin eliminar la verificación ni inventar experiencia previa. Las cantidades no equivalen a estimaciones de horas.

| Integrante | Responsabilidad | Tareas | Primer paso disponible |
| --- | --- | --- | --- |
| Jorge | Base, composición e integración; validación inicial y aceptación final | T001, T002, T003, T012, T018, T024, T031, T038, T040 | T003 después de liberar técnicamente T001/T002 |
| Gael | Escenas 3D, animaciones y verificación visual/desenlaces | T004, T015, T020, T021, T025, T033, T034, T037, T039 | T004 después de la base |
| Adrian | Red, roles, estado y reloj; verificación del contrato | T007, T008, T009, T011, T013, T017, T030, T035 | T007 después de la base |
| Kevin | Módulos y reglas; verificación de la antena | T005, T010, T014, T019, T026, T027, T036, T041 | T005 después de la base |
| Isra | Manual, interfaz y calculadora; verificación de dificultad | T006, T016, T022, T023, T028, T029, T032, T042 | T006 después de la base |

La copia de tasks.md define rutas, dependencias y aceptación. La base técnica se verifica y publica en AESRJ/LaunchControlGodot; su guía docs/setup/team-readiness.md indica cuándo se liberan estas tareas. No esperar una cuenta de Sojo. La prueba personal de Windows y las pruebas de juego no se declaran realizadas por haber pasado CI.

## Dependencias de Jorge

T012 requiere T007/T008/T009/T010; T018 requiere T012/T015/T016/T017; T024 requiere T020/T021/T022/T023; T031 requiere T024/T027/T028/T029/T030; T038 requiere T025/T032/T037. Jorge termina lo que esté liberado y retoma esas integraciones conforme lleguen las entregas. No implementar trabajo ajeno para afirmar que terminó sus tareas.

## Forma de trabajo

Cada persona empieza con «Soy <nombre>», lee su tarea, spec.md y contracts/, trabaja una tarea liberada a la vez en su rama y modifica solo sus archivos. Claude está completando la base de Jorge; Codex coordina el repositorio de agentes y la memoria. Las pruebas reasignadas las ejecuta el dueño de cada ID y otro integrante puede contrastar su evidencia sin editar el mismo archivo.

> Soy Kevin. Lee assignments.md, tasks.md y task-index.json de specs/001-launch-control-godot. Muéstrame mis tareas activas y cuál puedo empezar según las dependencias y la guía de preparación del juego. Usa Spec Kit y conserva el reparto vigente.

Repositorios: agentes https://github.com/AESRJ/Agentes_Space_Ship; juego privado https://github.com/AESRJ/LaunchControlGodot. Cuentas confirmadas en el registro: Jorge AESRJ, Gael GaelFlores04, Adrian adrianbalderas373488, Kevin KVSO755 e Isra issgg. Acceso de escritura comprobado por API. No afirmar que una persona ya clonó o probó su equipo sin evidencia.

La primera versión del reparto entre seis personas permanece en Git como historia; no se vuelve a utilizar para asignar tareas actuales.
