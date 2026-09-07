# PRIME.AI v2 — ING Core Banking / BTA Payments

Deliverables for the ING leadership pitch. Read in this order.

## The two deliverables

| # | File | What it is |
|---|---|---|
| **1** | **[`03-slide-deck-content.md`](03-slide-deck-content.md)** | **The pitch.** 20 main slides + 5 appendix, in 4 acts. Every slide has: title-as-claim, exact on-slide text, visual instruction, Mermaid source, and speaker notes with evidence tier + hostile Q&A rebuttal. **Build the PPT from this.** |
| **2** | **[`04-research-paper.md`](04-research-paper.md)** | **The defence.** Research-paper-grade cited dossier. Every claim tiered T1–T4. Contains the counter-evidence, the limitations, and the "when not to build this" section. Read before presenting. |
| **3** | **[`05-knowledge-graph-technical-deep-dive.md`](05-knowledge-graph-technical-deep-dive.md)** | **The technical annex.** What is actually in the graph: full metamodel, the L0–L6 build pipeline, a worked Verification-of-Payee example, the agent retrieval contract, ontology constraints, the curation loop, 7 runnable Cypher queries, sizing and blind spots. For architects and the tech review board. |
| **4** | **[`06-agent-fleet-layer-by-layer.md`](06-agent-fleet-layer-by-layer.md)** | **The agent story.** Sahaj-style layer-by-layer breakdown: today's 7 HCL agents and their one structural flaw, the 16-agent / 6-layer fleet, an agent card for every one (Mission / Reads / Tools / Writes to graph / Reads code? / Human gate), the Conductor, one payment feature traced end to end, and the migration map showing nothing is discarded. **Works for tech leads and business people in the same room.** |

## Diagrams

Two sets, both as **`.mmd` source + `.png` + `.svg`**, all render-verified with mermaid-cli
v11.17.0 and visually inspected. Drop the PNG or SVG straight into PowerPoint.

### `diagrams/` — business deck (8)

| File | Used on |
|---|---|
| `s03-problem` | Slide 3 — the four failure modes |
| `s05-convergence` | Slide 5 — six sources, one conclusion |
| `s08-architecture` | Slide 8 — the seven planes |
| `s11-payment-chain` | Slide 11 — regulation → evidence pack |
| `s12-agent-fleet` | Slide 12 — the agent fleet |
| `s13-orchestration` | Slide 13 — the Conductor |
| `s18-roadmap` | Slide 18 — the four stages |
| `paper-7planes` | Research paper §5.3 |

### `diagrams/tech/` — technical annex (12)

| File | Shows |
|---|---|
| `T1-why-graph` | Why a graph, not a doc set or vector store |
| `T2-three-layer-stack` | **The primary architecture picture** — business / bridge / technical / ground truth |
| `T3a-metamodel-core` | Node and edge types, business-to-technical |
| `T3b-metamodel-delivery` | Node and edge types, delivery and assurance |
| `T4-confidence-split` | **The compliance answer** — deterministic vs inferred facts |
| `T5-build-pipeline` | L0–L6; six of seven layers use no model |
| `T6-worked-example-vop` | **The sceptic-converter** — Verification of Payee, end to end |
| `T7-retrieval-contract` | Task → context pack → agent → validation → back to graph |
| `T8-role-query-contract` | Role isolation enforced by the query layer |
| `T9-ontology-validator` | Four gates before a human spends attention |
| `T10-curation-loop` | **Answers the strongest objection** — how it stays true |
| `T11-deployment` | Where it runs; sources are read-only |

### `diagrams/fleet/` — agent fleet (10)

| File | Shows |
|---|---|
| `F1-today-private-derivation` | **Today's flaw** — 7 agents each re-deriving privately. Establishes the problem without criticising the team |
| `F2-reframe-substrate` | The reframe — one substrate, thin agents |
| `F3-fleet-layers` | **The centrepiece** — 16 agents, 6 layers, and the loop that compounds |
| `F4-agent-contract` | The six-part contract every agent obeys |
| `F5-conductor` | The Conductor; failure as a designed state |
| `F6-end-to-end-feature` | **The story slide** — Verification of Payee from regulation to evidence pack |
| `F7-verify-independence` | Why the generator must not mark its own work |
| `F8-migration-map` | Today's 7 agents → their new positions. Nothing discarded |
| `F9-human-gates` | Six gates, six named accountable roles |
| `F10-build-order` | Four stages; stage 1 has no AI risk |

To re-render after editing a `.mmd`:
```bash
npx --no-install mmdc -i diagrams/s08-architecture.mmd -o diagrams/s08-architecture.png -b white -w 1800
```

## Working papers (source material — not client-facing)

| File | Contents |
|---|---|
| `01-baseline-and-gap-analysis.md` | Full transcription of the v1 deck; weaknesses W1–W10; head-to-head vs Sahaj; requirements R1–R10 |
| `02-methodology-architecture.md` | Extended architecture design; deterministic/cognitive split; measurement model |
| `raw/thread-E-talks-distilled.md` | 9,800-word distillation of all six practitioner talks + slide-ready quotes |
| `raw/evidence-note-01-metr.md` | Verification note on the METR studies — **read this before quoting any METR number** |
| `raw/sahaj-deck.txt` | Extracted text of the 25-page Sahaj deck |
| `raw/transcripts/` | Full transcripts of all six source talks |
| `03-slide-deck-content-DRAFT1.md` | Superseded first draft, retained for reference |

## Three things that will lose the room if you get them wrong

1. **Never say "AI makes developers 19% slower" in the present tense.** METR superseded that
   result on 24 Feb 2026 and now reports an 18% *speed-up* for returning developers — while
   disclaiming its own new data as an unreliable signal. Use the framing in the paper §2.1.
2. **Never say "80% AI-assisted."** In a supervised bank it reads as "80% of our payment logic
   is machine-written." It is a risk-committee trigger, not a proof point.
3. **Never present a bare percentage.** Every velocity number is paired with a stability number,
   and states baseline · method · population · period. See paper §8.

## The four slides that win the room

**6** (the gap nobody else fills) · **14** (where we don't use AI) · **17** (the counter-evidence,
delivered by us before they raise it) · **19** (stage 1 carries no AI risk).

If the meeting is cut to ten minutes, present those four.

## The agent-story arc (from `06`)

If you want one continuous narrative rather than a slide catalogue, run these four diagrams
in order — problem → architecture → proof → ask:

**F1** (here is the flaw in what we run today) → **F3** (here is the fleet) →
**F6** (here is a real payment feature flowing through it) → **F10** (here is the four-week,
no-AI-risk first step).
