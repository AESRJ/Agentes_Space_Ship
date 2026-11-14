# Contexto y visión provisional

Actualizado: 2026-11-14. Estado: exploración; **no es una especificación aprobada**. Todo lo marcado como *Propuesta* es una idea para discutir, no una funcionalidad existente ni acordada.

## Actualización posterior de la misma fecha (2026-11-10)

El usuario aporta «Órbita: contacto con Tierra» como nombre provisional y propone construir, ensayar, lanzar, operar y evaluar consecuencias. Solicita planear con Unity y C#, y confirma dos PC por Internet. Véase [el plan de trabajo](plan-unity.md). Esto sustituye las menciones posteriores a motor, lenguaje y conexión sin decidir. El alcance detallado y la arquitectura siguen propuestos.

El usuario también indicó (2026-11-14) que quiere hacerlo en 3D. Se registra como intención del equipo; el grado de 3D (cabina, escenarios, torre) sigue por definir.

## Fuentes y autoridad

- S1: texto del desafío y explicación del usuario en esta conversación, 2026-11-10.
- S2: imagen aportada «Lluvia de ideas en el salon».
- S3: imagen aportada «Temas a investigar».
- S4: borrador de diseño previo elaborado por el asistente (experiencia central, roles, módulos, puzzles, simulación, resultados, herramientas). Es propuesta, no requisito. Sus referencias a NASA/ESA no se han verificado de nuevo aquí.
- Tablero asociado: https://miro.com/app/board/uXjVEWUr6N4=/ . No se ha leído directamente; este documento se basa en S1–S4, no en una revisión completa del tablero.

El texto del desafío es una traducción aportada por el usuario. Su redacción oficial, edición, criterios de evaluación y vínculo oficial aún no se han verificado. Las ideas del tablero son propuestas, no requisitos aprobados.

## Problema descrito en S1

Las decisiones de una misión espacial resultan abstractas para estudiantes que no pueden experimentar su ciclo completo. El desafío propone un juego para diseñar, administrar y simular una misión: elegir objetivos; seleccionar instrumentos y sistemas; administrar presupuesto, masa, energía y capacidad de lanzamiento; afrontar eventos; simular resultados y explicar éxito, fracaso o cumplimiento parcial.

El aprendizaje central es comprender las compensaciones entre objetivos, recursos y riesgos. No se ha especificado edad ni nivel académico.

## Concepto actual expresado por el equipo

Un juego cooperativo en el que astronauta y torre de control se coordinan para completar una misión. Durante el lanzamiento aparecen problemas que se resuelven con puzzles inspirados en situaciones reales. La referencia citada es Keep Talking and Nobody Explodes; el equipo la considera todavía vaga y abierta.

S2 propone niveles con dificultad creciente y destinos diferentes. Una nota plantea tres jugadores (torre, astronautas, estación espacial); otra menciona comunicación limitada entre «los tres astronautas». S1 enfatiza astronauta y torre, sin descartar definitivamente el tercer rol. No convertir estas formulaciones distintas en una decisión cerrada.

S3 identifica seis líneas de investigación: dificultades de astronautas; problemas matemáticos o físicos; herramientas de desarrollo; diseño de naves; instrumentos científicos; restricciones orbitales. Son temas por investigar, no hechos comprobados ni sistemas obligatorios del MVP.

## Síntesis propuesta por el asistente

Juego educativo cooperativo de misión espacial: los participantes toman decisiones sobre recursos y resuelven incidencias mediante información y acciones distribuidas entre roles. La distribución asimétrica de información es una propuesta derivada de la referencia del equipo. Inspirarse en el principio cooperativo no implica reproducir puzzles, textos o recursos del juego de referencia.

---

# Diseño detallado (Propuesta)

## 1. Pilares de diseño

