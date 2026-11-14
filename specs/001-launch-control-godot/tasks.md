# Tasks: Launch Control en Godot

**Estado**: 42 tareas propuestas, ninguna implementada o completada en esta planificación. **Reparto**: siete por persona, solicitado por Jorge; no se asumen conocimientos previos ni se promete igualdad de horas. **Fuentes**: [spec.md](spec.md), [plan.md](plan.md), [modelo](data-model.md), [contratos](contracts/session.md) y [validación](quickstart.md).

`GAME/` significa raíz del futuro repositorio del juego: no existe como carpeta implementada aquí. Cada ruta es el entregable previsto, no evidencia de archivos ya creados. Una tarea puede incluir su script compañero dentro de la misma carpeta; no habilita editar recursos de otro dueño. [P] significa que puede ejecutarse junto con otra persona una vez cumplidas sus dependencias; nunca obliga a la misma persona a abrir dos tareas a la vez. Las pruebas de aceptación son escenarios necesarios para demostrar la entrega, sin imponer TDD o una batería duplicada de la implementación.

## Fase 1 — Preparación

Repositorio, herramienta común y contratos de contenido. Tras T002, T003–T006 se liberan en paralelo.

- [ ] T001 Jorge — Identificar o crear el destino autorizado del juego y registrar URL, rama base y acceso de los seis; no iniciar el juego dentro del repositorio de agentes en `GAME/docs/setup/repository.md`. Depende: ninguna. Terminado: el equipo puede clonar el destino y reconoce GAME como su raíz. Cubre: FR-019.
- [ ] T002 Jorge — Crear base Godot 4.7.2 propuesta, fijar versión y renderer conservador, acción de interacción y estructura de carpetas en `GAME/project.godot`. Depende: T001. Terminado: proyecto vacío abre en dos equipos con la misma versión. Cubre: FR-008 FR-009.
- [ ] T003 [P] Sojo — Preparar escena/harness de validación con datos de prueba y forma de registrar captura y versión en `GAME/harness/scene_smoke.tscn`. Depende: T002. Terminado: se puede abrir un puesto aislado sin necesitar una partida real. Cubre: FR-018 SC-006.
- [ ] T004 [P] Gael — Definir guía de cabina, torre, paneles distinguibles y referencias propias basadas en las tres imágenes en `GAME/docs/art/visual-guide.md`. Depende: T002. Terminado: lista de recursos originales y bocetos de ambos puestos, sin copiar screenshots como assets. Cubre: FR-008 FR-009 FR-018 FR-019.
- [ ] T005 [P] Kevin — Definir recurso ModuleDefinition: id único, manual_section_id y rule_version=1; separar pista de regla/solución en `GAME/resources/modules/module_definition.gd`. Depende: T002. Terminado: antena y código pueden declararse sin depender de sus escenas. Cubre: FR-003 FR-004 FR-019.
- [ ] T006 [P] Isra — Definir índice y formato de páginas: identificación, qué preguntar, regla, instrucción y herramienta; conservar regla exacta de antena en `GAME/docs/manual/content-outline.md`. Depende: T002. Terminado: antena tiene las dos filas y código tiene tabla propia, sin huecos de solución. Cubre: FR-005 FR-010 FR-011.

## Fase 2 — Base compartida

Antes de integrar historias, fijar transporte, estado, reloj y frontera de módulos. No requiere arte final.

