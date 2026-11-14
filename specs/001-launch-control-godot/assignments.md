# Reparto inicial del equipo — Launch Control

Solicitado por Jorge: reparto equilibrado sin suponer experiencia previa. Son **42 tareas: siete por persona**. Las áreas evitan conflictos de archivos; el número de tareas no supone igualdad de horas ni fechas comprometidas. Todas siguen pendientes. El detalle ejecutable y los criterios de terminado están en [tasks.md](tasks.md).

| Integrante | Responsabilidad principal | Siete tareas | Primera tarea liberable |
| --- | --- | --- | --- |
| Jorge | Base del proyecto, composición e integración | T001, T002, T012, T018, T024, T031, T038 | T001: identificar el repositorio del juego; después T002 crea la base |
| Gael | Cabina/torre 3D, antena visual, desenlaces y prueba externa acompañada | T004, T015, T020, T021, T033, T034, T039 | T004: guía visual propia, tras T002 |
| Adrian | Red, roles, estado, reloj y validación autoritativa | T007, T008, T009, T013, T017, T030, T035 | T007: host/cliente, tras T002 |
| Kevin | Definición de módulos, reglas de antena/código y reinicio | T005, T010, T014, T026, T027, T036, T041 | T005: recurso de módulo, tras T002 |
| Isra | Manual, foco de laptop, HUD, calculadora y guía de demo | T006, T016, T022, T023, T028, T029, T042 | T006: contenido del manual, tras T002 |
| Sojo | Harness, verificación de cada corte y evidencia final | T003, T011, T019, T025, T032, T037, T040 | T003: escena de validación aislada, tras T002 |

Cada dueño comprueba su propio trabajo; Sojo verifica integración y evidencia, no corrige por defecto los archivos de todos. Gael ejecuta T039 con apoyo técnico de Adrian, pero solo Adrian modifica su implementación de red. Jorge integra escenas por instancias y señales, sin editar su interior. Las revisiones breves pueden hacerse por parejas sin añadir una aprobación obligatoria de PR.

## Qué entregar primero

1. Jorge registra el destino GAME y configura la base común; mientras, el resto puede leer reglas, preparar notas y revisar sus interfaces sin crear escenas en este repositorio.
2. Después de T002 trabajan en paralelo Gael T004, Adrian T007, Kevin T005, Isra T006 y Sojo T003. Jorge espera contratos listos para T012.
3. Primer hito jugable: dos puestos provisionales, antena, manual, cuenta regresiva y éxito/fallo compartido (T019). No comenzar cinco acertijos ni pulir el paracaídas antes de este corte.
4. Segundo hito: puestos 3D finales, normal con dos componentes, herramienta, desenlaces y prueba en redes externas (T040). El resultado de T039 decide si la conexión remota está demostrada.

## Cómo trabajar con IA y Spec Kit

Cada conversación comienza con «Soy <nombre>». Leer la tarea concreta, spec.md y los dos contratos. Usar `$speckit-tasks` para consultar/refinar el desglose y `$speckit-implement` limitado al ID asignado cuando el destino y las dependencias existan. No regenerar una lista alternativa por persona ni ejecutar las 42 tareas de una sola vez. Usar una rama `<id>/tNNN-descripcion` y un escritor por archivo.

Mensaje de inicio reutilizable:

> Soy <nombre>. Trabajo en TNNN de specs/001-launch-control-godot/tasks.md. Lee spec.md, plan.md y contracts/. Comprueba primero sus dependencias y el repositorio GAME. Aplica Spec Kit solo a mi tarea y mis archivos. Entrega el cambio, cómo probar su criterio, evidencia real y checkpoint con mi nombre; conserva las interfaces del equipo.

Al terminar, crear commit `[id] ...` con `Team-Member` y `AI-Assisted`; guardar resultado y revisión en memoria. Los repositorios de agentes y del juego siguen separados. Para llevar este paquete al juego, copiar explícitamente `specs/001-launch-control-godot/`; el exportador histórico de contexto solo recoge docs/ y no incluye automáticamente specs/.

## Cuentas y accesos

Los nombres bastan para este reparto local. Jorge → AESRJ y Kevin → KVSO755 están integrados en el registro Git consultado. No se infiere una cuenta a partir del nombre ni se crean asignaciones GitHub a cuentas no verificadas. Una mención de cuenta en NotebookLM no reemplaza su registro canónico. Esta entrega no envía mensajes a integrantes, no crea issues y no cambia permisos.
