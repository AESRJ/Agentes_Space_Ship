# ADR-0002: identidad por nombre y atribución del trabajo

Fecha: 2026-11-14. Estado: aceptado por Jorge en esta conversación.

## Decisión y autorización

Jorge proporcionó los nombres Gael, Adrian, Kevin, Isra y Jorge; después confirmó «Mi nombre es jorge esta es mi cuenta y el otro integrante se llama sojo» y pidió publicar los cambios, documentarlos en Git y NotebookLM y que identificarse por nombre fuera el primer paso. La API de GitHub confirmó que la cuenta conectada es `AESRJ`.

Los seis IDs son `gael`, `adrian`, `kevin`, `isra`, `jorge` y `sojo`. El registro canónico es `team/members.json`. Solo está confirmado el vínculo Jorge ↔ AESRJ; las otras cuentas se incorporarán cuando sus titulares las proporcionen.

## Aplicación

- Al iniciar cada conversación, la persona dice su nombre o la IA lo pregunta antes de actuar o consultar memoria. Una identidad guardada en disco no basta para confirmar quién está presente. Si ya se identificó en la conversación, no se repite la pregunta.
- Una sesión local contiene integrante, tarea y rama. El correo Git se conserva localmente y se usa para la autoría de commits; no se añade al registro compartido del equipo ni al checkpoint.
- Los commits creados con `team_session.py commit` llevan `[id]`, `Team-Member` y `AI-Assisted`. El workflow de PR comprueba etiquetas, sin afirmar verificación de identidad criptográfica.
- Los nuevos checkpoints incluyen el integrante declarado de la sesión. Los registros anteriores quedan intactos y no se atribuyen retrospectivamente.
- Git conserva decisiones y evidencia versionada; NotebookLM recibe checkpoints e instantáneas con revisión Git. Los recibos `synced` con `source_id` acreditan sincronización; un archivo local por sí solo no la acredita.

## Límites

No concede permisos ni verifica a los otros cinco usuarios en GitHub o Google. No cambia reglas remotas de aprobación. El método de tareas pequeñas con IA está documentado como recomendación en `docs/team-workflow.md`. No cambia las decisiones del videojuego ni sustituye otras decisiones del equipo.
