# Estado del proyecto

Actualizado: 2026-11-14.

## Prototipo local autorizado posteriormente

Mejora solicitada de comprensión: tutorial de lanzamiento con una orden de torre por paso, respuesta sugerida y control concreto para astronauta. Pausas automáticas para leer, desactivables. Compilación y pruebas de guía/pausas/recorrido completo aprobadas; interfaz inicial, avance y recuperación de error revisados visualmente. Evidencia en [sesión de tutorial](sessions/2026-11-10-tutorial-torre.md). Trabajo local en `prototype/launch-tutorial`.

Ampliación solicitada después: despegue 3D con comprobaciones, banda de inclinación y separación cooperativa. Escena `Launch.unity` y [PUZ-002](puzzles/PUZ-002-despegue-local.md), implementados en el proyecto local; compilación Windows y comprobaciones automáticas aprobadas. Revisión visual de despegue y aborto por tiempo realizada; [evidencia y límites](sessions/2026-11-10-despegue-verificado.md). Documentación en rama `prototype/launch-puzzles`, sin integrar. Sigue siendo local en una pantalla; no hay conexión por Internet implementada.

El usuario solicita crear un proyecto Unity local para probar. Se prepara `../OrbitaPrototype` con Unity 6000.6.8f1, escena de dos paneles locales y reglas de energía/captura/transmisión. Esta petición amplía el encargo anterior de planificación. La conexión por Internet sigue pendiente y el proyecto no tiene repositorio remoto asignado. Ver [PUZ-001](puzzles/PUZ-001-energia-local.md). La verificación se registra en la sesión de prototipo; las afirmaciones siguientes de no implementación describen la entrega anterior.

## Nueva planificación

El usuario elige Unity y C# y dos PC conectados por Internet. Se preparó [un plan por hitos](plan-unity.md), pendiente de implementación y validación. Estas decisiones sustituyen las afirmaciones históricas siguientes sobre motor y conexión abiertos. El repositorio del juego todavía no está acordado. Próximo paso propuesto: conexión remota y prototipo orbital breve antes de la misión completa.

## Dirección

Proyecto en exploración: cooperación astronauta/torre de control, puzzles durante el lanzamiento y aprendizaje sobre decisiones de misión. No hay motor, MVP o arquitectura del videojuego aprobados. Ver [visión](vision.md) y [alcance](scope.md).

## Infraestructura de trabajo

Repositorio destino autorizado: `AESRJ/Agentes_Space_Ship`. Se creó el cuaderno [Space Ship — Memoria de creación](https://notebooklm.google.com/notebook/62c97db5-1c82-41bd-a443-2f1f98675ada).

Se publicaron seis perfiles Codex, instrucciones comunes, skill de memoria, adaptador MCP basado en knowingdoing, instalador PowerShell, pruebas de herramientas y exportador de contexto. Se verificaron consultas y escritura de checkpoints reales por MCP. La primera ejecución CI pasó en Linux y Windows. Véase [evidencia y límites](verification.md) y los registros de `docs/sessions/`; la presencia de un script no demuestra el login interactivo en todos los equipos.

## Pendientes del equipo

- Identidad del equipo en `team/members.json`: Gael, Adrian, Kevin, Isra, Jorge y Sojo. Jorge confirmó su cuenta `AESRJ`. El primer paso de cada conversación es identificarse por nombre. Herramienta de sesión/commits etiquetados, atribución automática en checkpoints y flujo con IA documentados en `docs/team-workflow.md`. Implementado e integrado mediante [PR #3](https://github.com/AESRJ/Agentes_Space_Ship/pull/3), con atribución y CI Linux/Windows aprobados. Decisión sincronizada en NotebookLM (fuente `ece98b4e-ce5e-45bf-99eb-d991adeec8a6`); evidencias en `docs/sessions/2026-11-14-jorge-identidad-equipo.md` y el registro de publicación. Faltan las otras cinco cuentas GitHub; no se modificaron reglas remotas.
- Se recibió la identidad de un compañero: invitación GitHub creada con escritura y acceso NotebookLM concedido como editor. Falta aceptar la invitación GitHub y probar su incorporación. Recibir las identidades restantes para completar los accesos del equipo; los permisos se consultan en los servicios, sin duplicar correos personales en los documentos.
- Ejecutar la incorporación interactiva en un equipo Windows y confirmar login/permisos.
- Acordar roles jugables, primer recorrido, público y modalidad de conexión.
- Investigar un fenómeno y definir un primer puzzle con fuentes.
- Identificar la edición y URL oficial del reto para verificar criterios.
- Elegir después el repositorio del videojuego y registrar el traspaso.

## Distinciones

Las ideas iniciales están preservadas en [visión](vision.md); la [propuesta inicial](propuesta-inicial.md) es histórica y sus frases de «todavía no instalado» describen ese momento anterior. Las decisiones aceptadas se registran en `docs/decisions/`. No se implementó el videojuego en esta entrega.
