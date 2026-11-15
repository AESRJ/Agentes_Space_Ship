# Feature Specification: Launch Control — prototipo cooperativo

**Feature Branch**: `jorge/launch-control-godot`
**Created**: 2026-11-14
**Status**: propuesta lista para planificación; sin juego implementado.
**Input**: Jorge pide usar `Etapa_1_final.md` y las imágenes, ignorar la metodología del documento y distribuir el prototipo entre los seis integrantes mediante Spec Kit. La elección técnica explícita está en plan.md.

## Contexto y autoridad

**Actualización del equipo**: Jorge aclara que Sojo no está incorporado por ahora. El equipo activo es Jorge, Gael, Adrian, Kevin e Isra; ver reparto actualizado. La mención original de seis conserva el origen del encargo, no el estado actual.

La fuente define dos puestos en primera persona, panel modular, laptop con manual, cuenta regresiva, dificultad por cantidad de componentes, despegue y fallo cómico. Se conserva su regla de antena. Su sección «Primer mensaje para trabajar con IA» no gobierna el proceso: Jorge solicita Specify → Plan → Tasks. Las fuentes originales y hashes están en [references](references/README.md).

Jorge aprobó dos PC en la misma LAN como criterio final del prototipo (ADR-0006, 2026-11-15); Internet entre redes externas queda fuera de esta entrega. Los valores de tiempo, segundo módulo, presentación simplificada y responsabilidades se proponen para hacer ejecutable el plan; no representan aprobación individual de los demás integrantes.

## User Scenarios & Testing

### User Story 1 — Resolver juntos la antena (Priority: P1)

Dos personas eligen roles distintos, confirman que están listas y juegan la misma ronda. El astronauta describe la luz y opera; la torre consulta el manual y dicta la solución. Ambos ven el reloj y el mismo resultado.

**Why this priority**: es un corte completo que prueba cooperación, información repartida y consecuencias, inicialmente con vistas provisionales.

**Independent Test**: dos equipos y una antena; ejecutar fija/acierto, parpadeante/acierto, error/reintento y vencimiento. No necesita el módulo numérico ni arte final.

**Acceptance Scenarios**:
1. **Given** dos roles distintos listos, **When** empieza la ronda, **Then** se fija una configuración y el reloj empieza una sola vez.
2. **Given** luz fija y tiempo disponible, **When** astronauta confirma luna, **Then** aparece Listo y se gana si no quedan pendientes.
3. **Given** luz parpadeante, **When** confirma estrella a tiempo, **Then** queda Listo; luna deja pendiente y permite reintento.
4. **Given** tiempo vencido y un pendiente, **When** llega una respuesta tardía, **Then** ambos conservan fallo, sin victoria posterior.
5. **Given** ronda activa, **When** uno se desconecta, **Then** el otro ve interrumpida y puede volver al inicio, sin desenlace normal ficticio.

### User Story 2 — Operar desde cabina y torre (Priority: P1)

Astronauta ve cielo y panel desde su asiento. Torre ve oficina, laptop y cohete; enfoca la laptop, abre el índice y consulta instrucciones sin perder el reloj.

**Why this priority**: reproduce los puestos pedidos con interacción comprensible y sin paseo libre.

**Independent Test**: cada escena se abre con datos de prueba para revisar visibilidad e interacción; la integración usa el estado de US1.

**Acceptance Scenarios**:
1. **Given** astronauta, **When** entra, **Then** ve panel, cielo y controles al alcance, sin manual.
2. **Given** torre, **When** recorre índice → sección → índice y vuelve a la oficina, **Then** el reloj no desaparece ni se reinicia y no puede operar cabina.
3. **Given** ventana 1280 × 720, **When** se lee el manual, **Then** instrucciones y controles se ven sin recortes.

### User Story 3 — Elegir dificultad y consultar una herramienta (Priority: P2)

Fácil activa antena; normal activa antena y un módulo numérico propuesto. Astronauta dicta dos pares de letras y torre usa una tabla original y calculadora para indicar la respuesta.

**Why this priority**: cubre cantidad de componentes y herramienta de la referencia sin implementar su catálogo completo.

**Independent Test**: fácil tiene uno y normal dos; resolver solo uno de normal no gana. La calculadora y el módulo pueden probarse con una ronda simulada.

**Acceptance Scenarios**:
1. **Given** fácil y normal, **When** inicia cada ronda, **Then** se activan respectivamente uno y dos componentes.
2. **Given** tabla propuesta A=2, B=5, C=7, D=9 y panel AB / CD, **When** torre traduce 25 y 79 y calcula 1975, **Then** confirmar 1975 resuelve el módulo.
3. **Given** entrada vacía o incorrecta, **When** se confirma, **Then** sigue pendiente, muestra el rechazo y permite reintentar a tiempo.
4. **Given** calculadora abierta, **When** vuelve al manual, **Then** conserva el reloj y no cambia el estado de la ronda.

### User Story 4 — Ver desenlace y volver a jugar (Priority: P2)

