# ADR-0006 — Prueba final de red en LAN

Fecha: 2026-11-15. Aprobado explícitamente por Jorge en la conversación de coordinación: «Aceptar LAN como criterio final y autorizar el cambio del PR #54».

## Decisión

Para este prototipo, FR-020/SC-005 y T039 se demuestran con dos PC físicos en la misma LAN. Se sustituye el requisito de dos redes externas por Internet; la conectividad entre redes externas queda fuera de la aceptación de esta entrega. No se afirma que el juego ya fue probado en LAN.

Se conservan las cinco rondas con éxito, vencimiento y error recuperado, la desconexión adicional con resultado interrumpido, ambos equipos identificados y las métricas de reloj/rendimiento. Loopback en una sola PC no satisface T039. Gael conserva T039 y Sojo su apoyo; no cambian los 42 IDs. T038 precede a T039 y T040 consolida la evidencia real.

Evidencia: propuesta de Kevin AESRJ/LaunchControlGodot#54; fusionada tras la aprobación en `3b849fef7c9d91864b2dc6a54c0d4b231d4d0b46`, CI Linux/Windows aprobado. Esta decisión sustituye las menciones anteriores de Internet como criterio obligatorio de este prototipo. No altera la duración ni las reglas de módulos.
