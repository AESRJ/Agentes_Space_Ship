# Estado del proyecto

Actualizado: 2026-11-14.

## Actualización — T003 fusionada por petición de Jorge

Jorge pidió explícitamente que Codex hiciera la fusión del PR #2. GitHub confirma MERGED en `3cf3de79f9dd360013a4ed8fa41a27a81e6b7482`, cabecera `11bab3a`, CI Linux/Windows 43652062713 aprobado. Se usó squash, revisión fijada y trailers de Jorge, sin bypass ni cambio de permisos. Esta actualización sustituye el estado anterior de cambios solicitados/fusión pendiente de T003; las secciones de revisión conservan la evidencia histórica de la cabecera 105a1e7. No acredita pruebas de puestos reales o gameplay. Ver `docs/sessions/2026-11-14-jorge-fusion-t003-autorizada.md`.

## Equipo y destino vigentes

Activos: Jorge (`AESRJ`), Gael (`GaelFlores04`), Adrian (`adrianbalderas373488`), Kevin (`KVSO755`) e Isra (`issgg`). Escritura efectiva comprobada en el juego privado https://github.com/AESRJ/LaunchControlGodot. No hay invitaciones pendientes al consultar. Sojo no está incorporado por instrucción de Jorge, figura pending y no tiene tareas activas.

El reparto mantiene 42 IDs: Jorge 9, Gael 9, Adrian 8, Kevin 8 e Isra 8. Sus antiguas tareas de Sojo se redistribuyeron sin eliminar QA. Ver [ADR-0004](decisions/0004-cinco-activos-y-arranque.md), [reparto](../specs/001-launch-control-godot/assignments.md) y [estado operativo](../specs/001-launch-control-godot/status.md).

## Base publicada y tareas liberadas

Claude integró PR #1 del juego con squash en `0ec8b6ac0fffa864f7549dd95f871efa96a12d58`. La base Godot 4.7.2 incluye proyecto/escena vacía, instaladores Linux/Windows con SHA-512, comprobadores, CI y guía `docs/setup/team-readiness.md`. Codex revisó los archivos y ejecutó el check Linux: importación, escena y configuración OK, salida 0. CI Linux/Windows de la cabecera fusionada aprobado en run 43646971560.

La base técnica y los permisos permiten iniciar Gael T004, Adrian T007, Kevin T005 e Isra T006. Jorge tiene T003 en revisión. Prueba GUI en el Windows personal de Jorge y comprobación en cada PC siguen pendientes; no se presentan como hechos ni bloquean el inicio de quienes ya tienen acceso. T001/T002 conservan sus criterios de aceptación y se distinguen del estado técnico publicado.

## Última revisión de Claude

T003 añade harness, fixtures, un puesto simulado, captura y registro de métricas. Está en PR #2, cabecera revisada `105a1e7`, con CI aprobado. Codex reprodujo tres problemas y pidió corrección: registro no escrito devuelve éxito, frames inválido queda interactivo y headless con viewport 64×64 marca resolución 1280×720 como válida. [Informe de revisión](reviews/2026-11-14-claude-base-y-harness.md).

Claude recibió el encargo de corregir R1–R3 y publicar nuevas regresiones en ese PR. La fusión anterior del PR #2 fue denegada por su clasificador de permisos; no se elude por otra vía. Las integraciones posteriores de Jorge esperan tareas reales de los compañeros; nadie implementa trabajo ajeno para cerrar su lista.

## Plan y memoria

El plan vigente es Launch Control en Godot con Spec Kit, a partir de Etapa_1_final y tres imágenes. Antena primero; segundo módulo numérico/calculadora y 180 s son propuestas. No hay una ronda jugable, red entre dos PC ni rendimiento real del juego verificado. Unity y los repartos anteriores se conservan como historia.

Repositorio de agentes: AESRJ/Agentes_Space_Ship. Cuaderno fijado: 62c97db5-1c82-41bd-a443-2f1f98675ada. La URL real del juego y las cinco cuentas están en memory/notebook.json y team/members.json. Los checkpoints y sus recibos distinguen contenido local de revisión integrada; no se afirma sincronización solo por escribir un documento.

## Pendientes

- Correcciones y revisión nueva de T003; resolver la vía de aprobación de su fusión sin bypass.
- Integrantes clonan main, ejecutan su comprobador y empiezan su primera tarea liberada.
- Validar futuras entregas antes de T012/T018/T024/T031/T038/T040.
- Confirmar público, parámetros de dificultad, fuentes de puzzles futuros y edición/criterios del reto.
- Probar GUI Windows personal y, cuando exista la ronda, dos redes externas y métricas con puestos reales.
