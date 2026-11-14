# Despegue y puzzles locales

Solicitud del usuario: implementar primero despegue de nave y puzzles para hacerlo más divertido. Se implementó en `../OrbitaPrototype` con Unity 6000.6.8f1; documentación en `prototype/launch-puzzles`, sin subida ni integración nuevas.

Contenido: LaunchMission.cs, LaunchDemo.cs, Editor/LaunchSetup.cs, escena Launch.unity y PrototypeSurface.mat. Nave 3D procedural, plataforma, torre, llama, cámara de seguimiento, cuenta atrás, circuitos confirmados, bandas de inclinación, interbloqueos de separación, etapa desprendida y transición a observación orbital. Se conserva escena orbital anterior. Guía en README del proyecto local.

Evidencia: compilación Unity terminó con código 0, `LAUNCH_BUILD_PASSED`, `LAUNCH_CHECKS_PASSED` y `ORBITA_CHECKS_PASSED`. Pruebas cubren orden incorrecto, autorización prematura, separación insegura, vuelo completo, estado terminal, ventana perdida, desviación sin integridad y empuje cero; regresión de seis comprobaciones orbitales.

Inspección real del ejecutable: nave visible, tres confirmaciones, cuenta regresiva, ascenso con llama, inclinación con deslizador, entrada a separación, armado desde torre, corte de empuje, aborto al vencer margen de 25 s y reinicio a plataforma. La sesión manual no completó separación ni inserción; ese recorrido está probado en simulación automática, no en interacción manual completa. Se corrigió un shader omitido en la primera compilación mediante material referenciado en escena. Player.log de la ejecución corregida sin Exception/Error en la inspección posterior al despegue. Logs completos solo locales.

`git diff --check` sin errores. No se cambiaron herramientas del repositorio de agentes. Sin pruebas de red ni de diversión con dos personas. La consulta CLI de memoria falló al imprimir caracteres en consola; se contrastó documentación local y se preserva este registro para sincronización. No guardar logs completos en memoria.

Siguiente: usuario prueba ritmo/dificultad y se ajusta separación si hace falta; después se conecta la autoridad de simulación a dos clientes por Internet. Ciencia y simplificaciones en PUZ-002; parámetros arcade, sin afirmación de órbita físicamente simulada.
