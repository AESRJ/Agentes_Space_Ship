# Quickstart — Validation of the planned prototype

Status: procedures to execute when the game exists. None of these gameplay checks has been run in this planning task. GAME is the future repository from T001. Godot 4.7.2 and export templates are proposed; pin their actual version in T002.

## Setup

1. Person declares their name; reads spec, assigned task and both contracts. Install the same Godot build as other contributors.
2. Obtain GAME, import GAME/project.godot, use a branch <member>/<task-id>-<description>. This repository currently has no project.godot to run.
3. Export/open two instances with identical content. First test loopback, then two LAN machines, finally two different external networks. Use the lobby's host/join address and documented UDP port; do not put connection details in a public issue.
4. Use voice externally. Pick different roles, select easy, both ready. Either role must be able to host.

## Independent story checks

| Case | Procedure | Expected result |
| --- | --- | --- |
| Q01 / US1 | fixed light → moon, confirm before zero | Listo, success on both |
| Q02 / US1 | blinking → moon (wrong), then star | pending with retry, then success |
| Q03 / US1 | leave pending until zero; submit after expiry | timeout on both; result immutable |
| Q04 / US1 | duplicate role request, duplicate command, tower attempts input | rejection without duplicated role/effect |
| Q05 / US1 | disconnect during round, with either host role | interrupted, return to lobby possible for remaining peer |
| Q06 / US2 | check both seated views at 1280×720; focus laptop, index/page/back | visible environments, no inaccessible/occluded controls |
| Q07 / US2 | navigate manual and calculator over 3 minutes | timer stays visible; ≤1 s display difference under recorded stable conditions |
| Q08 / US3 | compare easy and normal, solve only one normal module | 1 versus 2 active; normal does not end early |
| Q09 / US3 | AB/CD →25×79=1975, wrong value then correct | wrong remains pending; 1975 resolves |
| Q10 / US3 | empty, decimal, out-of-range; navigate calculator | invalid input explained; no state corruption; calculator reachable in 2 actions from index |
| Q11 / US4 | force success/timeout twice with delayed/duplicate finish event | each presentation runs once, correct per role |
| Q12 / US4 | rematch, both ready, replay with old command from previous round | fresh clock/state; stale command ignored |
| Q13 / final | 5 rounds across 2 external networks; swap host role | no contradictory results, reachable transport documented |
| Q14 / final | measure both workstations on 2 identified PCs | ≥30 FPS at 1280×720; conditions and evidence recorded |

## Evidence and limits

Jorge consolidates GAME/docs/qa/acceptance.md with build revision, engine version, anonymous machine labels, scenario ID, actual/expected outcome, screenshots or short clips and unresolved defects. Sojo records connectivity route and clock observations without credentials or addresses. Failing Q13 means remote delivery remains pending even if Q01–Q12 pass locally. Presentation, FPS and network metrics are targets to verify, not achievements of this specification.

First playable cut: Q01–Q05 with a plain UI. Final prototype requires all rows and the acceptance mapping in tasks.md. No release/deployment is implied by this guide.