- [ ] T007 [P] Adrian — Implementar transporte host/cliente y enlace de emisor; mantener mismo NodePath en ambos puestos en `GAME/autoload/session_service.gd`. Depende: T002. Terminado: dos procesos intercambian estado y se informa conexión/desconexión, sin declarar éxito de Internet. Cubre: FR-001 FR-015 FR-020.
- [ ] T008 Adrian — Implementar estado lobby/playing/finished/interrupted, round_id nuevo y revision creciente; resultado inmutable en `GAME/autoload/round_controller.gd`. Depende: T007. Terminado: no hay dos resultados ni transición desde terminal a jugando por mensaje tardío. Cubre: FR-004 FR-007 FR-015 FR-016.
- [ ] T009 Adrian — Implementar deadline monotónico y estimación visual; timeout prevalece cuando now >= deadline y cliente no decide resultado en `GAME/autoload/server_clock.gd`. Depende: T008. Terminado: cambiar reloj del sistema no cambia la ronda; estado de ambos relojes medible. Cubre: FR-002 FR-007 SC-002.
- [ ] T010 [P] Kevin — Implementar interfaz de instancia: pending/solved, bind/reset y evaluación de reglas sin decidir victoria; active debe ser booleano en `GAME/scripts/modules/module_runtime.gd`. Depende: T005. Terminado: regla y vista pueden sustituirse sin modificar SessionService. Cubre: FR-004 FR-006 FR-017.
- [ ] T011 [P] Sojo — Preparar casos ejecutables de rol, revisión, vencimiento e interrupción usando el contrato v1 en `GAME/harness/session_contract_runner.gd`. Depende: T007, T008, T009. Terminado: harness permite reproducir los límites sin introducir un segundo controlador de ronda. Cubre: FR-001 FR-007 FR-015 FR-017.
- [ ] T012 Jorge — Componer autoloads, escenas instanciadas y señales públicas; no editar nodos internos de escenas ajenas en `GAME/scenes/main.tscn`. Depende: T007, T008, T009, T010. Terminado: main selecciona la vista del rol y recibe eventos del contrato sin duplicar autoridad. Cubre: FR-003 FR-007.

## Fase 3 — US1: primer corte con antena

Validación independiente: Q01–Q05 con dos procesos/equipos. Este es el primer corte jugable completo.

- [ ] T013 [P] [US1] Adrian — Crear lobby host/join, elección exclusiva de rol, dificultad y readiness en `GAME/scenes/lobby/lobby.tscn`. Depende: T007, T008. Terminado: empieza solo con dos roles distintos listos y se rechaza rol ocupado. Cubre: FR-001 FR-013.
- [ ] T014 [P] [US1] Kevin — Implementar fixed→moon y blinking→star; incorrecta conserva pending y permite reintento sin penalización extra en `GAME/scripts/modules/antenna_rule.gd`. Depende: T010. Terminado: los cuatro casos de antena producen el resultado especificado. Cubre: FR-005 FR-006 SC-001.
- [ ] T015 [P] [US1] Gael — Construir luz fija/parpadeante, selector luna/estrella, Confirmar y señal Listo con forma/texto en `GAME/scenes/modules/antenna_view.tscn`. Depende: T004, T010. Terminado: la vista emite intento y no modifica directamente estado o resultado. Cubre: FR-003 FR-005 FR-018.
- [ ] T016 [P] [US1] Isra — Crear página de antena con preguntas y las dos reglas, sin exponer pistas vivas de cabina en `GAME/ui/manual/antenna_page.tscn`. Depende: T006. Terminado: torre resuelve ambas variantes consultando la página y no puede operar controles. Cubre: FR-003 FR-005 FR-010.
- [ ] T017 [US1] Adrian — Conectar submit_attempt con verificación de emisor/rol, round_id, command_id, activo y tiempo; host local pasa la misma validación en `GAME/autoload/session_service.gd`. Depende: T009, T013, T014. Terminado: torre, duplicados y mensajes tardíos no alteran indebidamente la ronda. Cubre: FR-004 FR-006 FR-007 FR-017.
- [ ] T018 [US1] Jorge — Integrar corte vertical con vistas provisionales, reloj, antena, manual y resultado textual en `GAME/scenes/main.tscn`. Depende: T012, T015, T016, T017. Terminado: dos procesos completan una ronda y la autoridad funciona alojando cualquiera de los roles. Cubre: FR-001 FR-002 FR-003 FR-007.
- [ ] T019 [US1] Sojo — Ejecutar Q01–Q05: dos luces, error/reintento, vencimiento, rol duplicado, intento inválido y desconexión; alternar rol host en `GAME/docs/qa/antenna-round.md`. Depende: T011, T018. Terminado: evidencia indica versión, caso y resultado real en ambos puestos; primer corte aceptable solo si todos pasan. Cubre: FR-001 FR-005 FR-006 FR-007 FR-015 FR-017 SC-001.