1. **Las decisiones del hangar importan en vuelo.** Lo que se elige al construir la nave cambia lo que se puede hacer durante la misión. Es la identidad del juego y lo que conecta con el desafío.
2. **Ninguno tiene toda la información.** Cada rol ve datos distintos y debe comunicarlos para decidir.
3. **Cada puzzle es un problema de operación.** Nada de acertijos arbitrarios: cada uno enseña una relación (energía, trayectoria, comunicación, temperatura).
4. **Los resultados se explican.** El informe final traza decisión → cambio de recursos → consecuencia.
5. **Simplificado pero consistente.** Las relaciones entre variables son coherentes aunque los números sean unidades de juego.

## 2. Ciclo de juego

Elegir misión → construir la nave → ensayar → despegar → fase orbital → resolver incidencias → cumplir objetivos → analizar resultados.

| Fase | Qué ocurre | Quién actúa | Qué aprende el jugador |
|---|---|---|---|
| Elegir misión | Se presentan objetivo principal, opcionales y condiciones de seguridad | Ambos | Qué se necesita lograr y qué limita |
| Construir | Se eligen módulos y lanzador bajo límites | Ambos, con discusión | Compensaciones entre masa, costo, energía y beneficio |
| Ensayar | Simulación previa con informe de problemas previsibles | Ambos | Detectar fallos antes de que ocurran |
| Despegar | Lanzamiento con bandas objetivo de orientación y empuje | Astronauta opera, torre guía | Velocidad horizontal además de altura |
| Fase orbital | Operar instrumentos, energía y comunicaciones | Ambos | Comprobar si la nave sirve para su objetivo científico |
| Incidencias | Eventos con pista previa y tiempo para actuar | Ambos | Diagnóstico y priorización |
| Cierre | Informe causal y línea de tiempo | Ambos | Por qué ocurrió el resultado |

## 3. Roles y distribución de información

Pregunta abierta: dos roles o tres (ver decisiones abiertas). Lo siguiente describe dos roles; el tercero se trata al final de esta sección.

| | Astronauta | Torre de control |
|---|---|---|
| Ve | Cabina, instrumentos, alarmas locales, vista exterior, respuesta de la nave | Trayectoria prevista, tendencias de telemetría, ventanas de comunicación, manuales y límites |
| Hace | Orienta, ajusta empuje, separa etapas, activa sistemas, opera instrumentos | Diagnostica, calcula maniobras simplificadas, prioriza objetivos, guía procedimientos |
| Necesita del otro | Trayectoria deseada, interpretación de fallos, procedimientos | Lecturas locales, confirmaciones, ejecución física |

Principios:

- La torre no solo lee instrucciones: compara sensores, prepara secuencias de encendido, calcula cuánto puede sostenerse una carga eléctrica y decide qué datos transmitir primero.
- El astronauta también razona: detecta vibraciones, observa una antena mal desplegada, nota diferencias entre cabina y telemetría de Tierra.
- **Confirmación breve (read-back)** para evitar ambigüedad: «Apaga el espectrómetro; conserva la cámara» → «Confirmo: espectrómetro apagado, cámara encendida» → «Correcto. Comprueba el consumo». El juego puede enseñarla y, opcionalmente, recompensarla o hacerla obligatoria en acciones críticas.
- **Tercer rol (estación o astronautas adicionales):** solo si el prototipo de dos roles funciona. Podría aportar un segundo canal de comunicación con ventanas limitadas. Documentar como ampliación, no como requisito.

## 4. Comunicación limitada (opciones por evaluar)

El significado de «comunicación limitada» no está decidido. Mecanismos candidatos:

- **Ventanas temporales:** solo se puede transmitir cuando la estación está en línea de vista.
- **Información incompleta:** cada rol ve datos que el otro no ve (base del diseño asimétrico).
- **Vocabulario controlado:** mensajes con términos estándar.
- **Demora:** en misiones lejanas, instrucciones enviadas con antelación.
- **Voz integrada o chat:** sin decidir; a probar si la voz externa (llamada aparte) basta para el prototipo.

Criterio de selección: que genere cooperación real sin frustrar. Probar con jugadores antes de fijar.

## 5. Misiones y niveles

