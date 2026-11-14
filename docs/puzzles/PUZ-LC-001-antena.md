# PUZ-LC-001 — Alineación de antena

Estado: especificación para el prototipo solicitado; sin implementación ni prueba de jugadores.

## Encargo y fundamento

- Fuente: `specs/001-launch-control-godot/references/Etapa_1_final.md`, sección de antena; requisitos FR-005/FR-006.
- Fase: preparación antes del despegue de Launch Control.
- Responsable inicial: Kevin (regla); Gael (vista); Isra (manual); revisión de aceptación: Sojo. Es reparto, no revisión ya realizada.
- Objetivo de aprendizaje: describir una observación, consultar una regla y coordinar una acción con información repartida.
- Problema real: no se afirma reproducir alineación física de antenas. Luz y símbolos son una simplificación lúdica; no se requieren ni inventan parámetros NASA.

## Cooperación

| Rol | Información | Acción | Necesita del otro |
| --- | --- | --- | --- |
| Astronauta | Luz fija o parpadeante; selección actual | Elegir luna/estrella y confirmar | Correspondencia del manual |
| Torre | Tabla fija→luna, parpadeante→estrella | Consultar y comunicar | Estado observado en cabina |

La interfaz no revela manual al astronauta ni pista viva a torre. No se promete impedir que alguien memorice la regla.

## Reglas y consecuencias

Al crear ronda, antena activa y pendiente; luz fija o parpadeante, selección vacía. Respuesta correcta es luna para fija y estrella para parpadeante. Error conserva pendiente y permite reintento sin tiempo extra de penalización. Acierto a tiempo deja Listo; si es el último pendiente, host decide éxito. Tiempo vencido falla; exactamente al límite prevalece vencimiento. Sin unidades físicas: luz y símbolo son categorías.

## Integración

Regla y vista previstas en GAME/scripts/modules/antenna_rule.gd y GAME/scenes/modules/antenna_view.tscn. Contratos en `specs/001-launch-control-godot/contracts/`. Host valida intención y emite estado; vista no decide victoria. Eventos incluyen round_id/command_id; duplicados y respuestas antiguas no repiten resultado. Desconexión interrumpe; nueva ronda limpia selección y estado.

## Verificación

Q01–Q05 y T014–T019 cubren dos aciertos, error/reintento, vencimiento, permisos y desconexión. Probar ambas ubicaciones del host. Impacto sobre la misión: éxito solo con todos los módulos activos resueltos. Pruebas de juego y evidencia: pendientes. No se ha realizado sesión de comprensión con jugadores.
