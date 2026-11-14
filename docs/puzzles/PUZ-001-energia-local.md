# PUZ-001 — Capturar y transmitir antes del eclipse

Estado: especificación del prototipo local autorizado por el usuario; parámetros de juego.

## Encargo y fundamento

- Primera prueba local de observación terrestre; responsable humano y revisor pendientes.
- Aprendizaje: distinguir generación, consumo y almacenamiento; conservar energía para entregar datos.
- Fuente consultada 2026-11-10: https://science.nasa.gov/learn/basics-of-space-flight/chapter11-3/ explica recarga solar y uso de batería al quedar paneles en sombra o fuera de orientación.
- Simplificación: duración 90 segundos, batería 100 unidades, paneles 3 unidades/s, base 0.5, cámara 2, transmisor 2. No representan una nave real, ni física orbital.

## Cooperación

| Rol | Información disponible | Acciones permitidas | Información que necesita del otro |
| --- | --- | --- | --- |
| Astronauta | Batería, equipos, datos locales | Apuntar Sol/objetivo/Tierra y activar cámara | Eclipse y ventana de enlace |
| Torre | Pronóstico temporal, entregas y ventana | Autorizar transmisión | Confirmación de orientación y batería |

En esta prueba ambos paneles comparten pantalla para depuración. No demuestra todavía separación de información ni cooperación remota.

## Reglas y consecuencias

- Eclipse entre segundos 35 y 60. Enlace disponible de 20 a 80.
- Orientar al Sol genera energía fuera del eclipse; al objetivo permite capturar 2 datos/s; a Tierra permite transmitir 4 datos/s si torre autoriza enlace.
- Almacén limitado a 100; éxito al entregar 40; parcial con alguna entrega; sin entregas, objetivo no logrado. Batería cero termina la sesión. Aborto manual conserva lo entregado.
- Cámara consume aunque apunte mal. Un transmisor activo consume aunque no haya enlace. Son decisiones deliberadas de este modelo didáctico.
- Pistas: panel de pronóstico, balance eléctrico y estado de enlace. Se puede apagar cámara, cerrar transmisión y reorientar para recuperar energía.
- Pausa y reinicio disponibles. Resultado muestra captura, entrega, energía consumida/generada y registro de acciones.

## Integración

- Proyecto hermano `../OrbitaPrototype`, escena `Assets/Scenes/Orbita.unity`.
- `Mission` posee estado y reglas; `OrbitaDemo` presenta controles y avanza pasos máximos de 0.05 segundos.
- Comandos locales de orientación/cámara/transmisión, sin eventos de red. Cierre único bloquea siguientes pasos. Reinicio crea una misión nueva.
- Sin dependencias de otros puzzles; sincronización y recuperación remotas pendientes.

## Verificación

- Autocomprobación en editor: solución, agotamiento, límites, exclusión de orientación y fin de misión.
- Ejecución y resultados se registrarán en el documento de sesión.
- Prueba con dos jugadores, reparto privado de información y conexiones: pendiente.
