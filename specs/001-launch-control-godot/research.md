# Phase 0 — Research and design decisions

Status: researched proposal; Godot itself is explicitly requested by Jorge. Consultation: 2026-11-14. No gameplay or network test has been executed for this plan.

## R1 — Current engine and language

**Decision proposed**: Godot 4.7.2 stable, standard edition, typed GDScript; pin the same version and export templates for every contributor. **Rationale**: a single toolchain avoids introducing .NET setup while replacing the historical Unity/C# plan. **Alternative**: Godot .NET remains possible if the team later elects C#; that is not assumed. Sources: https://godotengine.org/download/ and https://godotengine.org/download/archive/.

## R2 — Network authority

**Decision proposed**: one participating host plus one client using ENet; a common session node with matching NodePath and RPC declarations in both executables. Host may be astronaut or tower; role never determines authority. Sender identity is checked on server. **Rationale**: one outcome and one clock are easier to reason about than duplicated decisions. **Alternative**: hosted dedicated server or relay adds deployment and is unnecessary until reachability is tested. Official API and UDP limitations: https://docs.godotengine.org/en/4.7/tutorials/networking/high_level_multiplayer.html.

**Important boundary**: UDP host must actually be reachable. LAN, localhost and two networks are different validation levels. Port forwarding may be needed; ENet alone does not solve NAT/CGNAT. If inaccessible, test an available private network or change hosting route, document it and repeat the two-network scenario. Do not promise a public no-setup lobby.

## R3 — Time and duplicate actions

**Decision proposed**: host monotonic deadline with Time.get_ticks_msec(), current round ID, command ID and revision. Reject commands when now ≥ deadline, when terminal or when stale. Client clock is presentation only. **Rationale**: wall-clock changes and delayed packets must not reverse a result. The API supplies monotonic time; the precedence and duplicate policy are our design inference. Source: https://docs.godotengine.org/en/4.7/classes/class_time.html.

## R4 — Laptop and fixed-camera scenes

**Decision proposed**: office includes a 3D laptop; focusing it opens a readable Control/CanvasLayer interface. Timer remains outside page/tool containers. **Rationale**: preserves scene and manual use without implementing ray-to-UV input mapping. **Alternative deferred**: SubViewport rendered on mesh. A standalone SubViewport does not automatically receive pointer input; special routing is needed. Sources: https://docs.godotengine.org/en/4.7/classes/class_subviewport.html, https://docs.godotengine.org/en/4.7/tutorials/rendering/viewports.html and https://github.com/godotengine/godot-demo-projects/tree/master/viewport/gui_in_3d.

## R5 — Reference images and scope

Antennas use the exact two rules in the source. The numeric extension uses a new four-letter table and basic multiplication; no copied reference game text or art. Only two difficulties are proposed, with 180 s each. A simple comedic effect satisfies the failure theme; a tiny parachute is optional polish within T034, not a third game system. No claim that a lunar/star selector simulates physical antenna alignment: it is an abstract communication puzzle.

## R6 — Source conflict and accounts

The new explicit Godot request supersedes docs/plan-unity.md for this prototype. NotebookLM also describes other local Unity work and accounts; those summaries do not establish current code or identity. After fetching Git, origin/main c2c38a0 verifies Kevin → KVSO755 and Jorge → AESRJ. Adrian's account appears in memory but is not integrated into the canonical roster, so no new mapping or GitHub assignee is inferred. All six are assigned by their confirmed names. Source copies preserve hashes and keep the original methodology as historical content excluded from this workflow.
