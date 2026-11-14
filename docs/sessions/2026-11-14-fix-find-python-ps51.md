# Sesión: detección de Python en Windows PowerShell 5.1

Fecha: 2026-11-14. Integrante: kevin. Rama de trabajo: `kevin/fix-find-python-ps51`. Trabajo sin integrar en main.

Tipo: corrección de herramienta. Estado del contenido: implementado y verificado localmente.

## Resumen

En un equipo Windows 11 con Windows PowerShell 5.1 y Python 3.13 instalado (lanzador `py`), `Setup-Windows.ps1` sin `.venv` previo informaba `Missing dependency Python.Python.3.12`. Causa: en `Find-Python`, la expresión `if` desenvolvía `@('-3')` a una cadena y el splatting previo a los argumentos literales perdía `-c`; `py` iniciaba un intérprete interactivo, escribía su banner en stderr y, con `ErrorActionPreference = 'Stop'`, el candidato se descartaba. Se construye ahora un único arreglo explícito de argumentos.

Sustituye al PR #2 (rama `fix/find-python-ps51`), cuyo commit no llevaba la etiqueta de integrante exigida desde el PR #3.

## Evidencia

- Antes: la función extraída del script rechazaba `py` (excepción con el banner de Python 3.13.6).
- Después: la función extraída de `Setup-Windows.ps1` devuelve `py`; la rama `python` con un intérprete real devuelve código 0; el script se analiza sin errores con el parser de PowerShell.
- `scripts/validate.py` OK y pruebas unitarias OK; CI del PR #2 pasó en Ubuntu y Windows con el mismo cambio.
- Memoria: la versión anterior de este registro se sincronizó en NotebookLM (fuente `420ea24c-3b58-4c61-9e88-5466291d3637`).

## Límites y siguientes pasos

No se ejecutó el instalador completo desde cero (se conservó el `.venv` existente). CI valida solo la sintaxis PowerShell con `pwsh`, no este comportamiento de 5.1. Tras integrar, sincronizar esta versión con `memory_sync`.
