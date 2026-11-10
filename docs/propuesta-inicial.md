# Propuesta de agentes y memoria compartida

Fecha: 2026-11-10. Estado: propuesta para discusión; no constituye alcance aprobado del juego.

## Contexto confirmado y pendiente

El equipo tiene seis personas. Se busca colaborar mediante GitHub con agentes de investigación, implementación, diseño y pruebas, mantener memoria recurrente y conservar la correspondencia entre diseño de niveles e integración del juego.

El tablero asociado es https://miro.com/app/board/uXjVEWUr6N4=/ del equipo «UABC Team». La lectura directa falló, pero posteriormente el usuario aportó dos capturas, el texto del desafío y una explicación del concepto. Esa información está registrada en [docs/vision.md](vision.md), distinguiendo ideas, propuestas y decisiones abiertas. El concepto actual plantea cooperación entre astronauta y torre de control mediante puzzles durante el lanzamiento. El desafío aportado abarca además diseño y gestión de una misión completa; falta acordar cómo cubrirlo. Motor, plataforma, repositorio remoto y número definitivo de jugadores siguen pendientes.

## Arquitectura propuesta

GitHub contendrá la versión acordada de instrucciones, especificaciones, código, decisiones y evidencias. Miro será el espacio de exploración visual. Una idea del tablero pasa a ser requisito cuando se documenta su aceptación, su responsable y su referencia al elemento de Miro. No se presupone sincronización automática entre ambos.

Cada persona trabajará con su propia cuenta, copia del repositorio y sesión del asistente. Compartirán definiciones y memoria versionada; los chats y los agentes en ejecución no se comparten automáticamente al clonar. Las credenciales y autorizaciones de MCP se configuran individualmente, fuera de Git.

| Rol | Trabajo | Entregable y límite |
| --- | --- | --- |
| Coordinación y alcance | Leer estado, descomponer tareas y seleccionar especialistas | Encargo con requisito, archivos, dependencias y aceptación; no aprobar ampliaciones de alcance |
| Investigación | Verificar fuentes científicas, datos y documentación del motor | Hallazgos con fuente, fecha, incertidumbres y repercusión; no convertir hipótesis en requisitos |
| Diseño | Definir experiencia, niveles, interfaz y criterios jugables | Fichas de nivel y contratos de integración ligados a requisitos |
| Implementación | Construir mecánicas e integrar escenas y recursos | Cambio limitado al encargo, evidencias y documentación actualizada |
| Pruebas | Revisar comportamiento, regresiones e integración | Casos, resultado real, versión probada y defectos reproducibles |
| Integración y memoria | Comprobar coherencia entre diseño, código y documentación | Revisión de discrepancias y actualización propuesta del estado compartido |

Los seis roles son reutilizables por cualquier integrante. No requieren seis agentes activos en cada tarea. La revisión humana de alcance y de integración permanece en el equipo. Se paralelizan investigaciones o revisiones independientes; se secuencian trabajos dependientes y se evita editar simultáneamente una misma escena.

## Organización sugerida del repositorio

```text
AGENTS.md                        Reglas comunes y mapa de lectura
.codex/agents/                   Definiciones de agentes para Codex
.agents/skills/                  Procedimientos reutilizables, si hacen falta
docs/vision.md                   Objetivo, público y experiencia central
docs/scope.md                    MVP, exclusiones y criterios de aceptación
docs/state.md                    Estado integrado y enlaces a evidencias
docs/architecture.md             Motor, versiones y contratos técnicos
docs/decisions/                  Decisiones aceptadas, motivos y sustituciones
docs/research/                   Fuentes y hallazgos verificables
docs/levels/                     Una ficha por nivel
docs/handoffs/                   Un registro por tarea y punto de control
docs/traceability.md             Requisito → diseño → cambio → prueba
.github/                        Plantillas, responsables y validaciones
```

Los nombres de `docs/` son convenciones propuestas: se deben enlazar expresamente desde las instrucciones. AGENTS.md debe ser breve y dirigir al contexto relevante, sin cargar todo el historial en cada tarea.

## Memoria recurrente

