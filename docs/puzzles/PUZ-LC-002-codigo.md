# PUZ-LC-002 — Código numérico

Estado: ampliación propuesta para dificultad normal; sin implementación ni prueba de jugadores.

## Encargo y fundamento

- Fuente visual: `specs/001-launch-control-godot/references/Ejemplo_de_acetijo.png`; FR-011/FR-012. La tabla y textos son propios, no una transcripción del juego de referencia.
- Fase: preparación antes del despegue. Responsable inicial: Kevin (regla/vista); Isra (manual/calculadora); verificación: Sojo.
- Objetivo: traducir símbolos mediante una tabla, multiplicar dos números y comunicar un resultado inequívoco.
- No simula un cálculo de ingeniería de lanzamiento. La matemática es multiplicación entera ordinaria, sin datos físicos ficticios.

## Cooperación

| Rol | Información | Acción | Necesita del otro |
| --- | --- | --- | --- |
| Astronauta | Dos pares de letras de A/B/C/D | Dictar pares, introducir hasta cuatro dígitos y confirmar | Traducción y producto |
| Torre | Tabla A=2 B=5 C=7 D=9, instrucciones y calculadora | Traducir, multiplicar y dictar | Pares observados por astronauta |

## Reglas y consecuencias

Normal activa código y antena; fácil solo antena. Cada par concatena dos dígitos, no los suma. AB/CD representa 25 y 79: respuesta 1975. Mínimo AA/AA=22×22=484; máximo DD/DD=99×99=9801. Respuesta válida es entero entre esos extremos, hasta cuatro dígitos; vacío/decimal/fuera de rango se rechaza sin resolver. Valor incorrecto conserva pendiente y permite reintento a tiempo. Acierto deja Listo; el host solo declara éxito si todos los activos están resueltos antes de cero. No hay penalización extra propuesta.

## Integración

Previstos GAME/scripts/modules/code_rule.gd, GAME/scenes/modules/code_view.tscn y GAME/ui/manual/code_page.tscn; calculadora en GAME/ui/tools/calculator.tscn. Regla y manual comparten rule_version=1. El módulo solo emite intento, host valida rol/round_id/command_id/tiempo. La herramienta de torre no modifica RoundState. Reinicio limpia entrada/pista/resolución; desconexión interrumpe.

## Verificación

Q08–Q10 y T026–T032 verifican tabla, 1975, extremos, entradas inválidas, error/reintento, normal sin victoria tras un único acierto y navegación con reloj. Comprobar todos los pares generables frente a la misma tabla del manual. Pruebas ejecutadas del juego, comprensión de usuarios y evidencia: pendientes.
