# Tutorial y mensajes para la torre

Petición del usuario: hacer el despegue más fácil de entender, con tutorial y órdenes directas que torre pueda leer al astronauta.

Implementado en proyecto local `../OrbitaPrototype`: LaunchGuidance.cs deriva orden, acción, respuesta sugerida y explicación del estado de LaunchMission. LaunchTutorial pausa al cambiar de instrucción; controles siguen disponibles y Continuar vuelo reanuda. Modo libre conserva mensajes sin pausas automáticas. LaunchDemo presenta solo el paso actual, explica empuje/inclinación/etapa y usa etiquetas explícitas. Los mensajes de aborto distinguen integridad, combustible y tiempo. Se conserva historia de acciones en modelo. No existe reconocimiento de voz ni validación de confirmación hablada.

Verificado: Unity 6000.6.8f1 compiló Windows con retorno 0 y marcadores TUTORIAL_CHECKS_PASSED, LAUNCH_CHECKS_PASSED, ORBITA_CHECKS_PASSED y LAUNCH_BUILD_PASSED. Pruebas nuevas cubren orden actual, recuperación tras error, congelación del reloj, continuación, guía de separación en orden, recorrido completo y desactivación del tutorial. No se modificaron herramientas del repositorio de agentes.

Revisión visual del ejecutable a tamaño observado 1024×640 de contenido: textos y botones legibles sin recortes en preparación; confirmar energía cambia orden a guía; pulsar combustible fuera de orden explica volver a energía; reinicio deja tutorial abierto en primer paso. Sin revisión manual completa de todas las fases ni prueba con dos personas. No se atribuye una mejora medida de diversión o comprensión.

Documentación: PUZ-002 y README del proyecto local actualizados. Rama prototype/launch-tutorial, sin nueva publicación GitHub. Próximo paso: usuario prueba el tutorial; ajustar duración y mensajes según dificultades observadas. Internet y pantallas privadas pendientes.
