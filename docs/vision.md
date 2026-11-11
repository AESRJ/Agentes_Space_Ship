# Contexto y visión provisional

## Actualización posterior de la misma fecha

El usuario aporta «Órbita: contacto con Tierra» como nombre provisional y propone construir, ensayar, lanzar, operar y evaluar consecuencias. Solicita planear con Unity y C#, y confirma dos PC por Internet. Véase [el plan de trabajo](plan-unity.md). Esto sustituye las menciones posteriores a motor, lenguaje y conexión sin decidir. El alcance detallado y la arquitectura siguen propuestos.

Actualizado: 2026-11-10. Estado: exploración; no es una especificación aprobada.

## Fuentes y autoridad

- S1: texto del desafío y explicación del usuario en esta conversación, 2026-11-10.
- S2: imagen aportada «Lluvia de ideas en el salon».
- S3: imagen aportada «Temas a investigar».
- Tablero asociado: https://miro.com/app/board/uXjVEWUr6N4=/ . No se ha leído directamente; este documento se basa en S1–S3, no en una revisión completa del tablero.

El texto del desafío es una traducción aportada por el usuario. Su redacción oficial, edición, criterios de evaluación y vínculo oficial aún no se han verificado. Las ideas del tablero son propuestas, no requisitos aprobados. La aclaración más reciente del usuario orienta el concepto actual sin resolver todas las decisiones.

## Problema descrito en S1

Las decisiones de una misión espacial resultan abstractas para estudiantes que no pueden experimentar su ciclo completo. El desafío aportado propone un juego para diseñar, administrar y simular una misión: elegir objetivos; seleccionar instrumentos y sistemas; administrar presupuesto, masa, energía y capacidad de lanzamiento; afrontar eventos; simular resultados y explicar éxito, fracaso o cumplimiento parcial.

El aprendizaje central es comprender las compensaciones entre objetivos, recursos y riesgos. No se ha especificado edad ni nivel académico de los jugadores.

## Concepto actual expresado por el equipo

Un juego cooperativo en el que astronauta y torre de control se coordinan para completar una misión. Durante el lanzamiento aparecen problemas que se resuelven con puzzles inspirados en situaciones reales. El equipo cita como referencia los puzzles de Keep Talking and Nobody Explodes. Todavía considera vaga y abierta esta idea.

S2 también propone niveles con dificultad creciente y destinos diferentes. Una nota plantea tres jugadores: torre de control, astronautas y estación espacial. Otra menciona comunicación limitada entre «los tres astronautas». S1 enfatiza astronauta y torre de control, pero no establece definitivamente dos jugadores ni descarta el tercer rol. No convertir estas formulaciones distintas en una decisión cerrada.

S3 identifica seis líneas de investigación: dificultades de astronautas; problemas matemáticos o físicos; herramientas de desarrollo; diseño de naves; instrumentos científicos; restricciones orbitales. Son temas para investigar, no hechos científicos ya comprobados ni sistemas obligatorios del MVP.

## Síntesis propuesta por el asistente

Juego educativo cooperativo de misión espacial: los participantes toman decisiones sobre recursos y resuelven incidencias mediante información y acciones distribuidas entre roles. El lanzamiento puede ser la primera porción jugable.

La distribución asimétrica de información es una propuesta de diseño derivada de la referencia del equipo. Aún falta decidir qué ve, sabe y puede hacer cada rol y qué limita la comunicación. Inspirarse en el principio cooperativo no implica reproducir puzzles, textos o recursos del juego de referencia.

## Relación entre el prototipo y el desafío

Un prototipo concentrado en puzzles durante el lanzamiento permite probar la cooperación, pero no demuestra por sí solo diseño, gestión y operación de una misión completa.

Propuesta para conectar ambos: una preparación breve donde se eligen componentes bajo límites; una ejecución cooperativa donde esas elecciones afectan recursos y opciones; y una evaluación que explica las consecuencias. El alcance exacto y la cobertura del desafío deben acordarse antes de declarar cumplimiento.

## Límites provisionales para futuros agentes

- No presentar ideas o ejemplos de este documento como funcionalidades aprobadas o existentes.
- No asumir motor, lenguaje, plataforma, número definitivo de jugadores, modalidad de conexión, voz integrada, 2D/3D ni física de alta fidelidad.
- Toda afirmación de realismo exige una fuente técnica verificable. Registrar las simplificaciones educativas y evitar presentar parámetros inventados como valores reales.
- Vincular cada puzzle a un objetivo de aprendizaje, una necesidad de cooperación y una consecuencia observable.
- Evaluar nuevas funciones según su contribución al concepto; documentar ampliaciones de alcance como propuestas.
- Los agentes ayudan al equipo de desarrollo; no se ha pedido incorporar personajes de IA al juego.

## Decisiones abiertas

1. Dos roles o tres; distribución de información y acciones.
2. Primer entregable centrado en lanzamiento o ciclo simplificado completo.
3. Público objetivo, dificultad y duración de partida.
4. Plataforma, motor y modalidad local/remota.
5. Significado de comunicación limitada: turnos, ventanas temporales, vocabulario, información incompleta u otro mecanismo.
6. Recursos, criterios de éxito y nivel de fidelidad científica.
7. Reto oficial, calendario, repositorio del videojuego y responsables humanos. El repositorio de agentes ya fue indicado por el usuario: `AESRJ/Agentes_Space_Ship`.

No es necesario resolver todo para discutir el concepto; sí resolver las decisiones que condicionan cada implementación antes de empezarla.
