# Órbita: contacto con Tierra — base de desarrollo

Fecha: 2026-11-10. Estado: plan propuesto; videojuego sin implementar.

## Autoridad y alcance

El usuario solicita empezar un juego con Unity y C# y planear su base. Confirma después dos PC conectados por Internet. Estas son decisiones expresas de esta conversación. El nombre es provisional. El resto de este documento organiza su propuesta y recomendaciones técnicas; no constituye aprobación de cada detalle.

Este repositorio conserva el plan y la memoria. El repositorio del juego sigue pendiente; no se crea aquí un proyecto Unity. Windows como plataforma de distribución todavía debe confirmarse, aunque el equipo trabaja desde Windows.

## Experiencia que se busca probar

Dos roles con información y acciones complementarias: astronauta en cabina y torre con pronósticos, procedimientos y telemetría. Construir bajo restricciones debe cambiar las opciones durante el vuelo y explicar el resultado científico. El ciclo objetivo es elegir misión, construir, ensayar, despegar, operar en órbita y revisar consecuencias.

Primera versión candidata: observación terrestre, dos jugadores, 20–25 minutos, dos lanzadores, unas diez opciones de módulos y tres problemas de energía, orientación y comunicación. La duración general de 25–40 minutos queda como horizonte. Cuatro jugadores, Marte y asteroides son ampliaciones posteriores.

## Hitos y condiciones de salida

| Hito | Entregable | Evidencia para avanzar |
| --- | --- | --- |
| 0. Preparación | Repositorio del juego acordado, versión exacta de Unity y paquetes, proyecto mínimo, reglas Git y recursos | Ambos desarrolladores abren la misma revisión sin errores; las licencias y compatibilidad se revisan antes de fijar paquetes |
| 1. Conexión | Crear/unirse a sesión por Internet, dos roles exclusivos y vistas provisionales | Dos PC en redes diferentes se conectan; una acción válida aparece en ambos; se comprueba desconexión |
| 2. Prototipo cooperativo | Nave ya en órbita, batería, generación solar, cámara, datos y transmisión; escenario de 5–8 minutos | Ambos toman decisiones necesarias; sus acciones cambian recursos; el resultado tiene una causa explicable |
| 3. Preparación de nave | Dos variantes por sistema y límites de presupuesto/masa; ensayo del mismo modelo | Dos configuraciones producen consecuencias distintas en el mismo escenario; el ensayo detecta un déficit previsible |
| 4. Misión completa | Lanzamiento simplificado, fase orbital y cierre de 20–25 minutos | Se puede completar, abortar o lograr éxito parcial; se entienden orientación y velocidad lateral |
| 5. Validación | Informe causal y repetición del escenario con condiciones iguales | Una pareja identifica qué decisión produjo el resultado y propone un cambio verificable |

No fijar calendario hasta conocer disponibilidad y experiencia del equipo. Priorizar el hito 2 antes de producir cabina final, hangar detallado o muchos componentes.

## Base técnica propuesta

- Unity con C#; versión soportada y paquetes exactos por verificar al crear el proyecto. URP y Blender son candidatos de producción.
- Núcleo de simulación C# separado de escenas y red. Recibe comandos, avanza por pasos de tiempo y produce estado y eventos. Sus reglas deben poder comprobarse sin interfaces.
- Definiciones de módulos y misiones como datos; ScriptableObjects son un candidato. Separar definiciones de configuración elegida y estado mutable de cada partida.
- Una autoridad calcula recursos, valida acciones y evalúa objetivos. Los clientes envían intenciones; no escriben directamente batería, combustible ni resultados. Filtrar la información enviada según el rol.
- Propuesta de red: un jugador aloja la partida y el otro se une mediante código. Evaluar Netcode for GameObjects y Relay/servicios de sesión para evitar exigir configuración manual del router. Comprobar compatibilidad, cuentas y condiciones antes de adoptarlos. La red no equivale a voz integrada.
- Desconexión inicial propuesta: pausar y mostrar cierre/reinicio controlado si no se recupera la conexión. Reconexión y migración del anfitrión quedan pendientes; no prometerlas en el primer prototipo.
- Presentación: vistas provisionales separadas de astronauta y torre. La torre necesita acciones propias, por ejemplo preparar ventanas de transmisión y validar planes; el astronauta orienta y ejecuta cambios locales.
- Evaluación: registro estructurado de decisiones y cambios de recursos. Guardar causas explícitas; el informe no debe inventar explicaciones a partir del resultado final.

## Reglas mínimas y aprendizaje

Potencia de generación y consumo se expresan en unidades de juego por segundo; batería en unidades de energía de juego. Cambio de batería = (generación − consumo) × tiempo, limitado por capacidad y cero. Datos capturados, almacenados y transmitidos se contabilizan por separado. Solo los datos entregados cuentan como transmitidos. Combustible de lanzamiento y de maniobra son reservas distintas.

Estos modelos son simplificaciones propuestas, sin parámetros NASA ni fidelidad orbital acreditada. Primero se valida la cooperación; después se investiga y documenta cada fenómeno. Cada puzzle deberá usar [la plantilla](puzzles/TEMPLATE.md) con fuentes, reparto de información, reglas, integración y pruebas antes de implementarse. Este plan no sustituye esas fichas.

El escenario inicial debe permitir conservar datos y abandonar un objetivo opcional para mantener energía de comunicación. Cada incidencia tendrá pista, margen de reacción y consecuencia; evitar eventos aleatorios sin señales.

## Verificación prevista

Comprobar límites de batería y datos, rechazo de comandos del rol incorrecto, acciones duplicadas, desconexión y consistencia entre anfitrión/cliente. Verificar que ensayo y misión usan las mismas reglas con entradas equivalentes. Repetir condiciones iniciales y semilla al comparar diseños; no prometer reproducibilidad exacta de toda la física del motor.

En pruebas con personas observar qué decisión tomó cada rol, cuándo necesitaron comunicarse y si pueden explicar una consecuencia sin ayuda. Todas estas pruebas están pendientes: no existe implementación ni sesión jugable verificada.

## Pendientes que condicionan la implementación

Referencia técnica consultada el 2026-11-10: [integración oficial Relay y Netcode for GameObjects](https://docs.unity.com/en-us/mps-sdk/tutorials/relay-and-ngo). Documenta la conexión mediante código; no demuestra que este proyecto ya esté conectado ni valida costos o versiones específicas.

Destino del repositorio, plataforma final, experiencia y disponibilidad del equipo, público y edad, versión/paquetes, presupuesto de servicios, comunicación por voz externa o integrada y comportamiento final ante desconexiones. La conexión por Internet y Unity/C# ya fueron expresados por el usuario.
