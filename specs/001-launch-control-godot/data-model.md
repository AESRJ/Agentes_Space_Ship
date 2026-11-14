# Phase 1 — Data model

Design contract, not implemented classes. Host-only fields must not be included in general client snapshots.

| Entity | Fields and constraints | Owner |
| --- | --- | --- |
| Session | session_id; exactly 2 peer bindings; unique role per connected peer: astronaut/tower; per-peer ready; phase lobby/playing/finished/interrupted | Adrian |
| RoundConfig | difficulty easy/normal; duration_s positive, proposed 180; active IDs: [antenna] or [antenna,code]; config frozen at start | Adrian (Kevin supplies rule data) |
| RoundState | new round_id per attempt; revision strictly increasing; phase; host deadline_ms; remaining display clamped to ≥0; active module statuses; result none/success/timeout/interrupted | Adrian |
| ModuleDefinition | unique id; kind antenna/code; manual_section_id; caption; view resource; rule_version, proposed 1 | Kevin |
| ModuleInstance | instance_id; round_id; active; state pending/solved; role-filtered clue; current selection; answer stored/derived only in authoritative rules | Kevin |
| AntennaClue | light fixed/blinking; selected_symbol unset/moon/star; fixed answers moon, blinking answers star | Kevin |
| CodeClue | exactly 2 pairs of 2 letters each; allowed A/B/C/D; mapping 2/5/7/9; each decoded number has 2 digits; product integer between 484 and 9801 | Kevin |
| Attempt | round_id; command_id unique per peer and round; module_id; payload; sender peer derived from transport, never trusted as a payload assertion | Adrian |
| ManualSection | unique id; component name/illustration; question to astronaut; rule/table; tool_id nullable; timer is outside page content | Isra |
| CalculatorState | left/right integer operands; result; validation error; local-only; no authority over module/round state | Isra |

## Transitions and invariants

Session lobby → playing only with two connected peers in different roles, both ready. Host allocates new round ID, clues and deadline, then broadcasts the initial snapshot. Wrong attempt remains pending. Correct attempt changes only its module pending → solved; solving all active while now < deadline transitions once to success. If now ≥ deadline and no prior result, timeout wins. Disconnect during play transitions once to interrupted; after finish it only changes connection/lobby availability. A result is immutable for that round.

Returning to lobby clears both ready flags. New round creates fresh state and new round ID; old attempts are discarded. Presentation does not decide or change result. Duplicate command IDs never advance revision twice. The client uses a local receipt time plus remaining_ms to estimate the display; host ticks are not directly comparable to a different machine's monotonic clock.

## Separation by role

Both receive round ID, difficulty, remaining time, module completion status and outcome. Astronaut receives active clues and operates inputs; tower receives manual content, not live clues or correct answer computed for that exact round. The host application is authoritative and holds solution logic regardless of its local role; this is a cooperative prototype, not protection against a modified executable. No player account or personal data storage is required.