| Misión | Objetivo principal | Reto de diseño | Reto de vuelo |
|---|---|---|---|
| Observar la Tierra | Obtener y transmitir imágenes de tres regiones | Equilibrar cámara, batería y almacenamiento | Apuntar y aprovechar ventanas |
| Explorar Marte | Desplegar una sonda y obtener datos atmosféricos | Reservar recursos para una misión larga | Preparar maniobras, comunicación demorada |
| Estudiar un asteroide | Medir su composición en un encuentro breve | Elegir instrumentos y combustible de maniobra | Orientar con precisión en una ventana corta |

- Primera misión propuesta: **observación terrestre**, porque enseña todo el sistema sin viajes interplanetarios.
- Marte y asteroide como misiones de **sonda** desplegada desde la nave tripulada, para evitar soporte vital de larga duración, radiación y retorno (alcance mucho mayor).
- La dificultad crece reduciendo márgenes y exigiendo decisiones más difíciles, no acumulando fallos imposibles.

## 6. Construcción de la nave

Cada módulo muestra: costo, masa, consumo o generación eléctrica, beneficio y limitaciones. Los valores son **unidades de juego**, identificadas como tales; no son especificaciones reales.

| Sistema | Elección | Ventaja | Consecuencia |
|---|---|---|---|
| Instrumentos | Cámara básica / alta resolución | Más detalle científico | Más masa, consumo y datos |
| Energía | Paneles pequeños / grandes | Más generación | Más masa; hay que orientarlos al Sol |
| Almacenamiento | Batería pequeña / grande | Más autonomía en eclipses | Más costo y masa |
| Comunicación | Antena sencilla / direccional | Más datos transmitidos | Exige apuntar con precisión |
| Propulsión | Menos / más combustible de maniobra | Más capacidad de corrección | Más masa al lanzamiento |
| Protección | Aislamiento térmico y redundancia | Tolera más fallos o condiciones | Consume presupuesto y capacidad |
| Lanzador | Ligero / mayor capacidad | Más carga transportable | Más costo, menos dinero para instrumentos |

Indicadores de interfaz propuestos:

- **Balance eléctrico:** «Produces 8 y consumes 10: estás usando batería».
- **Autonomía estimada:** «Con esta configuración quedan cuatro minutos».
- Separar visualmente generación, almacenamiento y consumo.

## 7. Límites visibles

| Recurso | Qué limita | Qué puede hacer el equipo |
|---|---|---|
| Presupuesto | Componentes y lanzador | Reducir alcance o aceptar menos redundancia |
| Masa | Carga que lleva el lanzador al destino | Quitar módulos o contratar más capacidad |
| Potencia y batería | Equipos simultáneos y duración | Programar turnos de uso |
| Combustible de maniobra | Correcciones disponibles | Pilotar con precisión o reducir objetivos |

- El combustible de lanzamiento y el de maniobras posteriores aparecen **separados**.
- La capacidad del lanzador depende del destino (órbita terrestre ≠ trayectoria a Marte).

## 8. Pilotaje (3D, accesible)

Controles del astronauta:

- **Orientación:** hacia dónde apunta la nave.
- **Empuje:** cuánto acelera.
- **Acciones de configuración:** separar etapas, desplegar paneles, activar sistemas.

La torre indica una **banda objetivo** (por ejemplo, mantener inclinación dentro de una zona y cortar motor al alcanzar una trayectoria aceptable), no una secuencia fija de botones.

Apoyos de aprendizaje:

- Mostrar trayectoria prevista y deseada.
- Traducir errores a mensajes como «demasiado alto, poca velocidad lateral».
- Permitir pequeñas correcciones antes de perder la misión.
- Aumentar la precisión exigida de forma progresiva.

Propuesta técnica para empezar: trayectoria simplificada en un plano, representada en 3D; ampliar la libertad de vuelo después.

## 9. Puzzles interactivos: paneles variables e incidencias de despegue (Propuesta)

Regla del equipo: cada puzzle se vincula a un **objetivo de aprendizaje**, una **necesidad de cooperación** y una **consecuencia observable**. Esta sección define dos familias nuevas, pensadas para resolverse hablando en el momento: **paneles que cambian** e **incidencias de despegue guiadas paso a paso**. El catálogo base anterior queda en 9.7.

