# ADR-0001: agentes compartidos y memoria NotebookLM

Estado: aceptada en cuanto a herramientas y repositorios por el usuario, 2026-11-10.
Evidencia: solicitud de montar agentes en git@github.com:AESRJ/Agentes_Space_Ship.git, preparar Windows y usar knowingdoing/notebooklm-codex.

Separamos el repositorio de trabajo conceptual del futuro repositorio del juego. Git registra documentos y cambios; NotebookLM permite consultar y recuperar memoria usando fuentes versionadas. Cada persona mantiene autenticación propia.

Detalles técnicos de esta implementación: cuaderno fijado por UUID, checkpoints por evento, reintento idempotente por hash/título, instantáneas con estado Git, adaptador MCP local y configuración de Codex por proyecto. Estos son mecanismos de implementación, no ampliaciones del diseño del juego.

Consecuencia: acceso a GitHub no otorga acceso a Google. El propietario deberá compartir el cuaderno con los integrantes identificados. No se publican credenciales. Si NotebookLM falla, permanece una copia recuperable en Git y se reporta sincronización pendiente.
