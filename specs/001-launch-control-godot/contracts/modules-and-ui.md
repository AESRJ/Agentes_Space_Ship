# Contract v1 — Modules and role UI

Kevin owns rules/definitions; Gael owns antenna visual and scenery; Isra owns manual, calculator and HUD; Sojo owns session state (original implementation by Adrian; ADR-0005). Jorge connects scenes without editing other owners' internal node structures.

## Module boundary

A module view receives a role-filtered instance and emits an attempt payload. It never writes RoundState or decides victory. Minimum view operations: bind_instance(instance), show_feedback(command_id,reason), set_locked(boolean), reset_view(round_id). Scene-local node names stay internal; exported signal attempt_requested(module_id,payload) is the integration boundary. SessionService adds round/command identifiers. Pending/solved is host-owned.

**antenna**: clue fixed/blinking; payload symbol moon/star; host rule fixed→moon, blinking→star. View contains light, two explicit shape-labelled selections, Confirmar and Listo/Pendiente feedback. Wrong leaves pending and does not reduce time beyond normal countdown.

**code**: clue two pairs of A/B/C/D; table A=2 B=5 C=7 D=9; concatenate each pair then multiply. Example AB/CD →25×79→1975. Allowed answer is an integer 484..9801 (up to 4 decimal digits); empty, decimals or outside-range input shows a validation error, no resolution. Other in-range wrong answers leave pending. Resource rule_version=1 is shared between manual and authoritative evaluator.

## UI boundary

- Manual routes: index → antenna or code; code page → calculator; calculator → code page; section → index. Only active module sections are required. Index may show all with inactive visibly labelled, but inactive sections cannot create game modules.
- Laptop focus toggles office/world input versus manual UI input. Esc/back returns office or previous page as documented; cannot route clicks to a hidden astronaut control.
- HUD is a separate CanvasLayer or persistent Control sibling, never a child of a page replaced during navigation. It shows timer, pending count and terminal status.
- Calculator supports two positive two-digit integers and multiplication, clear/back and result. No unrestricted expression evaluator or scientific operations are needed.
- Tower never receives live clue payload in its normal UI; astronaut never opens manual/calculator. Completion counts and terminal result are shared.
- Camera at seated fixed position; environment is local. Cabin sees sky through window; office sees rocket from platform. A fallback shape/text reinforces any light/color cue.

## Presentation boundary

round_finished triggers a local outcome scene once per round. Success: tower rocket movement, cockpit sky/motion/light equivalent. Timeout: tower comic failure and cockpit equivalent effect/message. Interrupted: status screen without explosion. Animations do not send solved events. After return to lobby each owning view clears local state before a new round.