## Fase 4 — US2: puestos y manual

Validación independiente: Q06–Q07; escenas pueden desarrollarse con datos de prueba tras el corte.

- [ ] T020 [P] [US2] Gael — Crear cabina 3D con cámara sentada fija, panel modular y ventana al cielo; instanciar antena en `GAME/scenes/cockpit/cockpit.tscn`. Depende: T004, T019. Terminado: panel alcanzable y cielo visible, sin manual del otro rol. Cubre: FR-003 FR-008 FR-018.
- [ ] T021 [US2] Gael — Crear oficina 3D, escritorio/laptop y vista del cohete en plataforma; exponer interacción de foco en `GAME/scenes/tower/tower.tscn`. Depende: T020. Terminado: cámara ve laptop y cohete; escena no decide la ronda ni contiene UI duplicada. Cubre: FR-009 FR-018.
- [ ] T022 [P] [US2] Isra — Construir índice, rutas de páginas y lectura ampliada al enfocar laptop; definir volver/escape en `GAME/ui/manual/manual_shell.tscn`. Depende: T016, T019. Terminado: índice→sección y sección→índice requieren una acción por trayecto. Cubre: FR-003 FR-009 FR-010.
- [ ] T023 [US2] Isra — Crear HUD persistente con tiempo y pendientes fuera del contenedor de páginas/herramientas en `GAME/ui/hud/round_hud.tscn`. Depende: T022. Terminado: navegar nunca oculta, reinicia ni permite editar el reloj; máximo 1 s de diferencia en prueba estable. Cubre: FR-002 FR-018 SC-002.
- [ ] T024 [US2] Jorge — Conectar escenas finales y evento de foco con enrutamiento de input al rol correcto en `GAME/scenes/main.tscn`. Depende: T020, T021, T022, T023. Terminado: interactuar con laptop no envía intentos a cabina y el reloj queda visible. Cubre: FR-003 FR-008 FR-009 FR-010.
- [ ] T025 [US2] Sojo — Ejecutar Q06–Q07: vistas, lectura a 1280×720, rutas, reloj y medición de rendimiento en equipos identificados en `GAME/docs/qa/workstations.md`. Depende: T024. Terminado: capturas y mediciones acreditan legibilidad, aislamiento y objetivo ≥30 FPS. Cubre: FR-002 FR-008 FR-009 FR-010 FR-018 SC-002 SC-006.

## Fase 5 — US3: dificultad y herramienta

Validación independiente: Q08–Q10. La ampliación numérica es una propuesta para satisfacer dificultad.

