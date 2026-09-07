# PRIME.AI v2 — ING Core Banking / BTA Payments

Deliverables for the ING leadership pitch. Read in this order.

## The two deliverables

| # | File | What it is |
|---|---|---|
| **1** | **[`03-slide-deck-content.md`](03-slide-deck-content.md)** | **The pitch.** 20 main slides + 5 appendix, in 4 acts. Every slide has: title-as-claim, exact on-slide text, visual instruction, Mermaid source, and speaker notes with evidence tier + hostile Q&A rebuttal. **Build the PPT from this.** |
| **2** | **[`04-research-paper.md`](04-research-paper.md)** | **The defence.** Research-paper-grade cited dossier. Every claim tiered T1–T4. Contains the counter-evidence, the limitations, and the "when not to build this" section. Read before presenting. |

## Diagrams

`diagrams/` holds all 8 flowcharts as **`.mmd` source + `.png` + `.svg`**.
All verified rendering with mermaid-cli v11.17.0. Drop the PNG/SVG straight into PowerPoint.

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