### 9.1 Paneles de cabina variables

**Idea:** la nave tiene la misma lógica de funciones (activar respaldo de sensor, cortar un equipo, separar etapa, orientar antena), pero el panel físico que las expone cambia. El astronauta ve el panel; la torre tiene el catálogo y el procedimiento. Ninguno puede resolver solo.

**Tres modelos propuestos (nombres provisionales, de juego):**

| Modelo | Aspecto | Cómo se opera | Rasgos que lo distinguen |
|---|---|---|---|
| A «Analógico» | Diales, palancas grandes, luces testigo fijas | Mover palancas y leer agujas | Borde de panel de un color, 4 diales redondos, palanca principal con tapa roja |
| B «Digital» | Pantallas con menús y pocos botones físicos | Navegar menús y confirmar | Pantalla central dividida en 3 zonas, botones de función en la parte inferior |
| C «Mixto» | Interruptores con tapas de seguridad y luces que parpadean con patrones | Levantar tapa, accionar, leer patrón | Fila de interruptores con tapas, placa de serie con prefijo visible |

**Cómo se identifica el modelo (puzzle de comunicación):**

1. El astronauta describe lo que ve sin saber el nombre: forma, cantidad, colores, disposición, texto de la placa.
2. La torre compara con su catálogo de siluetas y hace preguntas discriminantes («¿Las palancas tienen tapa?», «¿Cuántos diales hay en la fila superior?»).
3. La torre propone un modelo; el astronauta confirma con un detalle adicional.
4. Solo entonces la torre entrega el procedimiento del modelo correcto.

Para que describir importe, los modelos deben **parecerse en algo**: dos de ellos comparten, por ejemplo, el mismo color de borde, de modo que una descripción incompleta lleva a un procedimiento equivocado.

**Capas de variación (de menos a más difícil):**

| Capa | Qué cambia | Ejemplo |
|---|---|---|
| 1. Modelo | Aspecto general del panel | A, B o C según la misión |
| 2. Distribución | Posición y etiquetas de los controles dentro del modelo | «Respaldo de sensor» está arriba a la izquierda en una partida y abajo en otra |
| 3. Estado | Un control queda inutilizable por un fallo | La palanca de empuje fino falla; hay que usar la alternativa |

La **lógica de la nave no cambia**; solo cambia la interfaz. Objetivo de aprendizaje: distinguir la función (qué hay que lograr) de la interfaz (dónde se acciona), y usar procedimientos y confirmaciones en lugar de memoria.

**Vínculo con el hangar (pilar 1):** el tipo de panel puede ser un módulo elegible. Un panel digital ofrece más funciones pero depende de energía; uno analógico es más robusto pero con menos opciones. La elección afecta qué puzzles aparecen y qué fallos son posibles. *Por decidir si entra en el MVP.*

**Consecuencias observables:** acción en el control equivocado (equipo apagado por error, etapa sin separar), tiempo perdido, o procedimiento correcto que recupera margen.

### 9.2 Incidencias de despegue paso a paso

**Idea:** durante el ascenso ocurre una incidencia. El astronauta la reporta, la torre diagnostica y le **va dictando el procedimiento un paso a la vez**; el astronauta ejecuta y reporta el resultado antes del siguiente paso. El camino depende de lo que reporta cada uno.

**Flujo de una incidencia:**

| Etapa | Qué ocurre | Quién |
|---|---|---|
| 1. Señal | Alarma, vibración o cambio visible (pista detectable) | Astronauta |
| 2. Reporte | Describe qué ve: alarma, valores, luces, sensación de la nave | Astronauta |
| 3. Diagnóstico | Cruza el reporte con telemetría y manual; puede pedir más lecturas | Torre |
| 4. Procedimiento | Dicta un paso; el astronauta ejecuta y confirma; la torre elige el siguiente según el resultado | Ambos |
| 5. Verificación | Ambos comprueban que la variable vuelve a su banda | Ambos |
| 6. Consecuencia | Se registra el efecto en recursos y objetivos | Simulación |

