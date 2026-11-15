# ADR-0005 — Relevo de Adrian por Sojo

Fecha: 2026-11-15. Decisión aceptada por Jorge (coordinador), comunicada a Codex y delegada a Claude para su implementación.

## Decisión

Jorge pide cambiar al integrante responsable: **todas las tareas de Adrian pasan a Sojo**, que se incorpora al equipo.

- **Sojo** (`sojo`) pasa a `active` y asume T007, T008, T009, T011, T013, T017, T030 y T035, además del apoyo técnico de Adrian en T039. El dueño de T039 sigue siendo Gael.
- **Adrian** (`adrian`) pasa a `inactive`: sin asignaciones vigentes. Conserva su historial, su cuenta conocida y la autoría de lo que implementó. No se revocan permisos de GitHub.
- Reparto: Jorge 9, Gael 9, Sojo 8, Kevin 8 e Isra 8. Se mantienen los 42 IDs y sus dependencias.

## Consecuencias

- T007, T008, T009, T011, T013 y T017 ya están integradas y las **implementó Adrian**. Los índices lo indican con `implemented_by: adrian` y `previous_owner: adrian`. Sojo hereda el mantenimiento, no el crédito retrospectivo, y no las reimplementa.
- La primera tarea de desarrollo de Sojo es **T030** (T013 y T026 están integradas). T035 espera T017 y T030.
- La herramienta `scripts/team_session.py` admite el estado `inactive`. Solo `active` puede iniciar sesiones o firmar commits nuevos; por eso las sesiones de Adrian se rechazan y las de Sojo se aceptan.
- La cuenta GitHub y el sistema operativo de Sojo están **pendientes**. Sin cuenta confirmada no se le invita ni se declara su acceso, y no se infiere su cuenta por el nombre.
- Sustituye, para el reparto vigente, la parte de ADR-0004 según la cual Sojo no estaba incorporado. ADR-0004 y los anteriores se conservan como historia.
- Guía de incorporación: `docs/setup/sojo.md`.

## Confirmación posterior — 2026-11-15

Jorge comunicó la cuenta **Sojito312**; coordinación comprobó escritura en los dos repositorios. Este dato sustituye el pendiente inicial de GitHub, conservado arriba como contexto de la decisión. Sojo reportó su entorno preparado; la prueba visual propia sigue pendiente. El inicio técnico de T030 sobre T013/T026 integradas se precisa en [t030-inicio-sojo.md](../setup/t030-inicio-sojo.md), sin aceptar T019 ni cambiar su responsable.