- [ ] T026 [P] [US3] Kevin — Crear regla original A=2 B=5 C=7 D=9, generar dos pares, concatenar y multiplicar; producto entero 484..9801 en `GAME/scripts/modules/code_rule.gd`. Depende: T014, T019. Terminado: AB/CD se evalúa a 1975 y respuestas erróneas no resuelven; no se copia tabla de imagen. Cubre: FR-006 FR-011 FR-019.
- [ ] T027 [US3] Kevin — Crear display con dos pares, entrada de hasta 4 dígitos, Confirmar y feedback; rechazar vacío/decimal/fuera de rango en `GAME/scenes/modules/code_view.tscn`. Depende: T026. Terminado: emite intento válido y no decide victoria; wrong permite reintento. Cubre: FR-003 FR-006 FR-011 FR-018.
- [ ] T028 [P] [US3] Isra — Crear sección propia con tabla exacta, ejemplo 25×79=1975 y acceso a calculadora en `GAME/ui/manual/code_page.tscn`. Depende: T022, T026. Terminado: manual y evaluador comparten rule_version=1 y cubren todos los símbolos generables. Cubre: FR-010 FR-011 FR-019.
- [ ] T029 [US3] Isra — Crear multiplicación de dos enteros de dos cifras, limpiar y volver al manual sin eval arbitrario en `GAME/ui/tools/calculator.tscn`. Depende: T028. Terminado: desde índice dos acciones abren calculadora y una regresa a página; reloj sigue visible. Cubre: FR-002 FR-012 SC-004.
- [ ] T030 [P] [US3] Adrian — Conectar easy=[antenna] y normal=[antenna,code] al controlador; duración propuesta 180 s, sin cambiar durante play en `GAME/resources/difficulties/normal.tres`. Depende: T013, T026. Terminado: resolver solo una de normal nunca gana y los inactivos no cuentan. Cubre: FR-004 FR-013 SC-003.
- [ ] T031 [US3] Jorge — Integrar dos componentes y rutas de manual/herramienta por configuración en `GAME/scenes/main.tscn`. Depende: T024, T027, T028, T029, T030. Terminado: cambiar dificultad en lobby produce uno o dos módulos con manual y estado coherentes. Cubre: FR-004 FR-010 FR-011 FR-012 FR-013.
- [ ] T032 [US3] Sojo — Ejecutar Q08–Q10: cantidades, soluciones, errores y calculator/back; verificar casos límite de tabla en `GAME/docs/qa/difficulty-and-code.md`. Depende: T031. Terminado: evidencia acredita SC-003/SC-004 y ausencia de victoria prematura. Cubre: FR-004 FR-006 FR-011 FR-012 FR-013 SC-003 SC-004.

## Fase 6 — US4: desenlace y repetición

Validación independiente: Q11–Q12. Animaciones locales no deciden resultados.

- [ ] T033 [P] [US4] Gael — Crear presentación propia de despegue para torre y equivalente de cabina, activada por resultado host en `GAME/scenes/outcomes/launch.tscn`. Depende: T020, T021, T025. Terminado: un mismo success produce una presentación por puesto sin nueva decisión local. Cubre: FR-014 FR-019 SC-007.
- [ ] T034 [US4] Gael — Crear fallo cómico propio; punta-corcho y paracaídas opcionales dentro de esta tarea; interrupted muestra mensaje sin explosión en `GAME/scenes/outcomes/failure.tscn`. Depende: T033. Terminado: timeout y desconexión tienen presentaciones distintas y correctas. Cubre: FR-014 FR-015 FR-019 SC-007.
- [ ] T035 [P] [US4] Adrian — Conectar resultado terminal inmutable, retorno a lobby y nueva ronda solo con ambos listos; limpiar IDs/revision/readiness en `GAME/autoload/round_controller.gd`. Depende: T017, T030. Terminado: mensajes del intento anterior no afectan la siguiente ronda y fin repetido no duplica efectos. Cubre: FR-007 FR-015 FR-016 SC-007.
- [ ] T036 [P] [US4] Kevin — Completar reset de instancias para nueva ronda: pending, selección/entrada vacías y pistas nuevas en `GAME/scripts/modules/module_runtime.gd`. Depende: T027. Terminado: ningún componente conserva solved o respuestas de una ronda anterior. Cubre: FR-004 FR-016 SC-007.
- [ ] T037 [US4] Sojo — Ejecutar Q11–Q12 con éxito, timeout exacto, evento duplicado y dos rondas consecutivas en `GAME/docs/qa/outcomes-and-replay.md`. Depende: T032, T033, T034, T035, T036. Terminado: presentaciones únicas y estados limpios en ambos puestos documentados. Cubre: FR-007 FR-014 FR-015 FR-016 SC-007.

## Fase 7 — Entrega y verificación transversal

Validación final Q01–Q14; exportar no equivale a desplegar ni a demostrar Internet.

