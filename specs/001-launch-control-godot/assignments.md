# Reparto activo — Launch Control

**Relevo 2026-11-15 ([ADR-0005](../../docs/decisions/0005-relevo-adrian-sojo.md)):** por decisión de Jorge, **Sojo asume las ocho tareas de Adrian** (T007, T008, T009, T011, T013, T017, T030 y T035) y su apoyo técnico en T039. Adrian queda inactivo, sin asignaciones vigentes, y conserva la autoría de lo que implementó. Siguen los mismos 42 IDs y dependencias: **Jorge 9, Gael 9, Sojo 8, Kevin 8 e Isra 8**. (Antes, el 2026-11-14, Sojo no estaba incorporado y sus tareas se habían repartido; ese reparto queda como historia.) Las antiguas tareas de validación de Sojo se redistribuyen, sin eliminar la verificación ni inventar experiencia previa. Las cantidades no equivalen a estimaciones de horas.

| Integrante | Responsabilidad | Tareas | Primer paso disponible |
| --- | --- | --- | --- |
| Jorge | Base, composición e integración; validación inicial y aceptación final | T001, T002, T003, T012, T018, T024, T031, T038, T040 | T024 en revisión (#37), con T020–T023 integradas (T001/T002 con seguimiento; T003, T012 y T018 integradas) |
| Gael | Escenas 3D, animaciones y verificación visual/desenlaces | T004, T015, T020, T021, T025, T033, T034, T037, T039 | T025 después de T024 (T020/T021 y rediseño #32 integrados) |
| Sojo | Red, roles, estado y reloj; verificación del contrato (relevo de Adrian) | T007, T008, T009, T011, T013, T017, T030, T035 | **T030** (T013 y T026 integradas). T007–T009, T011, T013 y T017 las implementó Adrian y están integradas: Sojo las mantiene. Guía: `docs/setup/sojo.md` |
| Kevin | Módulos y reglas; verificación de la antena | T005, T010, T014, T019, T026, T027, T036, T041 | Aceptar T019; T026/T027/T036 ya integradas; T041 espera T034 |
| Isra | Manual, interfaz y calculadora; verificación de dificultad | T006, T016, T022, T023, T028, T029, T032, T042 | T032 después de T031 (T022/T023 y T028/T029 integradas) |

La copia de tasks.md define rutas, dependencias y aceptación. La base técnica se verifica y publica en AESRJ/LaunchControlGodot; su guía docs/setup/team-readiness.md indica cuándo se liberan estas tareas. Sojo usa Sojito312 y tiene escritura comprobada en ambos repositorios. T030 está técnicamente liberada sobre T013/T026, manteniendo la aceptación de T019 pendiente de Kevin; ver [inicio T030](../../docs/setup/t030-inicio-sojo.md). La prueba personal de Windows y las pruebas de juego no se declaran realizadas por haber pasado CI.

## Dependencias de Jorge

T012 y T018 están integradas (#21, #22). T024 requiere T020/T021/T022/T023; T031 requiere T024/T027/T028/T029/T030; T038 requiere T025/T032/T037. Jorge termina lo que esté liberado y retoma esas integraciones conforme lleguen las entregas. No implementar trabajo ajeno para afirmar que terminó sus tareas.

## Forma de trabajo

Cada persona empieza con «Soy <nombre>», lee su tarea, spec.md y contracts/, trabaja una tarea liberada a la vez en su rama y modifica solo sus archivos. Claude implementa las tareas de Jorge que este le delega; Codex coordina y revisa, y lleva la memoria compartida. Jorge asumió temporalmente solo la adaptación de siete pruebas de Adrian (autorizada); Adrian conserva su autoría histórica; Sojo mantiene esos componentes y las tareas transferidas. Las pruebas reasignadas las ejecuta el dueño de cada ID y otro integrante puede contrastar su evidencia sin editar el mismo archivo.

> Soy Kevin. Lee assignments.md, tasks.md y task-index.json de specs/001-launch-control-godot. Muéstrame mis tareas activas y cuál puedo empezar según las dependencias y la guía de preparación del juego. Usa Spec Kit y conserva el reparto vigente.

Repositorios: agentes https://github.com/AESRJ/Agentes_Space_Ship; juego privado https://github.com/AESRJ/LaunchControlGodot. Cuentas confirmadas en el registro: Jorge AESRJ, Gael GaelFlores04, Kevin KVSO755 e Isra issgg; Sojo Sojito312; Adrian adrianbalderas373488 (inactivo, historial). Acceso de escritura comprobado por API. No afirmar que una persona ya clonó o probó su equipo sin evidencia.

La primera versión del reparto entre seis personas permanece en Git como historia; no se vuelve a utilizar para asignar tareas actuales.