**Qué ve cada uno:**

- El astronauta ve síntomas locales (luz parpadeando, aguja, vibración, estado del control).
- La torre ve tendencias, historial y límites (lo que el astronauta no puede ver) y tiene el árbol de decisión.
- Algunas decisiones requieren un dato de cada lado: sin ambos, se actúa a ciegas.

**Incidencias candidatas para despegue (nombres y valores de juego):**

| Incidencia | Aprendizaje | Lo que aporta el astronauta | Lo que aporta la torre | Pasos de ejemplo | Consecuencia si falla |
|---|---|---|---|---|---|
| Sensores de orientación discrepan | Diagnóstico con evidencia | Dos indicadores que no coinciden; sensación de la nave | Historial y cuál suele derivar | Leer ambos, comparar con trayectoria, conmutar al respaldo, verificar | Trayectoria desviada, más combustible de corrección |
| Bus eléctrico en sobrecarga | Consumo y priorización | Equipos activos | Tabla de consumo y límite | Listar equipos, apagar los no críticos en orden, comprobar balance | Batería menor para la fase orbital |
| Temperatura de motor en ascenso | Límites térmicos y empuje | Temperatura local y alarma | Límite y tiempo de enfriamiento | Reducir empuje dentro de la banda, esperar, verificar | Pérdida de etapa o menos velocidad lateral |
| Separación de etapa que no confirma | Secuencias y condiciones | Estado de luces y tapas | Condiciones previas del procedimiento | Revisar condiciones, repetir secuencia en orden, confirmar | Masa extra en órbita, objetivos reducidos |

**Ejemplo de diálogo (panel B, sensores discrepantes):**

> **Astronauta:** Alarma de orientación. El indicador izquierdo marca 12° de inclinación y el derecho 4°.
> **Torre:** Recibido. Telemetría indica que vas en 5°. Describe tu panel: ¿cuántas zonas tiene la pantalla central?
> **Astronauta:** Tres zonas, botones abajo.
> **Torre:** Eso es el modelo B. Paso 1: abre el menú «Sensores» con el segundo botón de abajo.
> **Astronauta:** Confirmo: menú «Sensores» abierto. Aparecen dos entradas, SENS-1 y SENS-2.
> **Torre:** Paso 2: el izquierdo es SENS-1. Marca SENS-1 como «dudoso» y selecciona SENS-2.
> **Astronauta:** Confirmo: SENS-1 dudoso, SENS-2 activo. Ahora marcan 5° y 4°.
> **Torre:** Correcto. Paso 3: verifica que el empuje siga en la banda.

**Reglas de diseño:**

- Los pasos se dictan de **uno en uno** y cada uno exige confirmación (read-back) antes de avanzar.
- El procedimiento **ramifica**: el resultado reportado decide el paso siguiente; no hay un guion único que se pueda memorizar.
- Un paso equivocado tiene **consecuencia recuperable** en niveles iniciales y más severa en los avanzados.
- Hay un **reloj de fase** visible (la incidencia debe resolverse antes de cierto punto del ascenso), de modo que la presión sea el tiempo y no la confusión de reglas.
- Los pasos se generan desde **plantillas con parámetros** (qué sensor falla, qué botón, qué valor), para que cada partida difiera.

### 9.3 Cómo se evita que el puzzle sea un guion

- La torre no recibe todo escrito: tiene un **manual por modelo** y debe buscar, filtrar y elegir según lo que reporta el astronauta.
- El astronauta debe decidir **qué describir** y cuándo: lo irrelevante estorba, lo omitido confunde.
- Algunos datos solo están en el panel; otros solo en la telemetría.
- Las plantillas, el modelo de panel y la distribución cambian entre partidas.
- La comunicación se mide: ¿hubo confirmación?, ¿hubo ambigüedad?, ¿cuántos pasos se repitieron?

### 9.4 Escalado de dificultad