- [ ] T038 Jorge — Preparar exportación reproducible Windows y ficha de revisión/versión; excluir cachés y secretos en `GAME/export_presets.cfg`. Depende: T025, T032, T037. Terminado: dos builds equivalentes abren y corresponden a una revisión identificada. Cubre: FR-018 FR-020 SC-006.
- [ ] T039 Gael — Ejecutar con Adrian una sesión real entre dos redes externas, cinco rondas y una desconexión; Adrian corrige solo sus archivos si falla en `GAME/docs/qa/internet-session.md`. Depende: T038. Terminado: ruta de conexión y métricas descritas sin direcciones ni secretos; local/LAN no sustituye esta prueba. Cubre: FR-015 FR-020 SC-002 SC-005.
- [ ] T040 Sojo — Consolidar Q01–Q14, requisitos, FPS y evidencia entre equipos; marcar cada comprobación con resultado real y defectos en `GAME/docs/qa/acceptance.md`. Depende: T038, T039. Terminado: ninguna casilla se da por pasada solo por existir código; todos los criterios del prototipo tienen evidencia. Cubre: FR-001 FR-002 FR-003 FR-004 FR-005 FR-006 FR-007 FR-008 FR-009 FR-010 FR-011 FR-012 FR-013 FR-014 FR-015 FR-016 FR-017 FR-018 FR-019 FR-020 SC-001 SC-002 SC-003 SC-004 SC-005 SC-006 SC-007.
- [ ] T041 [P] Kevin — Consolidar procedencia/licencias de textos, imágenes, modelos y sonidos finales; separar las referencias del ejecutable en `GAME/docs/art/asset-register.md`. Depende: T034. Terminado: cada recurso distribuido tiene autor/licencia y no hay screenshots del juego de referencia empaquetados. Cubre: FR-019.
- [ ] T042 Isra — Redactar guía en español y recorrido de demostración: conectarse, roles, manual, herramienta, victoria, fallo y reinicio en `GAME/docs/demo/README.md`. Depende: T029, T037, T040, T041. Terminado: otra pareja reproduce el recorrido con las instrucciones y conoce límites/pendientes. Cubre: FR-001 FR-010 FR-012 FR-014 FR-016 FR-020.

## Dependencias y orden de ejecución

Preparación (T001→T002→T003–T006) → base (T007–T010) → corte US1 (T013–T019) → integración US2 (T020–T025) y ampliación US3 (T026–T032) → US4 (T033–T037) → exportación y aceptación (T038–T042). Las dependencias exactas de cada línea prevalecen sobre el orden de numeración: una tarea posterior puede empezar si todas sus dependencias están cerradas. Ejemplo: T026 puede avanzar en paralelo al arte de US2 después de T019; T031 espera a ambas líneas.

## Ejecución paralela concreta

- Tras T002: Gael T004, Kevin T005, Isra T006, Sojo T003 y Adrian T007; Jorge prepara integración cuando sus prerequisitos estén listos.
- US1: Gael T015, Kevin T014, Isra T016 y Adrian T013; después Adrian T017, Jorge T018 y Sojo T019. Cada uno modifica archivos distintos.
- US2/US3: Gael T020–T021 mientras Kevin T026–T027; Isra atiende primero T022–T023 y después T028–T029, sin simultanear tareas propias. Adrian T030 no toca las escenas.
- US4: Gael T033–T034, Adrian T035 y Kevin T036; Sojo integra evidencia en T037, sin convertirse en único responsable de que el trabajo ajeno funcione.

## Estrategia incremental

Primer corte: T001–T019, usando solo antena y vistas provisionales. El prototipo completo pedido en la etapa incluye también T020–T042; no se presenta el corte inicial como satisfacción de todas las imágenes y criterios. Cada dueño valida su tarea antes de entregarla, el integrador conecta escenas y Sojo mantiene evidencia independiente. La carga real se revisa al terminar el primer corte; siete tareas por persona es reparto inicial, no estimación de duración.

## Formato de entrega de una tarea

ID y responsable; rama `<id>/<task-id>-<descripcion>`; revisión Git; archivos modificados; criterio probado y evidencia; límites o fallo pendiente; checkpoint atribuido. Un nombre en esta lista no concede permisos GitHub ni demuestra una cuenta. No se han creado issues ni asignaciones remotas.
