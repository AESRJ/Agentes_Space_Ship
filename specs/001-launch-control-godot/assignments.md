# Reparto activo — Launch Control

Actualizado por instrucción de Jorge el 2026-11-14: **Sojo no está incorporado por ahora**. Se conserva su historial, pero no tiene tareas activas ni bloquea el arranque. Siguen los mismos 42 IDs y dependencias: **Jorge 9, Gael 9, Adrian 8, Kevin 8 e Isra 8**. Las antiguas tareas de validación de Sojo se redistribuyen, sin eliminar la verificación ni inventar experiencia previa. Las cantidades no equivalen a estimaciones de horas.

| Integrante | Responsabilidad | Tareas | Primer paso disponible |
| --- | --- | --- | --- |
| Jorge | Base, composición e integración; validación inicial y aceptación final | T001, T002, T003, T012, T018, T024, T031, T038, T040 | T024 cuando lleguen T020–T023 (T001/T002 con seguimiento; T003, T012 y T018 integradas) |
| Gael | Escenas 3D, animaciones y verificación visual/desenlaces | T004, T015, T020, T021, T025, T033, T034, T037, T039 | T020 tras aceptar T019 (T004 y T015 integradas) |
| Adrian | Red, roles, estado y reloj; verificación del contrato | T007, T008, T009, T011, T013, T017, T030, T035 | T030 tras T026 (T007–T009, T011, T013 y T017 integradas) |
| Kevin | Módulos y reglas; verificación de la antena | T005, T010, T014, T019, T026, T027, T036, T041 | **T019 ahora** (T005, T010 y T014 integradas); después T026 |
| Isra | Manual, interfaz y calculadora; verificación de dificultad | T006, T016, T022, T023, T028, T029, T032, T042 | T022 tras T019 (T006 y T016 integradas) |

La copia de tasks.md define rutas, dependencias y aceptación. La base técnica se verifica y publica en AESRJ/LaunchControlGodot; su guía docs/setup/team-readiness.md indica cuándo se liberan estas tareas. No esperar una cuenta de Sojo. La prueba personal de Windows y las pruebas de juego no se declaran realizadas por haber pasado CI.

## Dependencias de Jorge

T012 y T018 están integradas (#21, #22). T024 requiere T020/T021/T022/T023; T031 requiere T024/T027/T028/T029/T030; T038 requiere T025/T032/T037. Jorge termina lo que esté liberado y retoma esas integraciones conforme lleguen las entregas. No implementar trabajo ajeno para afirmar que terminó sus tareas.

## Forma de trabajo

Cada persona empieza con «Soy <nombre>», lee su tarea, spec.md y contracts/, trabaja una tarea liberada a la vez en su rama y modifica solo sus archivos. Claude implementa las tareas de Jorge que este le delega; Codex coordina y revisa, y lleva la memoria compartida. Jorge asumió temporalmente solo la adaptación de siete pruebas de Adrian (autorizada); Adrian conserva sus componentes y tareas. Las pruebas reasignadas las ejecuta el dueño de cada ID y otro integrante puede contrastar su evidencia sin editar el mismo archivo.

> Soy Kevin. Lee assignments.md, tasks.md y task-index.json de specs/001-launch-control-godot. Muéstrame mis tareas activas y cuál puedo empezar según las dependencias y la guía de preparación del juego. Usa Spec Kit y conserva el reparto vigente.

Repositorios: agentes https://github.com/AESRJ/Agentes_Space_Ship; juego privado https://github.com/AESRJ/LaunchControlGodot. Cuentas confirmadas en el registro: Jorge AESRJ, Gael GaelFlores04, Adrian adrianbalderas373488, Kevin KVSO755 e Isra issgg. Acceso de escritura comprobado por API. No afirmar que una persona ya clonó o probó su equipo sin evidencia.

La primera versión del reparto entre seis personas permanece en Git como historia; no se vuelve a utilizar para asignar tareas actuales.