| Nivel | Paneles | Incidencias de despegue |
|---|---|---|
| 1 | Un solo modelo, conocido de antemano | Una incidencia de 2–3 pasos con ayuda visible |
| 2 | Modelo desconocido que debe identificarse | Una incidencia de 4–5 pasos con una ramificación |
| 3 | Modelo + distribución cambiada | Dos incidencias, una con control inutilizable |
| 4 | Fallo parcial de panel durante la misión | Incidencias encadenadas con ventana de comunicación limitada |

### 9.5 Funciones necesarias para implementarlo (Propuesta)

- **Definición de paneles basada en datos:** cada modelo lista sus controles, posición y etiqueta; las funciones de la nave se mapean a controles distintos según el modelo.
- **Catálogo de modelos** visible para la torre (siluetas, rasgos, preguntas discriminantes).
- **Manuales por modelo** con búsqueda o índice, accesibles solo para la torre.
- **Plantillas de incidencia:** síntoma, variable afectada, pasos, ramas, parámetros, consecuencia.
- **Validador de pasos en el anfitrión:** comprueba la acción real del astronauta, avanza o ramifica y registra errores.
- **Registro de eventos** de la partida (reporte, confirmaciones, errores, tiempos) para el informe causal.
- **Reloj de fase** y banda objetivo mostrados a ambos con distinta información.
- **Semilla de partida** para repetir exactamente un escenario y comparar diseños.

### 9.6 Cómo probarlo

| Pregunta | Señal de éxito |
|---|---|
| ¿La torre identifica el modelo sin ver el panel? | Acierta con 2–3 preguntas |
| ¿Se confunden dos modelos parecidos? | Ocurre a veces y se corrige hablando |
| ¿El astronauta describe con precisión? | Cada vez menos ambigüedad con la práctica |
| ¿Hay un guion memorizable? | No: cambian modelo, distribución y plantilla |
| ¿Entienden por qué el procedimiento funcionó o falló? | Pueden explicarlo en el informe |

### 9.7 Catálogo base de puzzles (fase orbital y generales)

| Puzzle | Aprendizaje | Astronauta aporta | Torre aporta | Consecuencia observable |
|---|---|---|---|---|
| Batería descendiendo | Generación, almacenamiento y consumo | Equipos activos y carga restante | Próximo eclipse y consumo previsto | Se apagan equipos o se pierde un objetivo |
| Sensores discrepantes | Diagnóstico con evidencia | Lecturas locales y comportamiento | Historial y procedimiento | Se identifica el sensor poco fiable o se actúa con datos falsos |
| Antena sin enlace | Geometría de comunicación | Orientación y estado del mecanismo | Posición de estación y ventana | Se reorienta, espera o usa respaldo |
| Trayectoria desviada | Trayectoria y combustible | Orientación, empuje, combustible | Corrección necesaria y margen | Se gasta combustible o se acepta órbita menos útil |
| Instrumento caliente | Límites térmicos | Temperatura y alarmas | Límites y tiempo de enfriamiento | Se interrumpe la captura o se daña el equipo |

Ejemplo de tensión: quedan 40 s de observación; la cámara puede completar un objetivo opcional, pero la batería baja y se acerca un eclipse. ¿Conservar energía para transmitir lo ya obtenido o intentar conseguir más? No hay respuesta universal: depende del diseño.

Diferenciar de la referencia: el principio de «uno ve, el otro tiene el manual» es el mismo que el del juego citado, así que la diferencia debe estar en lo demás: los puzzles se derivan de operaciones de nave, dependen de las decisiones del hangar, dejan consecuencias persistentes en recursos y objetivos, y terminan en un informe causal. No copiar mecánicas, textos ni recursos del juego de referencia.

## 10. Eventos inesperados pero justos

Cada evento necesita tres elementos: **pista detectable, tiempo razonable para actuar, consecuencia comprensible**.

- Consumo elevado → batería se agota antes.
- Mala orientación → menor producción solar.
- Corrección imprecisa → consume reservas.
- Componente con respaldo → permite recuperarse de un fallo.
- Observación extra → puede costar una ventana de transmisión.

