# Baseline Analysis — What We Have, What Sahaj Has, Where The Gaps Are

> Source-grounded analysis of (a) the existing HCLTech draft deck and (b) the Sahaj Software
> talk, written before the external research landed so it records the *unassisted* reading of
> the material. Every statement about either deck is traceable to the extracted artefacts in
> `research/raw/`.

---

## Part 1 — Faithful transcription of the existing HCLTech draft deck

Seven slides, from `HCLTech-ppt-screenshots/`. Classification marking: *Internal*. Co-branded
HCLTech + ING.

### Slide 1 — Agenda
| Section | Stated purpose |
| --- | --- |
| AI Assisted Delivery Model | How the AI-assisted model reshaped the BTA delivery approach |
| PRIME.AI Methodology | The methodology underpinning the custom GHCP agent framework |
| Agent Overview & Architecture | The seven agents deployed across the SDLC and how they fit together |
| Agent Workflow | How the agents interact end-to-end across the engineering lifecycle |
| Demo | A live walkthrough of the agents in action |

### Slide 2 — "Acceleration Driven By AI-Assisted Delivery" (Transforming the BTA Payments Program)
- **Scope statement:** the Core Banking team adopted an AI-assisted methodology within the
  **BTA Payments stream** to meet an accelerated launch timeline; aim was to maximise
  development velocity "while strictly safeguarding software quality".
- **Challenge:** speed without sacrificing quality.
- **Approach:** "A PRIME.AI-based instructions, skills, agents, prompts — via custom agents
  build across SDLC phases."
- **Result:** *30% productivity improvement from the time of AI adoption*; freed ~2 sprints
  of capacity, used to absorb the additional **DG** requirements.
- **Impact at a glance:** 30% faster delivery velocity. **1 squad of 10 engineers assisted by
  7 agents.** Bar chart, "Timeline comparison (months)": Manual **3.5** → Agentic **2.5**.

### Slide 3 — "AI-Assisted BTA Project Delivery" (Deconstructing the 80/20 AI-Assisted Delivery Model)
Two streams, each split 80% AI-assisted / 20% non-AI:

| Stream | AI-assisted (80%) | Non-AI (20%) |
| --- | --- | --- |
| Coding & Unit Testing | Generating user stories; analysing dependencies; code development; unit test case generation; code coverage & fix defects | Pipeline creation; build application; deploy to ST & SIT; validation |
| Quality Engineering & Testing | Generating test cases; defect triage; analysing defects; defect reporting; test automation script generation | Test case execution; validation and approval |

- Illustrative squad: previously delivered endpoints in **API Factory**, now in BTA Payments.
- **Impact on endpoints delivery: 2 sprints → 1.4 sprints, ~30% faster.**

### Slide 4 — "Our Methodology & Approach"
- **PRIME.AI = Prompt driven, Reusable, Intent focused, Modular Engineering.**
- *Agent Configuration* — four markdown artefacts feeding "Agent Capability":
  - `instructions.md` — **who** the agent is
  - `skills.md` — **what** the agent can do
  - `agents.md` — **how** the agent executes
  - `prompts.md` — templates used
- Flanking concepts: **Dynamic Knowledge Graph** (left) and **Context Engineering** (right),
  funnelling into *"Engineered to be Token Efficient"*.
- Badge row: DevOps & SRE Enabled · Developer & Tester Friendly · Orchestration efficient ·
  Multi-Agentic Framework · LLM & token Friendly.

### Slide 5 — "Agents Overview" (seven agents, with a % badge each)

