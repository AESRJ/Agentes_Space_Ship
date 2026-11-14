# Registro 2026-11-14-gael-campana-unity

Fecha: 2026-11-14
Integrante: gael
Proyecto afectado: `../OrbitaPrototype` (Unity 6000.6.8f1, local, sin repositorio Git ni remoto)

Tipo: avance
Estado del contenido: implementado y verificado con pruebas automáticas; jugabilidad manual pendiente

## Resumen

Gael pidió ampliar el prototipo Unity siguiendo `docs/vision.md` y `docs/plan-unity.md`, con prioridad en funcionalidades y en que el juego sea divertido y dinámico, sin invertir en diseño visual. Codex implementó el código coordinado mediante Orca y Claude auditó cada entrega sin modificar código. Hubo 3 rondas de corrección.

Ciclo jugable implementado en una sola escena (`Assets/Scenes/Campaign.unity`), con el ejecutable empezando por el menú:

- **Misión:** «Observación terrestre» en dos dificultades (Aprendiz y Operador), con semilla repetible. Objetivo principal: entregar datos de tres regiones (Costa, Cordillera y Bosque). Opcionales: terminar con al menos 30 % de batería y usar alta resolución.
- **Hangar:** 2 lanzadores y 12 módulos en 6 ranuras (cámara, paneles, batería, antena, reserva de maniobra, protección). Cada módulo tiene costo, masa, consumo o generación y efecto real en la simulación. Los límites de presupuesto y de masa bloquean las configuraciones inválidas. Se muestran el balance eléctrico y la autonomía.
- **Ensayo:** gratuito; usa el mismo núcleo y avisa de déficits previsibles (por ejemplo, la batería no cubre el eclipse con la cámara activa).
- **Despegue 3D:** reutiliza la presentación anterior (nave, llama, separación de etapa y cámara de seguimiento). La masa de la nave afecta al empuje efectivo. Hay dos modelos de panel: A analógico (acción directa) y B digital (seleccionar y confirmar). La distribución de los controles cambia según la semilla.
- **Incidencias guiadas:** sensores discrepantes, bus sobrecargado e instrumento caliente.
  - El astronauta solo ve lecturas en bruto y controles con códigos.
  - Solo la torre tiene el manual que relaciona lectura con control.
  - En la incidencia de sensores, una lectura a mitad del procedimiento decide entre confirmar o conmutar al respaldo.
  - Cada incidencia tiene pista previa, plazo visible y read-back.
  - Los errores dejan consecuencias que se arrastran (menos capacidad de batería, combustible y puntos).
- **Órbita:** eclipses, orientación (Sol, objetivo o Tierra), ventanas de captura por región, almacenamiento, ventanas de enlace y antena simple o direccional. Durante una incidencia orbital los controles de órbita siguen disponibles.
- **Informe:** cuatro resultados posibles (éxito completo, éxito parcial, aborto seguro o fracaso). Incluye puntuación y estrellas, mejor marca local, una cadena causal resumida a partir de eventos reales, una sugerencia según la causa dominante con su costo, el registro completo opcional y los botones «Repetir misma semilla» y «Volver al hangar».

Arquitectura: el núcleo C# (`Assets/Scripts/Core/`) no depende de Unity y funciona por comandos que lleva cada rol. Rechaza los comandos del rol incorrecto y ofrece vistas separadas para astronauta y torre, como preparación para la red futura. No se implementó red.

## Evidencia

- La compilación Unity en batchmode (`CampaignSetup.Build`) terminó con código 0. El log `OrbitaPrototype/Logs/campaign-code-only-final.log` contiene 10 marcadores: `ORBITA`, `TUTORIAL`, `LAUNCH`, `AUTHORITY_HANGAR`, `REHEARSAL_DETERMINISM`, `INCIDENT`, `AUDIT_ROUND1`, `AUDIT_ROUND2` y `CAMPAIGN_OUTCOMES` (todos `_CHECKS_PASSED`), más `CAMPAIGN_BUILD_PASSED`.
- Las comprobaciones dotnet (`Assets/Validation~/RunChecks.ps1`) terminaron con código 0, según el reporte de Codex.
- Las comprobaciones automáticas cubren:
  - el rechazo por rol y los límites de presupuesto y masa;
  - el determinismo por semilla y la detección de déficit en el ensayo;
  - ambas ramas de cada incidencia y la persistencia de daños en la órbita;
  - la necesidad de la torre para elegir el control correcto;
  - los cuatro resultados, la dificultad Operador y el registro de controles acotado.
- Hallazgos de la auditoría corregidos:
  - se había perdido el despegue 3D;
  - el astronauta podía resolver las incidencias sin la torre;
  - el procedimiento no tenía ramificación real;
  - el informe salía ilegible y la sugerencia era fija;
  - los paneles A y B se operaban igual;
  - los controles orbitales desaparecían durante las incidencias;
  - se perdían ajustes de control en el registro;
  - había artefactos de compilación dentro de `Assets`.
- Los valores son unidades de juego y la trayectoria es arcade. No son datos ni procedimientos NASA.

## Límites y pendientes

- **Jugabilidad manual:** pendiente de prueba por Gael. Incluye separación, órbita, incidencias en pantalla, ritmo, diversión, resoluciones y persistencia del récord. No se probó con dos personas.
- **Código fuera de Git:** `OrbitaPrototype` no tiene repositorio Git; la copia de referencia previa a los cambios solo existe localmente. El repositorio del juego sigue sin acordar.
- **Red y voz:** sin conexión por Internet ni voz. Ambos roles comparten la pantalla.
- **Observaciones menores no corregidas:** en el hangar todas las elecciones quedan registradas como de la torre, y resolver el bus sobrecargado no deja consecuencia posterior.
- **Pendiente de este repositorio:** no se actualizó `docs/state.md` con esta sesión ni se registró el checkpoint en NotebookLM.