Incertidumbre externa permitida, siempre con señales previas. La dificultad sube con menos margen, no con fallos imposibles.

## 11. Simulación

Dos modalidades:

- **Ensayo previo:** prueba el diseño y devuelve informe («La batería no cubre el eclipse con todos los instrumentos encendidos»). El ensayo básico es gratuito para favorecer el aprendizaje.
- **Misión en vivo:** la simulación avanza mientras ambos operan; calcula trayectoria, combustible, electricidad, temperatura y datos científicos.

Relaciones mínimas coherentes:

- Más tiempo de instrumentos → más consumo y más datos.
- Más datos → más almacenamiento y tiempo de transmisión.
- Más correcciones → menos combustible.
- Menos margen → menor capacidad de responder a incidentes.

Tiempo acelerado en tramos largos, con parada antes de maniobras, eclipses o incidencias. La demora de comunicación en misiones lejanas se representa con instrucciones enviadas por adelantado.

## 12. Resultados y retroalimentación

| Resultado | Condición de ejemplo |
|---|---|
| Éxito completo | Tripulación segura y todos los objetivos principales cumplidos |
| Éxito parcial | Tripulación segura y parte de los objetivos |
| Aborto seguro | Misión cancelada para proteger a la tripulación |
| Fracaso | Se pierde la nave o no se logra el objetivo mínimo |

El informe separa seguridad, objetivos científicos y uso de recursos, e incluye:

- Una **cadena causal** («La cámara avanzada elevó el consumo; en el eclipse tuvieron que apagarla para conservar energía de comunicaciones»).
- Sugerencias con su costo («batería mayor: más masa; capturas más cortas: menos datos»).
- **Línea de tiempo** decisión → cambio de recursos → consecuencia.
- **Repetición del mismo escenario** con las mismas condiciones para comparar diseños.

## 13. Interfaz por rol (3D)

- **Astronauta:** cabina 3D en primera persona con botones, palancas, pantallas y vista exterior.
- **Torre:** estación con mapas, telemetría, procedimientos y planificación; puede tener entorno 3D sencillo, con la interacción principal en pantallas.
- Pantallas distintas para cada jugador, sin compartir la vista completa.
- Accesibilidad por considerar: textos legibles, no depender solo del color, subtítulos si hay voz, opciones de dificultad.

## 14. Funciones por prioridad

**Núcleo de prueba (MVP propuesto)**

- Dos jugadores, dos PC por Internet, pantallas distintas.
- Una misión de observación terrestre.
- Dos lanzadores y unas diez opciones de módulos.
- Construcción → ensayo → despegue → fase orbital → cierre.
- Tres problemas: energía, orientación y comunicación.
- Dos modelos de panel (identificación por descripción) y dos incidencias de despegue guiadas paso a paso (ver sección 9).
- Informe causal final.

**Después del MVP**

- Más misiones (Marte y asteroide con sonda).
- Repetición de escenarios y comparación de diseños.
- Niveles con dificultad creciente.
- Tercer rol o cuatro jugadores.
- Más puzzles y eventos.
- Modo para aula (guía didáctica, resumen para el docente) si el público lo requiere.

**Fuera de alcance por ahora**

- Física de alta fidelidad.
- Soporte vital de larga duración, radiación, retorno a la Tierra.
- Personajes de IA dentro del juego (no solicitado).

## 15. Arquitectura técnica propuesta

Unity y C# son la elección planteada por el usuario; véase [plan-unity.md](plan-unity.md). Lo siguiente es propuesta:

- Una aplicación con dos vistas según el rol.
- **Anfitrión autoritativo:** una instancia calcula el estado oficial (combustible, trayectoria, electricidad, temperatura, fallos); la otra envía acciones y recibe solo los datos de su rol. Así no hay dos simulaciones distintas.
- Modelo de datos separado para módulos, misiones y eventos, de modo que añadir contenido no requiera reescribir la lógica.
- Reglas de órbita, consumo y propulsión implementadas por el equipo; el motor aporta renderizado, entrada y red.
- Candidatos de red, modelado y versionado (Netcode for GameObjects, Blender, Git con archivos grandes) pendientes de confirmar en el plan.

