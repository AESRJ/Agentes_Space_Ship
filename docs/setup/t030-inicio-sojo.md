# Inicio técnico de T030 — Sojo

Actualización de coordinación de Jorge, 2026-11-15, tras recibir el reporte de incorporación de Sojo. Resuelve la consulta sobre T026 → T019 sin reescribir dependencias ni aprobar QA ajena.

## Decisión operativa

**Sojo puede comenzar T030 en `sojo/t030-dificultades`.** Las dependencias directas son T013 (lobby, #12) y T026 (regla de código, #26); ambas implementaciones ya están integradas y disponibles en main. La dependencia histórica de T026 respecto a T019 se conserva; su fusión no cambia la aceptación de esa validación.

Se distingue implementación disponible de aceptación del corte: **T019 continúa pendiente de Kevin**, incluida la incidencia del recorrido GUI documentada en el issue #23. Comenzar T030 no la acepta, no cierra el issue y no sustituye sus pruebas. Antes de aceptar el prototipo o declarar una cadena de QA cerrada se debe resolver esa evidencia pendiente. No se borra ni falsea ese seguimiento.

La liberación se limita a configurar y probar dificultades sobre los componentes existentes. T035 espera sus dependencias; T039 sigue siendo de Gael con apoyo técnico de Sojo.

## Cuenta y entorno

- Cuenta confirmada por Jorge: **Sojito312**, ID GitHub `226743142`.
- Coordinación comprobó mediante la API que tiene **write** en AESRJ/Agentes_Space_Ship y AESRJ/LaunchControlGodot. No necesita nuevas invitaciones.
- Sojo reporta dos clones, Godot4.7.2 instalado, comprobador aprobado, harness21/21 e integración43/43. No se presenta ese reporte como una ejecución independiente de coordinación en su PC.
- Falta su prueba visual de dos instancias alternando el rol del host. Puede iniciar T030 y debe conservar ese pendiente, completar el smoke visual y registrar los resultados de su entrega.
- El correo de commits comunicado por Sojo se configura localmente en sus clones y sesión; no se añade al registro público de integrantes ni se usa para atribuirle los commits de coordinación de Jorge.

## Alcance

1. Leer las APIs de SessionService, RoundController y ServerClock y la regla de código de Kevin. Conservar autoridad del host, permisos por rol, deadline y resultado inmutable.
2. Configurar fácil = `[antenna]` y normal = `[antenna, code]`, con recursos y registro de reglas coherentes. No permitir cambiar dificultad durante la ronda.
3. Normal no debe ganar con un solo módulo; los inactivos no cuentan para completar. No asumir que una escena ya publicada implica que la configuración de dificultad la activa.
4. Probar ambas dificultades y ambos roles de host, error/reintento, vencimiento, intentos inválidos y las regresiones existentes. Mantener la duración acordada como propuesta si no hay decisión que la fije.
5. No editar `scenes/main.*` ni el harness GUI que está integrando Jorge/Claude en T024; coordinar si cambia una API pública. No implementar T031 de Jorge ni T035 en este PR.
6. Commit `[sojo] ...`, trailers Team-Member: sojo y AI-Assisted: true; PR revisable con revisión, pruebas y límites. Sojo no fusiona ni marca T019 aceptada en este encargo.

## Actualizar y empezar

Conserva tus cambios locales. En el clon de agentes, después de integrar PR #10, actualiza main sin forzar y consulta `team/members.json`, ADR-0005, assignments/status/index y esta página. Inicia o reanuda tu sesión con tu identidad y correo propios según `docs/team-workflow.md`.

En el clon del juego, con árbol limpio:

```sh
git switch main
git pull --ff-only
git switch -c sojo/t030-dificultades
```

Si ya creaste esa rama, reutilízala sin borrarla ni forzar su historial; incorpora main de forma ordinaria. Las escenas del rediseño #32 y la UI de código/calculadora #33 ya están integradas. La composición final de T024 se revisa por separado y no es una dependencia directa de T030.

Mensaje para su IA:

> Soy Sojo, cuenta Sojito312. El inicio técnico de T030 está liberado por coordinación con T013/T026 integradas. Lee esta decisión y las APIs reales; trabaja solo dificultades en mi rama. Conserva T019 pendiente de Kevin, T035 para después y T039 de Gael. No cambies la composición de T024 ni quites aserciones para obtener CI verde. Entrega un PR con pruebas y límites reales.
