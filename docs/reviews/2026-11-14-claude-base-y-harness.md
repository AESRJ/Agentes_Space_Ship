# Revisión de entregas Claude — base y harness T003

Fecha: 2026-11-14. Revisor: Codex por encargo de Jorge. Los resultados corresponden a las revisiones indicadas, no a futuras correcciones.

## Base publicada

[PR #1](https://github.com/AESRJ/LaunchControlGodot/pull/1) fusionado con squash en `0ec8b6ac0fffa864f7549dd95f871efa96a12d58`. Se revisaron proyecto/escena vacía, instaladores, comprobadores y guía de arranque. Comprobación independiente en Linux con Godot estándar 4.7.2: importación y check_project OK, salida 0. CI de la cabecera fusionada [43646971560](https://github.com/AESRJ/LaunchControlGodot/actions/runs/43646971560) aprobado en Linux y Windows.

El juego dispone de proyecto base y guía `docs/setup/team-readiness.md`. Esto permite iniciar trabajo a los cinco activos con acceso; no demuestra gameplay, red, rendimiento real ni apertura GUI en el Windows personal de Jorge.

## Entrega T003 revisada

[PR #2](https://github.com/AESRJ/LaunchControlGodot/pull/2), cabecera `105a1e7d37aa0dc8dd0184ee57c3fc5d1c30113b`, abierto y fusionable al consultar. CI [43648219159](https://github.com/AESRJ/LaunchControlGodot/actions/runs/43648219159) en verde para Linux y Windows. Añade harness de escena aislada, fixtures, puesto simulado explícitamente rotulado, hooks opcionales y registro/captura/métricas. No se confunde el stub con la cabina o torre de Gael.

## Hallazgos reproducidos independientemente

| ID | Severidad | Caso | Resultado observado | Corrección requerida |
| --- | --- | --- | --- | --- |
| R1 | Alta | `--record` apunta a un directorio existente | No se guarda JSON, pero exit=0, ok=true y se anuncia registro guardado | Propagar fallo de persistencia a errores y salida; no afirmar escritura inexistente |
| R2 | Media | `--frames=abc` | Se convierte a modo interactivo y agota timeout independiente de 6 s | Validar enteros/rangos; inválidos deben salir con error sin esperar al wrapper |
| R3 | Media | Stub válido en headless | viewport 64×64, target 1280×720, size_matches_target=true y tasa ~1900 FPS | Separar carga funcional de medición visual; headless no acredita resolución ni SC-006 |

Caso positivo astronaut: exit=0 y fixture aplicado; rol inválido: exit=1. Estos aciertos no cubren los fallos de persistencia/argumentos. Evidencia local detallada: `ProyectoNaS` comparte el informe temporal `/tmp/codex-harness-review-yqtrx79p/review-results.json`; la tabla conserva en Git los datos útiles sin logs personales completos.

## Instrucciones y límites

Se entrega a Claude un encargo de corrección R1–R3, regresiones portables y publicación en el mismo PR #2, con CI de la nueva cabecera. Las integraciones posteriores de Jorge continúan sujetas a los componentes de los otros dueños. Sojo no está incorporado y sus tareas ya se redistribuyen según ADR-0004.

Claude informó que su clasificador de permisos denegó la fusión del PR #2; no comunicó una causa más específica que esa denegación. No se reintenta por otro canal ni se cambia de identidad o permisos para eludirla. El PR queda además pendiente de corregir estos hallazgos y de la vía de aprobación permitida. La base ya publicada permite a los demás comenzar mientras se resuelve T003.