1. Al iniciar: identificar rama y revisión base, leer alcance y estado integrado, localizar ficha y decisiones aplicables, y revisar el código real. Registrar discrepancias antes de continuar con trabajo que dependa de ellas.
2. Tras un hito, decisión o bloqueo: guardar un registro por tarea con responsable, requisito, rama/revisión base, cambios, evidencias, pendientes y próximo paso. Guardar antes de cambiar de tarea o cerrar una sesión; no depender únicamente del resumen del chat.
3. Antes del pull request: actualizar diseño y registro junto al código. Separar resultados comprobados, propuestas y pruebas pendientes. Las actualizaciones locales todavía no son memoria compartida hasta publicarse en la rama remota.
4. Al integrar: consolidar el estado aceptado mediante el flujo de revisión y vincular el PR. No describir trabajo de una rama como ya integrado. Los registros por tarea reducen conflictos frente a un único diario editado por seis personas.
5. Semanalmente: revisar documentación obsoleta y enlaces rotos, marcar decisiones sustituidas y archivar registros antiguos conservando sus referencias. La frecuencia puede ajustarse al ritmo del equipo.

Cada hecho debe enlazar una fuente, archivo, PR o resultado verificable. Un test no ejecutado se marca «pendiente», nunca «aprobado». Si falta información, se declara como desconocida. Estas medidas reducen errores y permiten detectarlos; no garantizan eliminar alucinaciones.

## Contrato de cada nivel

Para este proyecto, cada nivel deberá vincular sus puzzles con la [plantilla de puzzle](puzzles/TEMPLATE.md). Investigación aporta fuentes y simplificaciones; diseño establece la información y acciones de cada rol; implementación conecta los resultados con el estado de misión; pruebas comprueba tanto cooperación como consecuencias. Integración y memoria revisa que los cuatro entregables correspondan a la misma versión.

Cada ficha incluirá: identificador estable; estado de diseño/implementación/validación; objetivo del jugador; requisito asociado; objetivo educativo si aplica; mecánicas permitidas; entrada y salida; victoria y derrota; recursos; escenas y scripts; eventos y datos intercambiados con otros sistemas; criterios de aceptación; pruebas y versión probada; referencia al diseño en Miro.

Ejemplo de trazabilidad, exclusivamente ilustrativo: `REQ-001 → LVL-001 → escena correspondiente → PR → caso de prueba`. El contenido concreto depende del tablero y del motor elegido.

## Colaboración y control de alcance

- Una tarea tiene responsable humano, requisito, entregable y criterio de aceptación. Cada integrante usa una rama propia por tarea.
- La rama principal se protege con revisión y comprobaciones requeridas, según las capacidades del repositorio. Designar responsables de diseño y de integración.
- Las escenas o recursos difíciles de fusionar tienen un único editor por tarea; evaluar Git LFS y bloqueos cuando se conozcan el motor y los formatos.
- Una mecánica o dependencia que amplíe el alcance se documenta como propuesta. Los agentes continúan el trabajo autorizado independiente y no la incorporan silenciosamente.
- Las validaciones automáticas comprueban estructura, referencias, compilación y pruebas disponibles. La revisión humana evalúa fidelidad a la idea y calidad jugable; un archivo de instrucciones por sí solo no impone esos controles.
- No integrar un cambio de nivel sin su ficha actualizada, contrato de integración revisado y evidencia de pruebas pertinentes, incluidas pruebas manuales en el motor cuando correspondan.

## Instrucción común propuesta

> Antes de actuar, identifica el requisito aprobado, el estado real de la rama y las decisiones aplicables. Implementa dentro del alcance de la tarea. Verifica fuentes y APIs; distingue hechos, hipótesis y propuestas. Mantén sincronizados diseño, código y pruebas. Guarda puntos de control verificables y deja un traspaso al terminar. Reporta lo que no pudiste comprobar. Si aparece una contradicción que afecta al resultado, señala las fuentes y solicita resolverla; continúa las partes independientes.

## Puesta en marcha

El contexto inicial ya se extrajo de los materiales aportados; véase [estado actual](state.md). El siguiente paso es delimitar el primer recorrido jugable, los roles y un puzzle representativo. Después adaptar las instrucciones y agentes al motor y repositorio reales. Validar el flujo con una tarea pequeña que atraviese diseño, implementación y pruebas. Finalmente incorporar a las seis personas con una guía de instalación, acceso, lectura de contexto y apertura de PR. Automatizar controles cuando el flujo piloto funcione.

No se han instalado ni activado agentes, creado repositorios remotos o configurado automatizaciones. Este documento conserva la propuesta y sus límites actuales.

## Referencias técnicas consultadas

- Instrucciones de proyecto en Codex: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Definiciones de subagentes: https://learn.chatgpt.com/docs/agent-configuration/subagents
- Reglas, skills y flujos de revisión en repositorio: https://developers.openai.com/blog/skills-agents-sdk
