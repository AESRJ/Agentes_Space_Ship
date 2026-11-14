# Implementation Plan: Launch Control en Godot

**Branch**: `jorge/launch-control-godot` | **Date**: 2026-11-14 | **Spec**: [spec.md](spec.md)

## Summary

Jorge solicita Godot y Spec Kit, sustituyendo la planificación histórica de Unity para este prototipo. Se entrega especificación, diseño y tareas; no código de juego. Corte inicial: dos participantes, roles distintos, una antena, manual, reloj y resultado. Después: escenarios, dificultad con segundo módulo, calculadora y presentaciones de desenlace.

## Technical Context

- **Motor**: Godot, decisión de Jorge. Versión propuesta fijada para los seis: 4.7.2 stable; comprobar disponibilidad de binario y export templates en T002.
- **Language/Version**: propuesta GDScript tipado y edición estándar, no C# heredado del plan Unity.
- **Primary Dependencies**: componentes integrados de Godot: Node3D, Camera3D, Control, CanvasLayer, ENetMultiplayerPeer y API RPC. Sin plugins externos obligatorios.
- **Storage**: Resources locales para configuración, reglas y manual; sesión efímera en memoria. No base de datos.
- **Testing**: validaciones de casos de uso de quickstart.md, harness de escenarios y evidencia entre dos equipos; no se impone TDD ni un framework no solicitado.
- **Target Platform**: escritorio Windows para el equipo; Linux como entorno de desarrollo opcional. Exportaciones de ambos pares deben usar igual versión y contenido.
- **Project Type**: juego cooperativo 3D con UI 2D, dos puestos de cámara fija.
- **Performance Goals**: ≥30 FPS a 1280 × 720 en dos máquinas identificadas; diferencia visual de reloj ≤1 s en conexión estable de prueba.
- **Constraints**: host autoritativo, exactamente dos roles, una ronda, máximo dos módulos activos, voz externa. La ruta UDP de Internet debe probarse, no presumirse.
- **Scale/Scope**: fácil: antena; normal: antena y códigos; 180 s propuestos en ambos. Sin paseo, matchmaking, física orbital, voz, cuentas ni migración de host.

## Constitution Check

La constitución instalada es una plantilla sin ratificar; no se le atribuyen reglas ficticias. Para esta planificación se comprueba la base efectiva del usuario y AGENTS.md: identidad Jorge confirmada; Godot explícito; planificación en repositorio de agentes; código en un destino separado; tareas con un escritor por archivo; fuentes y propuestas distinguidas; no datos NASA inventados; checkpoints atribuidos. Resultado antes y después del diseño: conforme a esas reglas. La ratificación de una constitución de producto no se presenta como realizada y no se usa para pedir una aprobación adicional del plan. T001 identifica el destino antes de programar.

## Project Structure

### Documentation (real, in this repository)

`specs/001-launch-control-godot/`: spec.md, plan.md, research.md, data-model.md, quickstart.md, tasks.md, assignments.md, contracts/session.md, contracts/modules-and-ui.md, checklists/requirements.md, references/.

### Source Code (planned, separate game repository)

All paths prefixed `GAME/` are relative to the future game repository. GAME is an alias, not an existing folder or a new repository created here.

```text
GAME/
├── project.godot                       # Jorge: composition and export config
├── export_presets.cfg
├── autoload/
│   ├── session_service.gd              # Adrian: transport and role assignment
│   ├── round_controller.gd             # Adrian: authoritative states
│   └── server_clock.gd                 # Adrian: authoritative clock
├── scenes/
│   ├── main.tscn                       # Jorge: composition only
│   ├── lobby/lobby.tscn                # Adrian: lobby
│   ├── cockpit/cockpit.tscn            # Gael: cabin
│   ├── tower/tower.tscn                # Gael: office and laptop model
│   ├── modules/antenna_view.tscn       # Gael: visual view
│   ├── modules/code_view.tscn          # Kevin: visual view
│   └── outcomes/{launch,failure}.tscn  # Gael: presentation
├── scripts/modules/                    # Kevin: rules, definitions, reset
├── ui/manual/                          # Isra: index, pages and focus
├── ui/tools/calculator.tscn            # Isra
├── ui/hud/round_hud.tscn               # Isra: persistent clock
├── resources/{modules,manual,difficulties}/
├── assets/{cockpit,tower,outcomes}/
├── harness/                            # Sojo: reproducible validation scenes
└── docs/{setup,art,qa,demo}/
```

**Structure Decision**: fixed cameras keep 3D scenery local; only game state crosses the network. Rule files are independent of views. Main scene instances other owners' scenes instead of duplicating their nodes. The laptop uses focus plus a Control overlay in MVP; embedding clickable UI on its 3D screen is deferred.

## Design and Interfaces

[research.md](research.md) records official sources and reasoning. [data-model.md](data-model.md) defines entities. [session contract](contracts/session.md) governs authority, timing, roles, validation and resets. [module/UI contract](contracts/modules-and-ui.md) governs data, signals and information separation. These are design documents, not an implemented API.

Host can play either role. Client sends intentions; host validates sender, role, round, component and time, updates state once and broadcasts a monotonic revision. Deadline uses host monotonic time; client display estimates and corrects. At exact zero expiry wins. Disconnect interrupts the round. No full world replication, RPC from each visual scene or duplicated client victory logic.

## Delivery and Integration

1. Confirm game repository and bootstrap (T001–T006).
2. Freeze core interfaces and validate state flow (T007–T010).
3. Demonstrate antenna end to end (T013–T019): first playable cut, not final artwork.
4. Integrate 3D workstations and manual (T020–T025).
5. Add proposed second module and difficulty (T026–T032).
6. Add final presentation and rematch (T033–T037).
7. Export, test external networks, verify acceptance and document demo (T038–T042).

Do not execute all 42 tasks through one AI prompt. Each person declares name, takes one ready task, supplies its contracts and acceptance case to their AI, inspects the diff, records evidence and creates their attributed commit. Each task has one owner; [P] only permits different owners/files after listed dependencies are met. No fixed dates or skill-level claims are invented.

## Risks and Complexity Tracking

No engine source changes, server infrastructure or external plugin justified at this stage. The main risks are Internet reachability, scene merge conflicts and overbuilding all reference modules. T039 owns the external-network proof; file ownership prevents shared scene edits; scope is limited to two modules. A route blocked by CGNAT is not fixed by promising that ENet or port forwarding always works. Local demos remain interim evidence, not FR-020 completion.
