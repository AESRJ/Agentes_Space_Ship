# Launch Control

Especificación inicial para trabajar con IA mediante desarrollo guiado por especificaciones (SDD).

## Objetivo de la ronda

Dos jugadores preparan una nave para el despegue antes de que termine una cuenta regresiva compartida. El juego se inspira en *Keep Talking and Nobody Explodes*. El astronauta describe el panel y manipula los controles. El operador de torre consulta el manual y le explica cómo resolver cada acertijo.

## Roles

| Aspecto | Astronauta | Torre de control |
| --- | --- | --- |
| Perspectiva | Primera persona desde la cabina. Por la ventana ve el cielo. | Primera persona desde una oficina con una laptop sobre el escritorio. Por la ventana ve el cohete en la plataforma. |
| Información | Ve los símbolos, luces y controles activos en el panel de la nave. | Abre el manual y las herramientas en la laptop. Puede consultar el tiempo restante mientras trabaja. |
| Acción | Describe lo que observa y opera el panel siguiendo las instrucciones del compañero. | Pregunta por el estado del componente, busca la regla correspondiente y guía al astronauta. |

## Primera versión jugable

1. Los jugadores eligen sus roles y el nivel de dificultad.
2. Al iniciar la ronda, ambos ven la misma cuenta regresiva. Los niveles fáciles tienen menos componentes activos y los difíciles tienen más.
3. Cada componente activo contiene un acertijo interactivo y tiene una sección correspondiente en el manual.
4. Si el astronauta resuelve todos los componentes a tiempo, el cohete despega.
5. Si el contador llega a cero con algún componente pendiente, el despegue falla y se reproduce una explosión cómica. Como propuesta visual, la punta del cohete sale disparada como un corcho y cae con un paracaídas diminuto.

## Cabina y panel del astronauta

Desde su asiento, el astronauta tiene el cuadro de instrumentos al alcance y ve el cielo por el parabrisas. La distribución y la apariencia del panel se ajustarán a las imágenes de referencia cuando estén disponibles. Cada componente activo presenta una pista que el astronauta puede describir, un control que puede manipular y una señal que indica si lo resolvió.

## Laptop interactiva de la torre

Desde su escritorio, el operador puede mirar el cohete por la ventana o interactuar con la laptop. Al abrirla encuentra un índice del manual con una sección por componente. Cada sección indica qué debe preguntarle al astronauta, cómo interpretar su respuesta y qué instrucción darle. El contador permanece visible al cambiar de sección o usar una herramienta.

Cuando un acertijo requiera una herramienta, su sección del manual debe permitir abrirla. Por ejemplo, si se incorpora un módulo de radio con señales codificadas, la laptop podría incluir una tabla de equivalencias. El operador buscaría la señal descrita por el astronauta y le comunicaría el ajuste correspondiente. Para el acertijo inicial de la antena basta la tabla del manual.

### Criterios de aceptación de la ronda

- [ ] Desde la cabina se ven el panel y el cielo. Desde la oficina se ven la laptop y el cohete en la plataforma.
- [ ] Una dificultad mayor activa más componentes que una menor. La ronda exige resolver todos los componentes activos.
- [ ] Cada componente activo tiene controles que responden al astronauta y una sección localizable en el índice de la laptop.
- [ ] El operador puede abrir una sección, consultar la herramienta necesaria y regresar al manual mientras sigue visible la cuenta regresiva compartida.
- [ ] Resolver el último componente antes de cero activa el despegue. Llegar a cero con alguno pendiente activa la animación cómica de explosión.

## Primera funcionalidad propuesta · Alineación de antena

**Objetivo:** comprobar que dos personas pueden resolver un componente comunicando lo que ven desde sus respectivos puestos.

En la cabina hay una luz fija o parpadeante, un selector con los símbolos de luna y estrella y un botón **Confirmar**. El astronauta describe la luz. El operador consulta esta sección del manual y le da la instrucción correspondiente.

| Estado observado en la cabina | Instrucción del manual |
| --- | --- |
| Luz fija | Selecciona la luna y pulsa **Confirmar**. |
| Luz parpadeante | Selecciona la estrella y pulsa **Confirmar**. |

### Criterios de aceptación

- [ ] Si la luz está fija y el astronauta confirma la luna a tiempo, el componente muestra **Listo**.
- [ ] Si la luz parpadea y el astronauta confirma la estrella a tiempo, el componente muestra **Listo**.
- [ ] Una selección incorrecta deja el componente pendiente y permite otro intento mientras quede tiempo.
- [ ] Si la antena es el último componente pendiente, resolverla a tiempo activa el despegue.
- [ ] Si el contador llega a cero con la antena pendiente, se activa la animación de fallo y ambos jugadores ven el mismo resultado.

## Primer mensaje para trabajar con IA

> Usa esta especificación para preparar una primera ronda jugable con el astronauta, el operador de torre y el acertijo de la antena. Antes de programar, revisa si el manual permite resolver todos los estados del componente. Muéstrame qué ve y qué hace cada jugador en una ronda exitosa y en una que termina por tiempo. Señala las decisiones que necesito tomar y convierte la funcionalidad en tareas pequeñas que pueda probar en orden. Espera mi revisión antes de generar código.

## Detalles pendientes

- Definir cómo se comunicarán los jugadores.
- Definir la cantidad de componentes por nivel y la duración de la cuenta regresiva.
- Incorporar las imágenes de referencia para definir la apariencia del panel.

La antena y el paracaídas son propuestas para el prototipo.

