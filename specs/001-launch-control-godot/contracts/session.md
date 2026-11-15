# Contract v1 — Session, clock and authority

Owner: Sojo since 2026-11-15 (original implementation by Adrian, ADR-0005); Jorge owns composition. This interface must be implemented identically in both role builds. Match NodePath under the shared autoload SessionService, RPC declarations and serialized fields. Specific Godot annotations are selected in T007, validated in T011, not scattered in scene scripts.

## Commands and notifications

| Intent/event | Who may send | Required content | Expected effect |
| --- | --- | --- | --- |
| request_role | connected peer in lobby | role astronaut/tower | host binds if role free, otherwise rejection with current roster |
| set_ready | peer with assigned role in lobby | boolean ready | start only when both ready |
| select_difficulty | host in lobby | easy/normal | store and notify; reject during play |
| submit_attempt | bound astronaut peer | round_id, command_id, module_id, selection/value | host validates and evaluates rule; never accept a client solved flag |
| snapshot | host only | round_id, revision, phase, remaining_ms, role-filtered module data, result | client applies only current/new round and newer revision |
| attempt_feedback | host only | matching command_id, accepted boolean, reason code | show success/wrong/stale/inactive/not_allowed/expired; rejected intent does not mutate state |
| round_finished | host only | round_id, revision, result success/timeout/interrupted | immutable result, lock controls and trigger local presentation once |
| return_to_lobby | connected peer after terminal | round_id | clear readiness; start another round only when both ready again |

## Time precedence

Host uses monotonic milliseconds and checks deadline before evaluating a submitted answer. If now ≥ deadline, first close as timeout; if now < deadline and all active modules solved, close as success. Client-provided send timestamps never override this order. Timer display can interpolate but cannot award success. Proposed snapshot cadence 4 Hz plus immediate state changes; periodic time updates must carry newer revisions. During terminal no clock update can revive play. Target display difference ≤1 s under documented stable test conditions.

Host submits its own local-role actions through the same validation function; whether the host plays tower or astronaut must not bypass permissions. Sender is taken from transport or local host context. Commands use reliable delivery; bounded duplicate ID tracking is reset each round. Losing the host/client during play interrupts without host migration. Time synchronization and measured latency are validated in T009/T019/T039.

## Gate before network acceptance

T039 proves two external networks and records transport route, builds and results. No router secrets, public IP logs or personal identifiers go into Git/NotebookLM. If direct UDP is unavailable, document a tested alternative route and repeat; localhost and LAN are intermediate checks only. No Internet success is claimed from API design alone.
