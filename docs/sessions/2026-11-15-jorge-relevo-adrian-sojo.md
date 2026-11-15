# Registro 2026-11-15-jorge-relevo-adrian-sojo

Fecha UTC: 2026-11-15T17:57:36+00:00
Integrante: jorge
Contexto Git al guardar: {"base_commit": "9a75d7e46f4e03dcdcc637613ccf72cfa1170451", "branch": "jorge/relevo-adrian-sojo", "working_tree_dirty": true}

Tipo: decision
Estado del contenido: verificado

## Resumen
Jorge decidió que Sojo releve a Adrian: Sojo pasa a activo y asume T007, T008, T009, T011, T013, T017, T030 y T035, además del apoyo técnico en T039. Adrian queda inactivo, conserva su autoría e historial, y no se revocan permisos. Claude implementó el relevo en agentes y en el juego; Codex revisa. No se implementan T030 ni T035.

## Evidencia
- ADR-0005.
- `team/members.json`: Sojo `active` (GitHub pendiente), Adrian `inactive`.
- `scripts/team_session.py` admite `inactive`; solo `active` inicia sesiones o firma commits.
- Pruebas con registro de ejemplo explícito: inactivo válido, sesión inactiva rechazada (también en `check`), sesión de Sojo activa y el caso `pending` conservado. 27 pruebas OK y `validate.py` OK.
- Una mutación (quitar `inactive`) provoca 11 errores.
- Juego en main `11d649b`, CI 43743111583 con 43/43 y 21/21 en Linux y Windows. Entregas reflejadas: #16, #17, #24 (T019 sin aceptar), #25, #26, #27, #28, #31 y #34.
- La línea base de T030 se comprobó en `autoload/round_controller.gd`: `RULE_SCRIPTS` solo con antena y `difficulty_modules` solo con easy.

## Siguientes pasos
- Recibir la cuenta GitHub y el sistema operativo de Sojo; después, invitarlo a ambos repositorios y comprobar su acceso.
- Sojo sigue `docs/setup/sojo.md` y empieza T030.
- T035 después de T030.
- T019 sigue pendiente de aceptación por Kevin.