La pareja ve despegue o fallo cómico y luego puede iniciar otra ronda limpia.

**Why this priority**: completa la presentación tras probar resultados textuales en US1.

**Independent Test**: forzar victoria y vencimiento con dos puestos y reiniciar; revisar efectos únicos y estados limpios, sin necesitar resolver manualmente todos los módulos.

**Acceptance Scenarios**:
1. **Given** éxito, **When** termina, **Then** cada puesto reproduce una presentación coherente una sola vez.
2. **Given** vencimiento, **When** termina, **Then** torre ve fallo cómico y cabina una presentación equivalente; no exige la misma cámara.
3. **Given** ambos listos de nuevo, **When** empieza otra ronda, **Then** reloj, componentes y entradas no heredan datos anteriores.

### Edge Cases

Rol ocupado no se duplica; dificultad no cambia durante ronda; Confirmar repetido no duplica efectos; respuestas de otra ronda o a módulos inactivos se descartan; torre no opera cabina; no se inicia sin segundo participante. Acierto recibido exactamente al vencimiento pierde. La asimetría no puede impedir que una persona memorice reglas aprendidas.

## Requirements

### Functional Requirements

- **FR-001**: admitir exactamente dos jugadores con roles distintos y comenzar solo con ambos listos.
- **FR-002**: mostrar cuenta regresiva común, visible durante manual y herramientas.
- **FR-003**: separar pistas/controles del astronauta de reglas/herramientas de torre.
- **FR-004**: exigir todos los componentes activos; un inactivo nunca bloquea ni concede victoria.
- **FR-005**: antena fija → luna; parpadeante → estrella; confirmar a tiempo deja Listo.
- **FR-006**: error deja pendiente y permite reintento, sin penalización temporal adicional propuesta.
- **FR-007**: decidir un único resultado compartido; resolver antes de cero gana y vencer con pendientes falla.
- **FR-008**: mostrar panel accesible y cielo desde cabina en primera persona.
- **FR-009**: mostrar oficina, laptop y cohete en plataforma desde torre en primera persona.
- **FR-010**: ofrecer índice y sección por componente activo; abrir sección desde índice y regresar requiere una acción por trayecto.
- **FR-011**: ofrecer en normal el módulo numérico propuesto con A=2, B=5, C=7, D=9, dos pares y respuesta por multiplicación.
- **FR-012**: permitir multiplicar dos enteros de dos cifras en calculadora accesible desde esa sección y volver al manual.
- **FR-013**: fácil activa uno y normal dos; dificultad fijada antes de empezar.
- **FR-014**: presentar despegue y fallo cómico coherentes con el resultado en ambos puestos.
- **FR-015**: ante desconexión mostrar interrumpida y permitir volver a inicio, sin inventar resultado normal.
- **FR-016**: otra ronda reinicia todos los datos transitorios tras nueva confirmación de ambos.
- **FR-017**: permitir operaciones de módulo solo al astronauta, para componente activo, ronda vigente y tiempo disponible.
- **FR-018**: complementar color con forma/texto y permitir leer y operar a 1280 × 720.
- **FR-019**: producir recursos, tablas, textos e ilustraciones propios; las imágenes son referencias, no assets del juego.
- **FR-020**: demostrar la ronda entre dos PC físicos en la misma LAN; loopback en una sola PC no basta (ADR-0006).

### Key Entities

Sesión con participantes y roles; ronda con dificultad, tiempo, componentes y resultado; componente con pista, respuesta y estado; sección con regla y herramienta; intento asociado a participante y ronda.

## Success Criteria

### Measurable Outcomes

- **SC-001**: ambos equipos coinciden en los cuatro casos de antena de US1, intercambiando qué rol aloja la partida.
- **SC-002**: relojes difieren como máximo un segundo durante tres minutos de conexión estable y permanecen visibles al consultar manual/herramientas.
- **SC-003**: fácil activa exactamente uno y normal dos; resolver solo uno en normal nunca gana.
- **SC-004**: desde índice se llega a calculadora en dos acciones y se regresa al manual en una, sin perder el reloj.
- **SC-005**: cinco rondas entre dos PC en la misma LAN, incluyendo éxito, vencimiento y error recuperado, no muestran desenlaces contradictorios; desconexión adicional produce interrumpida.
- **SC-006**: en dos equipos identificados, cada vista es legible a 1280 × 720 y mantiene al menos 30 cuadros por segundo durante una ronda; registrar medición y condiciones.
- **SC-007**: éxito y fallo disparan una presentación por ronda y dos rondas consecutivas no heredan entradas ni módulos resueltos.

## Assumptions

Propuestas de partida: 180 segundos en ambas dificultades; voz externa/presencial; dos escenarios 3D con cámara fija; laptop enfocable con lectura ampliada; antena primero y módulo numérico después. No hay voz integrada, cuentas, matchmaking, paseo libre, persistencia, migración de host o reconexión automática. Punta-corcho y paracaídas siguen como propuesta sustituible por un efecto cómico simple. El repositorio del ejecutable aún debe identificarse; aquí solo se planifica.
