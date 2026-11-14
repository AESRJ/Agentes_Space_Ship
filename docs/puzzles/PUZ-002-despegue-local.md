# PUZ-002 — Encendido, trayectoria y separación

Estado: diseño e implementación de prototipo local solicitados por el usuario; revisión humana y prueba con jugadores pendientes.

## Encargo y fundamento

Implementar primero despegue y puzzles para probar diversión. Tres retos de un único procedimiento de lanzamiento; objetivo educativo: confirmar pasos, interpretar trayectoria y comprender separación de etapas y componente lateral.

Fuente consultada 2026-11-10: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/flight-to-orbit/ describe lanzamiento de dos etapas, separación y giro hacia el horizonte. Los circuitos, orden, ángulos, tiempos, combustible e integridad son mecánicas ficticias, no procedimientos NASA. Altura y velocidad lateral son indicadores arcade; no prueban órbita física. Responsable humano/revisor pendientes.

## Cooperación

| Rol | Información disponible | Acciones permitidas | Información que necesita del otro |
| --- | --- | --- | --- |
| Astronauta | Circuitos, inclinación, empuje, combustible e integridad | Confirmar, orientar, cortar empuje, separar | Orden de pasos, banda de trayectoria, armado |
| Torre | Procedimiento, banda objetivo, tiempo disponible | Autorizar lanzamiento y armar separación | Confirmaciones y ejecución física |

Ambos paneles están en la misma pantalla para la prueba local. Se distribuyen acciones pero no se impide a una persona operar ambos; privacidad y cooperación entre dos equipos pendientes.

## Reglas y consecuencias

Actualización solicitada: tutorial activado por defecto. La torre recibe una orden corta para leer y una respuesta sugerida; astronauta ve el control que debe usar. La guía avanza según comprobaciones, fase, ángulo objetivo y subpaso de separación. Cada instrucción nueva detiene el tiempo sin bloquear controles. Continuar vuelo reanuda; desactivar pausas mantiene mensajes sin detener el tiempo. La pausa manual sigue separada. No se verifica voz ni se simula confirmación humana automática.

1. En plataforma: confirmar ENERGIA → GUIA → COMBUSTIBLE, después torre autoriza. Error reinicia comprobación; encendido prematuro se bloquea. Cuenta atrás 5 s. No se consumen reservas en plataforma.
2. Ascenso: banda ±8 grados de 0/15/30 grados, cambia a los 6/12 segundos equivalentes de empuje. Fuera de banda se pierde integridad a 2.5/s. Combustible consume 1.5 por segundo a máximo empuje. Empuje cero puede recuperarse, pero vuelo tiene límite 160 s. El esquema permite reaccionar varios segundos sin perder la misión inmediatamente.
3. A los 18 segundos equivalentes de empuje: ventana de separación 25 s. Torre arma; astronauta corta a ≤5% y libera. Interbloqueo impide separar sin cumplir condiciones. Se muestra la etapa desprendida. En segunda etapa objetivo 60 grados; al acumular 38 segundos equivalentes, se requieren ≥26 en banda y ≥42 unidades laterales. Si falta margen, aborto con causa.

Los indicadores de altura y velocidad lateral aumentan según componentes trigonométricas del empuje. No incluyen gravedad, arrastre ni trayectoria orbital: representación didáctica arcade. No existe caída física durante separación.

Éxito habilita observación orbital PUZ-001. Aborto o pérdida de integridad permiten reiniciar. Pausa congela simulación. Resultado conserva secuencia y causa; no implica seguridad real de una tripulación. Repetición usa mismas condiciones.

## Integración

`LaunchGuidance.cs` deriva textos del estado real y gestiona las pausas locales del tutorial. Las reglas de la misión permanecen en LaunchMission. Tutorial no implica red, reconocimiento de voz ni validación con jugadores. Etiquetas actuales: Apagar motor, Encender motor al 85%, Habilitar separación, Separar etapa 1.

Proyecto `../OrbitaPrototype`, escena `Assets/Scenes/Launch.unity`. `LaunchMission.cs` concentra estado y comandos; `LaunchDemo.cs` presenta y construye nave/entorno 3D con primitivas; `Editor/LaunchSetup.cs` comprueba y compila. `Mission.cs` y escena orbital se conservan. Cierre bloquea nuevos comandos; transición orbital se ejecuta una sola vez por botón. Red, reconexión y voces pendientes.

## Verificación

Autocomprobaciones previstas: orden incorrecto, encendido temprano, interbloqueo de separación, vuelo completo, cierre idempotente, ventana perdida, desviación y empuje cero. Regresión de seis comprobaciones orbitales. Evidencia real en registro de sesión al terminar compilación. Pruebas con dos jugadores y diversión: pendientes.