| # | Agent | Stated function | Declared inputs | Badge |
| --- | --- | --- | --- | --- |
| 1 | User Story Generation | Analyses requirements docs, generates user stories with acceptance criteria and traceability links | FSA + transcript | ~30% |
| 2 | Test Case Generation | Reviews user stories and interaction models → functional and regression test cases | FSA + transcript + user stories | ~30% |
| 3 | Code Generation | Converts approved designs and specifications into production-ready code | FSA + user stories + dependent repos + transcript + query log + mapping doc | ~25% |
| 4 | Unit Test Case Generation | Creates and validates unit tests, improving coverage without manual scripting | FSA + user stories + repo | ~35% |
| 5 | INGenious Test Script Generator | Reviews FSA and test cases, generates automation scripts, validates coverage across key user workflows | FSA + test cases | ~20% |
| 6 | Defect Triage | Reviews test results, classifies root causes, routes defects to the right owners | test cases + defects | ~25% |
| 7 | Mechanic | Inspects functional requirements and specs, flags automation gaps, recommends fixes via automated scans | FSA + dependent repo + test cases + defects + user stories | ~25% |

### Slide 6 — "Agent Architecture & Integrations"
- **AI engine:** GHCP Custom Agent ("custom-built GitHub Copilot agent orchestrating BTA
  delivery workflows") **+** Claude LLM ("reasoning and code generation").
- **Integrations:** Azure DevOps pipeline logs *via Azure CLI* · BIAB Region (OpenShift logs)
  *via OpenShift CLI* · Red Panda logs *via CLI* · Orange Sharing *via PAT tokens* · Forge
  documentation *via Forge CLI* · Azure Repo *via Azure CLI* · Teams meeting transcripts
  (*footnoted: currently fed offline*).
- **Outcomes:** Knowledge Graph ("unified enterprise knowledge base built from all integrated
  sources") · Output Compression ("condenses agent outputs into concise, actionable
  artifacts") · Self Learning ("continuously improves agent accuracy from feedback loops").

### Slide 7 — "Multi Agent Automation: Automating SDLC"
Four lanes, with role owners and a `*` marking human-in-the-loop steps:

1. **Requirements Gathering** (Business Analyst) — Story Generator. Fetch feature page from
   Orange Sharing → fetch attached docs/files from SharePoint in the FSAs → generate EPIC-wise
   user stories → `*` once BAs confirm and verify, push directly to ADO or upload via CSV.
2. **Development** (Developers) — Developer Agent + Unit Test Generator. Refer Forge
   documentation for coding standards → connect to Azure DevOps for story → connect to
   dependent repo and clone a local copy → `*` analysis and share implementation plan for
   engineer to validate → generate code → feedback. Unit test lane: uses cached KG of FSAs,
   transcripts, user stories and the code generator agent → generates and validates unit tests
   with `mvn clean test` and install → `*` raise PR post verification → feedback.
3. **Test Preparation** (Testers) — Test Case Generator + Test Script Generator. Fetch US from
   ADO with related links, attachments, comments → `*` analyse gathered KG cache of the FSAs
   and the US → generate ADO-importable test cases → after verification push to task board.
   INGenious script generator: generates scripts from cached KG or ADO or Orange Sharing →
   builds reusable components for assertions → `*` post-verification PR raised and proceed.
4. **Testing & Resolution** (Testers & Developers) — Defect Triage + Mechanic. Fetch bug
   info/attachments/comments from ADO → generate daily triage report. Mechanic: uses cached KG
   for complete bug context → reproduces the error by getting response from the endpoint, OCP
   logs → thorough analysis, deep research RCA and resolution plan → does the fix and after
   engineer's verification pushes changes through build and release pipelines.

---

## Part 2 — What the existing deck gets right

These are real strengths and must survive into the rewrite.

1. **It is grounded in a real delivery, not a lab.** Named stream (BTA Payments), named squad
   size, named tools, named artefacts (FSA, ADO, INGenious, Forge, Orange Sharing). This is the
   single most valuable asset in the pack — most competitor material is generic.
2. **The four-file agent configuration model is genuinely aligned with where the industry
   landed.** `instructions.md` / `skills.md` / `agents.md` / `prompts.md` maps almost exactly
   onto the emergent conventions: `.github/copilot-instructions.md`, Claude Agent Skills
   (`SKILL.md`), `AGENTS.md`. That is a credibility point that is currently buried.
3. **Human-in-the-loop is already explicit** on slide 7 with a marked legend. In a bank this
   is the most important design property on the page and it is rendered as a red asterisk.
4. **Coverage is genuinely end-to-end** — requirements → code → unit test → test case → test
   script → defect triage → fix → release. Very few competitor stories span the whole lifecycle.
5. **"Knowledge Graph" and "Context Engineering" already appear** as the differentiators.

## Part 3 — Where the existing deck is weak (candid)

Ordered by how badly each would hurt in front of ING leadership.

### W1. The knowledge graph is asserted, never explained — and the words used undercut it
The KG appears three times and each time weaker than the last: as a flanking label on slide 4
("Dynamic Knowledge Graph"), as an *outcome* on slide 6 ("unified enterprise knowledge base
built from all integrated sources"), and on slide 7 as **"cached KG"**.

- Calling it an **outcome** is backwards. A knowledge graph that is a *by-product* of running
  agents is a log. The entire argument for a graph is that it is an *input* — the substrate
  agents read from *before* they act.
- Calling it a **cache** is worse. A cache is a disposable performance optimisation.
  If the KG is a cache, then the honest description of this architecture is
  "seven prompts with a shared scratch directory", and a sharp reviewer will say exactly that.
- There is no schema, no entity types, no relationships, no query, no persistence story, no
  refresh story, no ownership. Nothing that survives the question *"show me the graph."*

**This is the biggest gap, and it is also the biggest opportunity**, because the KG is
precisely where the strongest external evidence and the strongest differentiation live.

### W2. The percentage badges are indefensible as presented
Each agent carries a bare "~30%", "~25%", "~35%". Of what? Effort saved, cycle time, coverage,
adoption? Measured how, against what baseline, over what period, with what confidence? These
numbers are the first thing a CFO or a delivery lead will attack, and there is no methodology
slide to fall back on. Worse, they are *near-identical* (20–35%), which reads as estimation
rather than measurement.

### W3. "80% AI-assisted" is the single most attackable claim in the pack
Slide 3 says coding and unit testing are "80% AI-assisted". Taken literally this says 80% of
the bank's payments code is machine-written. In a regulated core banking payments context that
sentence is a risk-committee trigger, not a selling point. The intended meaning is almost
certainly "80% of *activities in this stream* had AI assistance available", which is a very
different and much weaker claim. As written it invites a supervisory question the team cannot
comfortably answer.

### W4. Quality and risk are asserted, not evidenced
Slide 2 says the goal was speed "while strictly safeguarding software quality" — and then the
deck presents no quality evidence at all. No defect escape rate, no change failure rate, no
coverage delta, no rework/churn measure, no security finding rate. The external evidence base
(DORA 2024/2025 on stability, GitClear on churn and duplication, METR on perceived vs actual
speed) says this is *exactly* where AI delivery claims break. Presenting velocity without
stability in front of a bank is presenting half of the DORA scorecard, and the missing half is
the one the CRO cares about.

### W5. There is no orchestration story
Seven agents are listed on slide 5 as a flat catalogue and sequenced on slide 7 as four swim
lanes. Nothing explains who schedules them, what happens when one fails, what runs in
parallel, what state passes between them, how conflicting outputs are reconciled, or how
context is prevented from leaking between them. Slide 4 claims "Orchestration efficient" as a
badge. Sahaj devotes an entire layer (the Conductor) to precisely this question and asks it
explicitly: *"Who watches the workers?"* We currently have no answer.

### W6. Nothing about governance, audit, or regulation
For a European systemically important bank this is a startling omission. Nothing on: who is
accountable for agent-authored code; how agent actions are logged and attributed; how
requirement→code→test→approval traceability is evidenced to an auditor; source-code
confidentiality and data residency; EU AI Act or DORA posture; agent identity and least
privilege. The deck is addressed to ING leadership but answers none of the questions ING
leadership is obliged to ask.

### W7. The agent roster is shaped like the org chart, not like the problem
The seven agents mirror job titles (BA, dev, tester, triage). That is intuitive but it means
every agent is a *generator* — story generator, code generator, test generator, script
generator. There is almost nothing that **understands** (comprehension of the existing
estate), nothing that **verifies** independently, nothing that **maintains the shared model**,
and nothing that **governs**. A fleet of seven generators pointed at a legacy core banking
estate will produce a large volume of plausible artefacts with no independent check —
which is the documented failure mode.

### W8. The reverse-engineering / legacy comprehension problem is entirely absent
Every input on slide 5 is a *document* (FSA, transcript, user story) or a raw repo. But the
hardest and most valuable problem in core banking transformation is understanding the existing
system — what it does, what depends on it, what breaks if it changes. Sahaj's entire talk is
about this problem. We do not mention it. In a *transformation* programme, that is the gap
that matters most commercially.

### W9. Weak framing: "AI-assisted delivery" is a commodity claim
Every SI in the world is currently saying this. Nothing on slides 1–3 could not be said by
Accenture, TCS, Infosys, Capgemini or Cognizant next week. The defensible asset — a
persistent, governed, queryable model of the bank's payments estate — is the one thing a
competitor cannot copy from a slide, and it is currently the least developed idea in the deck.

### W10. Presentation-level issues
Overlapping text on slide 5 (input lines collide with the card below), inconsistent styling
between slide 4 (different template, different footer, "Copyright © 2026 HCLTech |
Confidential") and the rest, and a demo slot with no stated success criteria.

---

## Part 4 — Sahaj Software: full reconstruction and assessment

Talk: *"The Practical Guide to Reverse Engineering XXL Codebases with Agentic AI"*,
Harshad Nawathe, Solution Consultant, Sahaj Software.

### Their argument, in order
1. **Constraints dictate architecture.** Opens on `std::sort`: in-memory algorithms assume
   unbounded resources; hardware limits shatter pure algorithmic theory; at sufficient scale
   you must pivot from *local computation* to *systemic coordination*. (This is the external
   merge-sort analogy, and it is a very good one.)
2. **APS**: **A**cknowledge the limits of the container · **P**artition into isolated,
   parallelisable workloads · **S**ynthesize distributed outputs into a cohesive state.
3. **The one-shot prompt fails.** They show a genuinely well-engineered ten-line "Principal
   Engineer" reverse-engineering prompt — and it still fails at scale.
4. **Compaction kills context.** The agent fills the window silently; compaction drops
   instructions; the model forgets, then invents. *"Larger context window? Same problem.
   Bigger bucket."*
5. **Four Perils of Context Overload**: context contamination · low signal-to-noise ratio ·
   lost in the middle · attention dilution.
6. **The pivot question: "What if the agents never read the code?"**
7. **Deterministic tools for deterministic work.** Cognitive tasks → LLM agents; parsing,
   indexing, dependency resolution → purpose-built tools. *"LLMs read for meaning — not for
   structure. Structure is already encoded in build files, LSP servers, symbol indexes. Don't
   burn context tokens on work a compiler does for free."*

### Their pipeline — five layers, eleven agents, one orchestrator

| Layer | Agent(s) | Reads | Code access | Produces |
| --- | --- | --- | --- | --- |
| 0 | **Scout** | Build files only (`pom.xml`, `build.gradle`, `package.json`) | **Never** | Project skeleton JSON + module summary |
| 1 | **Cartographers** | Scout's skeleton JSON | **Never** — only tool output (LSP, symbol indexers, dependency analysers) | Symbol index: classes, methods, interfaces, inter-file relationships |
| 2 | **Specialists** — Archaeologist, Taxonomist, BeanStalkJack | Symbol index | Surgical reads only — targeted, bounded, intentional | Entity models, Spring bean graphs, concept taxonomies |
| 3 | **Surveyors** — Port Mapper, Surveyor, Choreographer | All Layer-2 artefacts + symbol index | Surgical reads only | Service boundary maps, integration topology, workflow graphs |
| 4 | **Chronicler** | All artefacts from Layers 0–3 | **None** | Complete technical domain documentation |
| Orch. | **Conductor** | **Pipeline state only** — completed, failed, pending | None | Scheduling, scaling, retry/replan/escalate |

The Conductor is explicitly a **hub, agents are spokes**; *"state flows in, instructions flow
out"*; its context is *"the leanest in the entire system — state only, no content."* It is
introduced by three questions: who decides how many Cartographers to spin up, what happens
when a stage fails, and how the pipeline knows what runs in parallel versus what must wait.

### Their four principles of context engineering
- **Progressive Disclosure** — reveal information strictly as the role requires. *Structure
  before content. Boundaries before reads.*
- **Deterministic Grounding** — fast deterministic tooling for structural work; reserve LLM
  context exclusively for semantic reasoning.
- **Role Isolation** — one agent, one competency, one narrow context. *"Specialisation
  eliminates hallucination and instruction drifts."*
- **Subagent Isolation** — delegate cognitive tasks to disposable subagent contexts; keep the
  orchestration layer uncontaminated.

### Their claimed output
10,000+ classes/methods indexed and queryable · 200+ documents (~15MB) · 400+ database tables
mapped to entity classes · 80+ REST and 60+ SOAP endpoints catalogued · 15+ service boundaries
identified and "ready for decomposition" · 80+ workflow traces with sequence diagrams ·
C4 diagrams at three levels · incremental regeneration via input fingerprints.

### Their production lessons
Validate early (*"trust in generated documentation must be earned, not assumed"*) · evolve the
tools, the architecture holds · decoupled layers evolve independently, the inter-layer contract
is the only fixed thing · **respect the economics** — *"the full pipeline justifies its cost
only when a holistic view is needed."*

---

## Part 5 — Head-to-head: where each is stronger

| Dimension | HCLTech PRIME.AI (current draft) | Sahaj | Verdict |
| --- | --- | --- | --- |
| **Lifecycle coverage** | Requirements → code → unit test → test case → script → triage → fix → release | Comprehension only; stops at documentation | **HCLTech far broader** |
| **Direction** | Forward engineering (spec → artefact) | Reverse engineering (code → understanding) | **Complementary — neither is complete** |
| **Legacy comprehension** | Absent | The entire thesis, done rigorously | **Sahaj decisively better** |
| **Context engineering** | One badge: "Engineered to be Token Efficient" | Four named principles, derived from stated failure modes | **Sahaj decisively better** |
| **Orchestration** | Not addressed; one badge | The Conductor — a designed component with scaling, scheduling, failure handling | **Sahaj decisively better** |
| **Deterministic vs cognitive split** | Not addressed; agents read repos directly | Central design rule; agents mostly never read code | **Sahaj decisively better** |
| **Role isolation / context hygiene** | Not addressed | Explicit principle | **Sahaj better** |
| **Knowledge representation** | "Knowledge graph" asserted, treated as cache/outcome | Symbol index + 200 markdown documents. Honest, but documents don't compose or answer arbitrary queries, and they go stale | **Both weak — this is the open ground** |
| **Ontology / business semantics** | Absent | Absent (a "Taxonomist" agent, but no formal ontology) | **Neither has it — biggest differentiator available** |
| **Business/requirements linkage** | Implicit via FSA and ADO | None at all | **HCLTech better, but not made explicit** |
| **Client-embeddedness** | Deep: real stream, real tools, real squad | Generic Java monolith | **HCLTech better** |
| **Measured outcomes** | 30%, unspecified methodology | Volumetric counts (classes, docs, endpoints) — countable but not value-linked | **Both weak; Sahaj's are at least verifiable** |
| **Governance / regulation** | Absent | Absent (not their audience) | **Neither — mandatory for us** |
| **Economics honesty** | Absent | Explicit: "respect the economics", says when *not* to build it | **Sahaj better, and it builds trust** |
| **Runtime / operations** | Touches OpenShift + Red Panda logs, Mechanic agent does RCA | None | **HCLTech better** |

### The single most important observation

**Sahaj's output is documents. Ours should be a model.**

Sahaj produces 200+ markdown files (~15MB) generated from current code. That is a real
achievement and it beats what we have today. But it has three structural weaknesses we can
name honestly and exploit:

1. **Documents don't compose.** You cannot ask 200 markdown files *"which services touch the
   SEPA instant payment flow and which of them have no regression coverage?"* You can ask a
   graph that.
2. **Documents are write-once per generation.** Their incremental fingerprinting regenerates
   *artefacts*; it does not maintain a *model* with identity and history. There is no way to
   ask what changed, when, and why.
3. **There is no business layer.** A symbol index and a taxonomy of code concepts is not a
   domain ontology. Nothing connects `PaymentProcessorImpl` to *"SEPA Instant Credit
   Transfer"*, to the regulation that mandates it, to the requirement that specified it, or to
   the test that proves it.

Meanwhile, this is *exactly* the gap the external primary sources point at:

- **Matt Pocock** independently arrives at the need for a shared "ubiquitous language" between
  human and agent — and implements it as a markdown file.
- **Emil Eifrem (Neo4j)** answers that directly: *"markdown files… it is part of the solution,
  but it is not the solution"* — you need a **business ontology + technical ontology +
  execution traces**, i.e. thin agents on a smarter shared substrate.
- **Frank Coyle** supplies the third leg: the ontology is not just retrieval, it is a
  **validator** — a symbolic guardrail on probabilistic output (neuro-symbolic AI).
- **Sahaj** supplies the discipline for getting facts into that substrate cheaply and
  reliably (deterministic grounding, progressive disclosure, role isolation).

So the synthesis writes itself: **Sahaj's rigour, applied to build and maintain a
business-grounded ontology rather than a documentation set, spanning the whole lifecycle
rather than comprehension alone, and governed to banking standards.** That is a genuine
superset, and each of its four parts is externally supported rather than invented.

---

## Part 6 — What the rewrite must therefore do

| # | Requirement | Because |
| --- | --- | --- |
| R1 | Promote the knowledge graph from by-product to **substrate**, with a real schema, real queries, real ownership and real refresh | W1; it is the only defensible differentiator |
| R2 | Add a **business ontology layer** grounded in BIAN / ISO 20022 / FIBO rather than invented | Neither competitor has it; ING is a payments bank |
| R3 | Add **comprehension agents** for the existing estate, adopting Sahaj's layered discipline | W8; highest commercial value in a transformation |
| R4 | Add an explicit **orchestration layer** with failure, parallelism and state semantics | W5; "who watches the workers?" |
| R5 | Publish the **deterministic vs cognitive** split as a design rule | W3, W7; also the honest answer to token cost |
| R6 | Replace bare percentages with a **measurement model** — baseline, method, confidence, and both velocity *and* stability metrics | W2, W4 |
| R7 | Add a **governance and audit** layer: traceability graph as compliance asset, agent identity, approval gates, EU AI Act / DORA posture | W6; mandatory for this audience |
| R8 | Rebalance the agent roster: not only generators, but comprehenders, verifiers, curators and governors | W7 |
| R9 | State the **economics honestly**, including when *not* to use the full pipeline | Sahaj's most trust-building slide; costs nothing to copy |
| R10 | Reframe the top-line story away from "AI-assisted delivery" to something a competitor cannot say next week | W9 |
