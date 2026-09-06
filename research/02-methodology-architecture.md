# PRIME.AI — Methodology Architecture (working draft)

> Design document. The intellectual spine is sourced from `research/raw/thread-E-talks-distilled.md`
> (six primary conference talks) and the gap analysis in `research/01-baseline-and-gap-analysis.md`.
> Citations for external claims are added from research threads A–D. Claims are tiered per
> `.github/skills/prime-evidence-discipline/SKILL.md`.

---

## 0. The one sentence

> **We build and maintain one governed, living model of ING's payments estate — and then run
> thin, specialised, accountable agents on top of it.**

Everything else in this document is an elaboration of that sentence.

---

## 1. Why the name has to be re-anchored

The current expansion is **P**rompt driven, **R**eusable, **I**ntent focused, **M**odular
**E**ngineering. Every word describes *how we configure an agent*. None describes *what makes
the agents work*. It is a statement about prompt hygiene at a moment when the entire field has
concluded that prompt hygiene is not the bottleneck.

The six primary sources agree on this with unusual unanimity: **context — not the model, not
the prompt — is the bottleneck.** Blitzy states it flatly ("the gap isn't the model … context
is the thesis"). Sahaj engineers around it. Eifrem sells a substrate for it. Pocock makes the
codebase itself the multiplier. Coyle makes the ontology the guardrail. Hightower attacks the
cost of ignoring it.

So the letters stay — the team has equity in them and the rewrite should flatter the work, not
bin it — but each letter now names a **principle we can be held to**, four of which are
externally sourced rather than invented:

| | Principle | Origin |
| --- | --- | --- |
| **P** | **Progressive disclosure** — an agent receives the minimum structured slice its role requires, never the raw estate | Sahaj, principle 1 (verbatim) |
| **R** | **Role isolation** — one agent, one competency, one narrow context | Sahaj, principle 3 (verbatim) |
| **I** | **Intent traceability** — every artefact is linked, in the graph, from regulation → requirement → story → code → test → release → evidence | Our addition; the regulated-industry differentiator |
| **M** | **Model-grounded** — agents are grounded in *the bank's domain model*, not merely in *a language model*; structure comes from deterministic tools | Sahaj "deterministic grounding" + Eifrem's ontology + Coyle's neuro-symbolic validator |
| **E** | **Evidenced** — every claim of benefit carries a baseline, a method and a stability metric alongside the velocity metric | Our addition; forced by DORA/METR counter-evidence |

**PRIME.AI — Progressive, Role-isolated, Intent-traceable, Model-grounded, Evidenced —
Agentic Engineering.**

The line to say out loud:

> *"We ground the agents in the bank's model, not in the language model."*

And the honest maturity story, which is stronger than pretending v1 never happened:

> *"Version 1 of PRIME.AI was about how we configure agents. That got us a working squad and
> a real result. Version 2 is about what the agents stand on — because that is what decides
> whether this works on ten repositories or on the whole estate."*

---

## 2. The problem, stated the way ING would state it

Not "we want to go faster". The actual problem in a core banking payments transformation:

1. **The estate exceeds any individual's — or any model's — comprehension.** Nobody holds the
   whole payments estate in their head. Neither does an LLM: the context window is a fixed
   container (Sahaj), and beyond it you get compaction, then forgetting, then invention.
2. **Knowledge lives in people and decays.** The engineer who knows why the reconciliation
   job has that exception leaves, and the knowledge leaves with them.
3. **Documentation is stale the moment it is written.** *"The map goes out of date almost as
   fast as you can drive"* (Blitzy).
4. **Deadlines are externally imposed.** Payments regulation does not negotiate. Delivery risk
   is the product being bought.
5. **Every change must be evidenced.** Requirement → code → test → approval → deploy, provable
   to an auditor and a supervisor.
6. **And now: AI accelerates entropy.** *"Bad code is the most expensive it's ever been"*
   (Pocock). Agents pointed at a poorly understood estate generate plausible artefacts fast,
   and the review burden lands on the few people who understand the system.

**Points 1–3 are knowledge problems. Point 5 is a traceability problem. Both are graph
problems.** That is the entire argument for the substrate, and it is stated in ING's terms
rather than ours.

---

## 3. The architecture — seven planes

```
┌────────────────────────────────────────────────────────────────────────────┐
│  P6  GOVERNANCE & EVIDENCE PLANE                                           │
│      agent identity · least privilege · approval gates · policy-as-code    │
│      immutable action log · audit evidence pack · measurement              │
├────────────────────────────────────────────────────────────────────────────┤
│  P5  ORCHESTRATION PLANE  — "the Conductor"                                │
│      state only, never content · dependency graph · parallelism · retry    │
├────────────────────────────────────────────────────────────────────────────┤
│  P4  AGENT FLEET  — thin, role-isolated, disposable contexts               │
│      Comprehend · Specify · Construct · Verify · Operate · Curate · Govern │
├────────────────────────────────────────────────────────────────────────────┤
│  P3  SEMANTIC BRIDGE   business concept ⇄ technical artefact               │
│      "SEPA Instant Credit Transfer" ⇄ services, endpoints, tables, tests   │
├───────────────────────────────┬────────────────────────────────────────────┤
│  P2  BUSINESS ONTOLOGY        │  P1  ESTATE GRAPH (technical ontology)     │
│      BIAN · ISO 20022 · FIBO  │      repos, modules, classes, endpoints,   │
│      capability · product ·   │      tables, topics, tests, pipelines,     │
│      requirement · control    │      work items, defects, releases         │
├───────────────────────────────┴────────────────────────────────────────────┤
│  P0  GROUND TRUTH — deterministic extraction. NO LLM.                      │
│      build introspection · tree-sitter · LSP · dependency analysis ·       │
│      OpenAPI/WSDL · DB schema · topic topology · Git history · ADO ·       │
│      pipeline logs · OTel traces                                           │
└────────────────────────────────────────────────────────────────────────────┘
        ▲                                                             │
        └────────── EXECUTION TRACES (what worked, what didn't) ──────┘
```

Read it bottom-up: **facts, then structure, then meaning, then work, then coordination, then
accountability** — with a feedback loop so the substrate improves with use.

### P0 — Ground truth (no LLM touches this plane)

The single most cost-effective decision in the architecture. Structure is already encoded in
build files, language servers, schemas and manifests; extracting it with a parser is
deterministic, fast, auditable and effectively free compared with tokens.

> *"LLMs read for meaning — not for structure. Structure is already encoded in build files,
> LSP servers, symbol indexes. Don't burn context tokens on work a compiler does for free."*
> — Sahaj

This is also the answer to Hightower's cost critique: **infer once, export, run without
inference.** We pay a language model to decide what something *means*, once; we never pay it
to re-derive what a parser already knows.

### P1 — The Estate Graph (technical ontology)

Everything the delivery organisation actually manipulates, as nodes and edges: repositories,
modules, classes, methods, endpoints, database tables and columns, Kafka/Red Panda topics,
configuration, tests, pipelines, environments, releases, work items, pull requests, commits,
defects, incidents.

Two properties that matter and that a documentation set cannot offer:

- **It composes.** *"Which services participate in the SEPA Instant flow, and which of them
  have no regression coverage?"* is one query against a graph and an impossible question to
  ask of 200 markdown files.
- **It has identity and history.** Nodes persist across regenerations, so *what changed, when,
  and why* is answerable.

### P2 — The Business Ontology (and we do not invent it)

This is the layer neither the current deck nor Sahaj has, and it is where a bank's credibility
is won or lost. The decisive move is **not to author a payments ontology from scratch**, but to
adopt the industry's:

- **BIAN** — service domains and the service landscape for banking capabilities.
- **ISO 20022** — the payments message model (`pacs`, `pain`, `camt`), already mandated across
  SEPA, T2 and CBPR+, so ING's engineers already speak it.
- **FIBO** — financial industry business ontology, for instrument and party concepts.

Saying *"we ground the model in BIAN and ISO 20022"* rather than *"we built an ontology"*
converts the riskiest-sounding part of the proposal into the safest. It is standards adoption,
not a science project — and the vocabulary is one ING's architects already use.

Expressed, per Eifrem, in the language of the business: `Customer` has a `first name`, not
`f_name`.

### P3 — The Semantic Bridge

The join. `SEPA Instant Credit Transfer` → the BIAN service domain → the ING services that
realise it → the endpoints they expose → the tables they write → the topics they publish →
the FSA that specified it → the stories that built it → the tests that prove it → the release
that shipped it → the regulation that requires it.

This single structure serves three audiences that are normally served by three different
efforts:

| Audience | The question it answers |
| --- | --- |
| Engineer | "What breaks if I change this?" |
| Delivery lead | "What is actually left to build for this scheme?" |
| Auditor / supervisor | "Show me the evidence chain for this change." |

**The compliance artefact and the engineering artefact are the same artefact.** That is the
strongest single idea in the pitch, because it converts a governance cost into a delivery asset.

### P4 — The agent fleet, organised by function rather than job title

The current roster is seven generators shaped like the org chart. A fleet of generators with
no independent verifier and no curator produces volume without assurance. Reorganised by what
the work actually requires:

| Family | Purpose | Reads from graph | Writes to graph |
| --- | --- | --- | --- |
| **Comprehend** | Understand the existing estate — the Sahaj capability we currently lack | P0/P1 facts | Structure, boundaries, workflows, domain model |
| **Specify** | Intent → requirement → story → acceptance criteria | P2/P3 business context, precedent stories | Requirements, stories, acceptance criteria, traceability edges |
| **Construct** | Produce the change — code, config, migration, test scaffolding | P3 impact slice, standards, precedent | Proposed change, linked to the story |
| **Verify** | **Independently** check — coverage, contract conformance, regression risk, standards, security | P1/P3 + the proposed change | Findings, evidence, coverage edges |
| **Operate** | Reproduce, triage, root-cause, fix, release | P1 runtime + logs + traces | Defect linkage, RCA, incident→code edges |
| **Curate** | Keep the graph true — freshness, drift, contradiction, orphans | The whole graph | Corrections, confidence scores, decay flags |
| **Govern** | Assemble evidence, enforce policy, report | Action log + traceability | Evidence packs, control attestations |

Two families are new and non-negotiable:

- **Verify must be independent of Construct.** A generator marking its own homework is not a
  control. Different context, different inputs, different agent — this is `role isolation`
  applied where it has audit value.
- **Curate is what makes it "living" rather than a one-off.** Without it we have Sahaj's
  15MB of documents with extra steps, and it goes stale exactly as fast.

### P5 — Orchestration: answer "who watches the workers?"

Sahaj asks the question we currently do not: who decides how many workers spin up, what
happens when a stage fails, what runs in parallel versus what must wait. The Conductor pattern
is the answer and we adopt it directly:

- **State only, never content.** The orchestrator holds *what completed, what failed, what is
  pending* — never code, never documents. Its context stays the leanest in the system, so it
  cannot be poisoned by the material it coordinates.
- **Hub-and-spoke.** State flows in, instructions flow out.
- **Explicit dependency graph**, so parallelism is a property of the plan rather than an
  accident.
- **Failure is a designed state**: retry, replan, or escalate to a human with context preserved.

### P6 — Governance and evidence

The plane the current deck omits entirely, in front of the audience least able to ignore it:

- **Agent identity** — each agent is a first-class, named principal with least-privilege
  credentials. Not a shared service account. Every action attributable.
- **Immutable action log** — what was proposed, by which agent, on which inputs, approved by
  whom, at what time.
- **Approval gates as policy, not convention** — encoded, enforced in pipeline, not a red
  asterisk on a slide.
- **Named human accountability** — a human being approves every change to production. The
  agent proposes; a person owns.
- **Evidence pack generation** — the traceability graph rendered as audit evidence on demand.

---

## 4. The deterministic / cognitive split, published as a design rule

Publishing this table is a credibility move: it shows we know where *not* to use AI, which is
the fastest way to be trusted about where we do.

| SDLC activity | Deterministic tool | LLM agent | Why |
| --- | --- | --- | --- |
| Parse code, resolve symbols, build call graph | ✅ | ❌ | Compilers solved this decades ago |
| Dependency & impact analysis | ✅ | ❌ | Graph traversal, exact, cheap |
| Schema/contract diff, breaking-change detection | ✅ | ❌ | Mechanical and must be exact |
| Lint, format, static analysis, SAST | ✅ | ❌ | Deterministic, already in pipeline |
| Test execution, coverage measurement | ✅ | ❌ | Must be reproducible evidence |
| Traceability link *maintenance* | ✅ | ❌ | Derived from IDs, not judgement |
| Infer *meaning* of legacy code | ❌ | ✅ | Genuinely semantic |
| Requirement → story with acceptance criteria | ❌ | ✅ | Language, ambiguity, judgement |
| Domain/bounded-context boundary proposal | ❌ | ✅ | Judgement — and always human-ratified |
| Write the change | ❌ | ✅ | Synthesis under constraint |
| Test *design* (execution stays deterministic) | ❌ | ✅ | Requires understanding intent |
| Defect root-cause narrative | ❌ | ✅ | Correlation across noisy sources |
| Ontology mapping proposal | ❌ | ✅ | Proposes; human ratifies; graph validates |

**Rule of thumb:** *if a compiler, parser or query could answer it, a language model must not
be asked to.* This is simultaneously the cost story, the accuracy story and the auditability
story — one rule serving three objections.

---

## 5. The neuro-symbolic guardrail (Coyle's contribution, and it is underrated)

The graph is not only retrieval. It is a **validator** — a symbolic check on probabilistic
output. Coyle's examples map disturbingly well onto payments:

| Ontology construct | Catches |
| --- | --- |
| Functional property (at most one) | A second refund against the same payment |
| Disjoint classes | A payout routed to a support representative rather than the beneficiary |
| Enumerated value range | An invented status such as "probably settled" |
| Domain / range constraints | A relationship asserted between incompatible entity types |

An agent proposes; the ontology adjudicates; only then does anything reach a human. *"Pydantic
at the door, ontology at the ledger"* (Coyle). In a payments context these are not academic
examples — they are the class of defect that costs money and attracts a supervisor's attention.

---

## 6. Measurement — replacing the bare percentages

The `~30%` badges must be replaced by a model, because the badges cannot survive their first
serious question. Every metric is reported as a **pair**, so velocity can never be claimed
without stability. This directly pre-empts the DORA finding that AI adoption raises throughput
while degrading delivery stability, and the METR result that perceived speed-up and actual
speed-up diverge.

| Dimension | Velocity metric | Paired stability metric |
| --- | --- | --- |
| Flow | Lead time for change; cycle time per story | Change failure rate |
| Quality | Defect detection in-sprint | Defect escape rate to ST/SIT/prod |
| Rework | First-time-right rate on PRs | Code churn / rework within 21 days |
| Coverage | Coverage delta | Mutation score or assertion quality |
| Review | Review turnaround | Review depth; % changes materially amended |
| Comprehension | Onboarding time to first merged PR | Graph freshness and coverage of the estate |
| Cost | Cost per story | Token + tooling cost per accepted change |

Every reported number states **baseline · method · population · period**. Bare percentages are
prohibited.

Include the counter-evidence deliberately and on a main slide, not in the appendix. Naming the
strongest contrary finding before the client does converts the most dangerous question in the
room into a demonstration of rigour.

---

## 7. Honest economics — when *not* to build this

Copied from Sahaj's most trust-building slide, because it costs nothing and buys a great deal.

**Build the full substrate when:** the estate exceeds individual comprehension; multiple squads
and multiple years are involved; the same questions are asked repeatedly by different people;
traceability must be evidenced to a supervisor; the system will be decomposed or migrated.

**Do not build it when:** the scope is a handful of well-understood repositories; the work is
genuinely greenfield; the team already holds the model in its head and turnover is low; the
programme ends before the substrate would pay back.

> *"Respect the economics. Match the instrument to the problem."* — Sahaj

Saying this out loud is what separates a partner from a vendor, and it makes every other claim
in the deck more believable.

---

## 8. Adoption path — four steps, each independently valuable

Designed so nothing depends on a big-bang commitment and every step ships something usable.

| Step | What is built | What ING gets | Proves |
| --- | --- | --- | --- |
| **1. Map** | P0 + P1 for the payments stream — deterministic extraction only | A queryable map of the stream: dependencies, endpoints, tables, topics, coverage gaps | The substrate is real and cheap; no LLM risk |
| **2. Mean** | P2 + P3 — BIAN/ISO 20022 grounding and the business↔technical bridge | "Show me everything that implements SEPA Instant, and its test evidence" | The business layer is standards-based, not invented |
| **3. Work** | P4 + P5 — the existing seven agents re-pointed at the graph, plus Verify and Curate; the Conductor | Same agents, better grounded; independent verification; the map stays current | Grounding measurably improves output |
| **4. Govern & scale** | P6, then extend beyond payments | Evidence packs on demand; a substrate reusable by every squad | It is an asset, not a project |

The sequencing matters commercially: **step 1 has no AI risk at all**, which makes it the
easiest thing a bank has ever been asked to approve, and it produces the artefact that makes
every later step cheaper.

---

## 9. What we are deliberately *not* claiming

The list that makes the rest believable:

- Not claiming agents write production payment logic unsupervised. A human approves every
  change.
- Not claiming a percentage of code is "AI-written". That framing invites a supervisory
  question with no comfortable answer.
- Not claiming the ontology is complete. It covers the payments stream and grows by use.
- Not claiming AI makes every engineer faster. The independent evidence says otherwise for
  unfamiliar codebases — which is precisely the condition the substrate is built to remove.
- Not claiming this removes the need for engineering judgement. It relocates it: from typing
  to designing, reviewing and deciding.

---

## 10. Open questions to resolve with the client

`[ASSUMPTION — validate with client]` on all of the following:

1. Which graph technology is permitted in ING's approved estate?
2. Where can source-code-derived artefacts be processed and stored, and under which
   model-hosting arrangement?
3. Does ING already hold a BIAN or ISO 20022 aligned service catalogue we should adopt rather
   than derive?
4. What is the actual baseline for the 30% claim — which sprints, which stories, which
   definition of done?
5. Who would own the substrate after the engagement? An asset with no owner becomes a liability.
6. What existing controls apply to non-human actors in the pipeline today?
