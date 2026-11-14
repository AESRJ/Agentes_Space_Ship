# ADR-0003 — Planificar Launch Control en Godot con Spec Kit

Fecha: 2026-11-14. Autor del encargo: Jorge (`AESRJ`).

## Decisión explícita

Jorge pide leer `Etapa_1_final.md`, usar las imágenes aportadas, ignorar la metodología del documento y utilizar Spec Kit para asignar tareas a los seis integrantes con el objetivo de lograr el prototipo en Godot. Después confirma que no hay preferencias de especialidad y solicita un reparto inicial equilibrado.

Para este prototipo, Godot sustituye la planificación anterior de Unity/C#. `docs/plan-unity.md` se conserva como antecedente histórico, no como stack vigente. La etapa se centra en Launch Control: astronauta y torre, panel/manual, cuenta regresiva, antena y despegue o fallo. No presupone ya el prototipo orbital descrito en planes anteriores.

## Implementación documental

Se aplican las skills `speckit-specify`, `speckit-plan` y `speckit-tasks`, usando sus resolutores y scripts de preparación. Se crea `specs/001-launch-control-godot/` con fuentes preservadas, especificación, investigación, modelo, contratos, validación y 42 tareas: siete por Gael, Adrian, Kevin, Isra, Jorge y Sojo. La investigación técnica independiente se delegó conforme a la skill de planificación; una sola persona escribió los artefactos.

## Propuestas diferenciadas

Versión Godot 4.7.2, GDScript, cámara fija, ENet con host autoritativo, voz externa, 180 segundos, fácil con antena y normal con antena más un módulo numérico propio son propuestas para concretar el trabajo. No se afirma que el equipo ya las haya probado o que cada integrante haya aprobado su responsabilidad individual. Los nombres se distribuyen según el encargo, sin inventar experiencia.

## Límites

Este encargo produce planificación y reparto. El destino del código se identifica en T001; no se crea ni implementa el juego dentro del repositorio de agentes. La constitución instalada sigue siendo una plantilla. No se configuran servicios, voz, cuentas, permisos ni issues; no se declara satisfecha la red por Internet sin prueba entre redes distintas.

Las capturas son referencias aportadas, no assets que se empaquetan en el juego. La regla de antena es una simplificación lúdica de comunicación, no un modelo científico de orientación de antenas.