## 16. Validación y métricas

La prueba decisiva del prototipo: ¿ambos jugadores tienen información útil, toman decisiones relevantes y entienden por qué ocurrió el resultado?

Preguntas para sesiones de prueba:

- ¿Algún jugador queda sin nada que hacer?
- ¿Las instrucciones ambiguas causan errores frecuentes?
- ¿El jugador puede explicar la causa del resultado final?
- ¿Cambiar el diseño en el hangar cambia de verdad lo que ocurre en vuelo?
- ¿Cuánto tarda una partida y dónde se pierde el ritmo?

## 17. Riesgos

| Riesgo | Mitigación propuesta |
|---|---|
| Alcance demasiado grande | Empezar con una misión y tres problemas |
| Un rol aburrido | Dar acciones propias a la torre; probar pronto |
| Sincronización en red | Anfitrión autoritativo; prototipo en red local primero |
| Realismo mal sustentado | Marcar unidades de juego; citar fuentes para cualquier afirmación real |
| Confusión con la referencia | Puzzles propios, derivados de operaciones de nave |
| 3D consume tiempo | Cabina y torre mínimas; trayectoria en plano |

---

## Relación entre el prototipo y el desafío

Un prototipo concentrado en puzzles durante el lanzamiento permite probar la cooperación, pero no demuestra por sí solo diseño, gestión y operación de una misión completa.

Propuesta para conectar ambos: preparación breve con componentes bajo límites; ejecución cooperativa donde esas elecciones afectan recursos y opciones; evaluación que explica las consecuencias. El alcance exacto y la cobertura del desafío deben acordarse antes de declarar cumplimiento.

## Temas de investigación pendientes (de S3)

Para cada línea, registrar fuente verificable antes de usarla en el juego:

1. Dificultades de los astronautas.
2. Problemas matemáticos o físicos relevantes.
3. Herramientas de desarrollo.
4. Diseño de naves.
5. Instrumentos científicos.
6. Restricciones orbitales.

## Límites provisionales para futuros agentes

- No presentar ideas o ejemplos de este documento como funcionalidades aprobadas o existentes.
- No asumir número definitivo de jugadores, voz integrada, grado de 3D ni física de alta fidelidad. Motor, lenguaje y modalidad de conexión siguen lo indicado en la actualización del usuario.
- Toda afirmación de realismo exige una fuente técnica verificable. Registrar las simplificaciones educativas y evitar presentar parámetros inventados como valores reales.
- Vincular cada puzzle a un objetivo de aprendizaje, una necesidad de cooperación y una consecuencia observable.
- Evaluar nuevas funciones según su contribución al concepto; documentar ampliaciones de alcance como propuestas.
- Los agentes ayudan al equipo de desarrollo; no se ha pedido incorporar personajes de IA al juego.

## Decisiones abiertas

1. Dos roles o tres; distribución de información y acciones.
2. Primer entregable centrado en lanzamiento o ciclo simplificado completo.
3. Público objetivo, dificultad y duración de partida (el borrador S4 menciona 25–40 min en la versión completa y 20–25 min en el prototipo; sin acordar).
4. Alcance del 3D, plataforma y detalles de conexión remota.
5. Significado de comunicación limitada: turnos, ventanas temporales, vocabulario, información incompleta u otro mecanismo; voz integrada o externa.
6. Recursos, criterios de éxito y nivel de fidelidad científica.
7. Cuántos modelos de panel entran en el MVP (2 o 3) y si el panel es un módulo elegible en el hangar.
8. Reto oficial, calendario, repositorio del videojuego y responsables humanos. El repositorio de agentes ya fue indicado por el usuario: `AESRJ/Agentes_Space_Ship`.

No es necesario resolver todo para discutir el concepto; sí resolver las decisiones que condicionan cada implementación antes de empezarla.
