# Thread E — Conference Talks, Distilled

**Purpose.** Primary-source distillation of six conference talks for the HCLTech → ING
"PRIME.AI" pitch (agentic-AI SDLC for Core Banking / BTA Payments). The dossier thesis
under test: *a knowledge-graph / ontology semantic layer, combined with rigorous context
engineering, is what makes SDLC AI agents work at enterprise scale.* Each talk is
distilled faithfully to its transcript; nothing is invented. Where the source is an
auto-caption with obvious errors, the garble is flagged and the most probable intended
term given in brackets.

**Sources (all in `research/raw/transcripts/`, plus `research/raw/sahaj-deck.txt`):**

| # | Speaker / Org | Title | Venue / channel | Len |
|---|---|---|---|---|
| 1 | Kelsey Hightower | "ZTA: Zero Token Architecture" | PlatformCon 2026 | ~29 min |
| 2 | Matthew + Carly, **Blitzy AI** | "Reverse Engineering Enterprise Codebases at Scale" | Blitzy webinar | ~46 min |
| 3 | Harshad Nawathe, **Sahaj Software** | "The Practical Guide to Reverse Engineering XXL Codebases with Agentic AI" | Hasgeek TV | ~37 min |
| 4 | Frank Coyle, UC Berkeley | "Why Agentic Systems Need Ontologies" | AI Engineer | ~20 min |
| 5 | Emil Eifrem, **Neo4j** | "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer" | AI Engineer | ~11 min |
| 6 | Matt Pocock | "Software Fundamentals Matter More Than Ever" | AI Engineer | ~18 min |

**Caption caveat.** Talks 1–3 are auto-captioned and lightly garbled. Confirmed
substitutions used below: "snake oil" (caption: *stink oil*), "Redis" (*Reddus*),
"ORM" (*an OM*), "Visio" (*Vizio*), "Jira" (*juro*), "Ansible/Chef" (*anore chef*),
"Quora" (*Kora*), "Rube Goldberg" (*R Goldberg*), "web scale" (*webs*); "McKinsey"
(*McKenzie*), "COBOL" (*cobalt*), "SWE-bench" (*swenchro*), "HashiCorp" (*Hashi Cororb*),
"Apollo 11 1202 error" (*122 er error*), "Copilot" (*C-pilot*), "POC" (*a PC*); "Claude
Code" (Pocock caption: *Clojure Code*). Genuinely uncertain terms (e.g. Sahaj's "a
scalar," and the "graphify / GitLab orbit" tool names) are flagged in place.

---

## TALK 1 — Kelsey Hightower, "ZTA: Zero Token Architecture" (PlatformCon 2026)

> This is the sceptical/contrarian keynote the dossier must co-opt. Read at full strength
> it is *not* anti-AI; it is anti-**waste** and pro-**fundamentals**. Most of its argument
> actually reinforces our thesis — but it hands a sharp CTO three real objections.

### Thesis in one sentence
**"Zero token architecture is simply that one sentence: infer once, export, and run
without inference"** — use an LLM's expensive inference *once* to work out the loop/tool,
then export it as deterministic code (library, framework, binary) that runs forever on a
"regular … CPU for pennies," never inferring again until the loop itself must change.

### Full argument structure (the spine)
1. **Framing joke / disclaimer.** "Zero token architecture isn't a thing. Some people
   think it is. Some VCs have even reached out to me. I should have taken their money."
2. **The track-saw parable.** He bought a fancy track saw, watched ~50 hours of YouTube,
   "thought I was a carpenter," moved as fast as he could, and it "jumps off the track …
   a spinning blade at 5[-]10,000 RPMs coming back at you." Punchline: *"that's the way I
   watch a lot of people using AI at the moment."* People think they're platform engineers
   "because they ask [Claude] to deploy a Kubernetes cluster." (Matrix reference: watching
   videos ≠ competence, "I know kung fu … doesn't work in real life.")
3. **The invoice arrives.** The hype wave has reached "burn all the tokens," and now people
   get "this magical thing called the invoice … a really unique piece of technology that
   tells you what things actually cost." $20/month fine; $2,000/month "we start asking
   questions"; *"when the token burn matches your salary, now we're being silly."* People
   now "build amazing products to try to figure out how to reduce token burn … **You're
   probably burning tokens to save tokens.**"
4. **What is an agent?** Audience answer: *"An AI agent is basically a script that does an
   L[L]M call that then forms an action."* Kelsey: "Good enough. He's getting fired next
   week." Coins **"loop engineering."** People brag "I have 15,000 agents"; he replies "that
   looks like a CI/CD pipeline to me." Concedes: *"there is something there. It's not 100%
   [snake] oil."*
5. **The human is the most agentic thing.** Career "software upgrades" (learning to
   program, understanding distributed systems) built "the Kelsey model … Kelsey version 45."
   *"That's the foundation of the zero token architecture … before you start burning tokens,
   I just want you to understand the thing you're trying to do first."* First question:
   *"How good is your software model?"*
6. **Deskilling / codependency.** At conferences he asks "How are you better than you were
   two years ago? Read any new books?" — mostly "no," so "their menu and solution range is
   so small that now they're outsourcing to the LLM." France anecdote: a company revoked
   "unlimited token burn," teams "revolted," couldn't "meet the same demand." *"They became
   codependent"* — like GitHub codependency ("GitHub is down. Everything stops"). "When the
   tokens go away … if that means you can't work anymore, then we have a problem."
7. **The contractor / rewrite trap.** Hire contractors who build from your "vague
   understanding" (aka **"zero tickets"**), they leave, and "the first thing that you all
   tend to do is … rewrite it because you don't understand the current system. This is …
   the foundational root of this problem."
8. **The ORM analogy (knowledge erosion).** "The first time I['ve] seen knowledge erode
   because of tools like an [ORM]." Developers "revolt[ed] that they shall not know how
   databases work," let the ORM map objects to tables, produced "queries that are 10,000
   pages long just to select one column," and DBAs "had to rewrite those queries and
   hardcode them." "I'm seeing the same process being repeated" — agents building database
   tables by inference, in a loop. *"This is a very expensive way to create a table."*
9. **The core move.** *"Why wouldn't you just export the tool that creates the table once
   you use inference to build that thing out?"* Works "for CI/CD processes … generating
   code … pretty much anything that you would want an agent to do once." Then it "can just
   run in the loop without the inference," "burning less tokens to complete the same task."
10. **Prediction.** *"We're going to go from burning tokens in a loop to using tokens only
    once to create the loop and never use inference again until we change the loop. That's …
    the magic stroke that makes this feasible."* Human analogy: "You write code once … we
    turn those into libraries, frameworks, and executable binaries that don't need us to
    rebuild the entire application every time." Payoff line: *"Infer once, export, and run
    without inference … I guarantee you that one sentence is probably going to save your
    company tens of millions of dollars."*

### Q&A (this is where the deeper, dossier-relevant argument lives)
- **Caching is the precedent (30 years).** "The entire industry has already been doing
  this." Expensive DB query → cache in Redis; "the concept of caching is a very core
  computing concept. It's what your CPU is doing … your hard drive … your developers …
  your language designers." Spend up front, reuse the computation, let hardware "optimize
  that loop to remove the unnecessary branches." *"Why are we treating an agent
  differently?"* An agent can "generate a pipeline, generate a function of code," but the
  "generated code should … be stuffed in a library so it can be imported and used thousands
  of times." *"Would you ever pay a developer … to write a database driver from scratch
  every time they ran a SQL query? That would be insane."*
- **Legibility is the real gap.** Questioner: "outdated docs, outdated architecture isn't
  the problem … we never really made our systems legible in the first place." Kelsey calls
  it "a good question." He advises **Mass Driver** (his advisee Corey's company), a tool to
  *visualize* infrastructure. "Everyone wants a platform with one exception … that they
  have to build … themselves."
- **Software is unconstrained → undesigned.** Unlike a building ("codes and the laws of
  physics"), "software engineering, we just do random things." Most enterprise systems
  "w[ere] not designed." **Kafka parable:** "your director went to a big data conference …
  they bought a jar of Kafka sauce and started rubbing it on stuff," and the platform team
  gets "we need Kafka … ASAP" without understanding why, how to integrate, maintain, or
  optimize it. Infrastructure "just organically grow[s] … a manifestation of people coming
  and going, doing ad hoc things." "Instead of reflecting … we decided to allow AI to deal
  with the complexity."
- **Structure makes AI work.** "We move[d] from infrastructure as code to infrastructure
  as data … Kubernetes … a manifest, Terraform. There's now structure to infrastructure.
  So … I'm not surprised that these tools are now … able to make sense of these things."
- **Blueprints & context for humans.** Best companies kept **Visio/CAD** diagrams updated.
  Construction analogy: entering a busy building, "the first thing you're going to ask for
  [is] … a diagram." With a blueprint "you can … look at the whole thing first and say …
  'You all are moving data around. That's what you're doing.'" **Killer line for us:**
  *"If you think context is amazing for agents, wait till you give it to humans."* And the
  warning: *"the mistake the industry is making is … we think AI is going to give us air
  cover for … kick[ing] that can down the road."*
- **Maintenance-first.** "We rarely talk about maintaining things … Start from maintaining
  the system first, work backwards." Are we "happy … on day 300"?
- **Productivity scepticism.** "First thing I ask people that [tout] the productivity thing:
  did you get a raise?" Their public product "typically … doesn't change … where's all the
  productivity going … Are you filling out [Jira] tickets faster? … writing tests that no
  one's ever going to read?"
- **Innovation risk.** Docker parable: for decades we shipped RPMs/deb packages (some "just
  shipping source code … with SCP"), used init/systemd/Ansible/Chef, "brought in Jenkins …
  but we didn't think to change the abstraction not one time." Then Docker: "Make files
  turn into Docker files … you end up with one … the container." *"Fundamentals are at the
  core of innovation."* Models are "a reflection of the past normalized into a model …
  trained [on] every GitHub commit, every question on [Quora]." Fear: does the innovation
  "batting average go down" as we deskill? "Are we stuck with … YAML files … these [Rube]
  Goldberg machines[?] or will one of you … build a better substrate that … even the AI
  agent will … operate [on]?"
- **Agents sit on top of your substrate.** *"Most AI agents sit as a layer on top of the
  existing thing. So if you have bad and terrible hard to maintain infrastructure, your
  agent is just going to be sitting there … burn[ing] tokens."*
- **Juniors (his "best question").** Learn the new tools "100%," but "be … [a] historian":
  find "how [people] w[ere] doing this before this tool." He wrote **"Kubernetes the hard
  way"** to "see how everything m[anually] fit together," then reproduced by hand-work in
  YAML, then asked "how does it work … on the actual server … exactly the same thing …
  when I was 18." "Do it manually first by hand step by step … then it's okay to outsource
  it."

### Concrete claims / numbers / tools / analogies (exhaustive)
Track saw @ 5–10,000 RPM; ~50 hrs YouTube; $20 vs $2,000/month vs "matches your salary";
"15,000 agents"; "zero tickets"; ORM "10,000-page" query; Redis cache; infra-as-code →
infra-as-data (Kubernetes manifest, Terraform); Visio/CAD; Mass Driver (advisee Corey);
Kafka "sauce"; Heroku; Docker vs RPM/deb/SCP/init/systemd/Ansible/Chef/Jenkins;
"Kubernetes the hard way"; "three servers … make a trillion dollars … Do not touch
Kubernetes … SSH in[,] the for loop … copy that binary … go on vacation."

### Genuinely novel / contrarian
- **"Infer once, export, run without inference"** as a named cost architecture — reframing
  agentics through the 30-year-old lens of *caching / compilation / library extraction*.
- The **invoice** as the forcing function ("burning tokens to save tokens").
- Naming **codependency / deskilling** and the **innovation batting-average** decline as
  first-order risks, not side effects.

### How it SUPPORTS the KG/ontology + context-engineering thesis
- *Understand-first* and *"how good is your software model?"* = context engineering as a
  human discipline before an agent discipline.
- *"Infer once, export, run without inference"* is precisely the economic case for a
  **knowledge graph as the exported artifact**: pay the expensive LLM pass once to *build*
  the graph/tools; thereafter query deterministically for pennies.
- *"Infrastructure as data … structure to infrastructure"* and the plea for **blueprints**
  = argue for a legible, structured semantic layer that both humans and agents read.
- *"If you think context is amazing for agents, wait till you give it to humans"* is the
  single best line to justify a shared semantic layer that serves engineers *and* agents.

### How it CHALLENGES / complicates the thesis (the CTO's ammunition)
- **"Agents sit as a layer on top … bad infrastructure → just burns tokens."** A KG built
  over an un-designed mess maps the mess; it does not fix architecture. Objection: *don't
  sell a graph as a substitute for actually understanding and re-designing the system.*
- **Codependency / deskilling:** outsourcing comprehension to KG+agents can hollow out the
  bank's own engineers; when the budget (or vendor) goes away, can they still operate?
- **Innovation / "reflection of the past"** — heavy reliance on models trained on the past
  may lower the odds of the bank inventing anything genuinely new.
- **Ongoing token burn:** even a KG-backed agent loop still infers on every query; ZTA asks
  *"can you export the result and stop inferring?"* — a real cost-governance challenge to
  any always-on agentic pattern.

### Transferable ideas for PRIME.AI
Adopt **"infer once, export, run without inference"** as the cost-governance principle:
the KG/index and the reusable analysis "recipes" are the *export*; deterministic queries
are the *run*. Treat the token **invoice** as a first-class KPI. Use the KG to *preserve*
institutional knowledge (a direct antidote to deskilling). Sell **legibility/blueprints
for humans**, not just agent context. Guard against "air cover for kicking the can down
the road" — position the KG as the tool that *forces* design, not one that excuses its
absence.

---

## TALK 2 — Blitzy AI (Matthew + Carly), "Reverse Engineering Enterprise Codebases at Scale"

> A vendor webinar for a commercial platform (Blitzy). Rich on the *problem framing*
> (context, drift, invisible layer) and on numbers, but the mechanism is described at
> marketing altitude and the metrics are self-reported.

### Thesis in one sentence
The barrier to enterprise-AI ROI is **context, not model quality**; Blitzy closes it with
a **dynamic knowledge graph** that ingests entire systems (up to hundreds of millions of
LOC) and feeds specialized agents **just-in-time slices** of that graph — enabling reverse
engineering *and* production-ready modernization at a scale "no single model context window
ever could hold."

### Full argument structure
1. **Data hook (McKinsey State of AI, end-2025):** ~**88%** of companies use AI in ≥1
   business function, but only ~**39%** see bottom-line earnings impact. McKinsey calls it
   a **workflow** problem: "layering AI on top of existing workflows is not … their
   recommendation"; rethink the workflow with AI in mind.
2. **The gap is context, not the model.** Generic copilots "don't … have that context of
   your system, your constraints or existing code." *"The gap isn't the model … It's the
   context. And context is the thesis for everything."* Example of the gap: "The 30-year-old
   business rule written in [COBOL] buried in a function nobody touched because the person
   who wrote it left the company a very long time ago."
3. **The invisible layer.** Beyond documented code: "forgotten legacy code … undocumented
   dependencies … hidden business logic … actual rules … buried inside conditional
   statements with zero documentation." Source of "security gaps, outages, and risky
   changes." *"You can't protect yourself from what you can't see, and you … cannot
   modernize it if you don't have context around it."*
4. **Why manual fails — drift.** Year 1: read code line by line, "track[] down who's ever
   still around." Year 2: notes "already … drift[ed]" while new code keeps being written.
   Long term: "most of what you've documented is stale again … you … map[] a moving target
   and the map goes out of date almost as fast as you can drive."
5. **War story (Carly, AWS).** A modernization initiative on **~50 million lines of code**,
   scoped at **~14 months**, that "eventually needed to be expanded to two years"; drift was
   visible after finishing even a single subtask. Matthew: **15 years** in software/cloud,
   also at an insurance company and **HashiCorp**; "most of the time isn't spent building …
   [it's] trying to understand the code … well enough to trust that you're not going to
   break something critical." *"It wasn't a technical problem … it was really a cognitive
   one."*
6. **The dynamic knowledge graph.** Ingest "source code, the business logic, and … decades
   of institutional knowledge … into one single connected graph" that you "could actually
   query" and that "stayed current automatically." "A living map of the system that updates
   itself," at **"infinite context."**
7. **Mechanics — three steps to beat the finite window.** "Never asking any one model to
   hold the whole system in its head at once." (1) An **orchestrator** reads the request,
   "breaks it into discrete tasks," decides which specialized agent is needed. (2) Each
   agent is "pulled in just a **slice** of the knowledge graph it actually needs — call
   chain … dependencies … the specific business rules relevant to that task … retrieved in
   real time." (3) Results "get composed back into a single full context window." It "builds
   recursively line by line, dependency by dependency, tracing … until it actually gets
   done, not until it's good enough." Net effect: "the model is always reasoning over your
   whole system … Not just segments, not just chunks, not just samples," yielding
   "production ready code."
8. **Flashlight-in-a-dark-room** (customer, "north of 30 million lines"): before Blitzy it
   was "like being in a pitch black dark room with nothing but a flashlight … you have no
   idea what's three feet to your left." Blitzy is "turning the lights on."
9. **Positioning vs copilots.** Copilot / Cursor / Claude Code are "fantastic … built for a
   different job" (individual dev, individual task). Blitzy is "a completely different
   category," winning on **three** things: **scale** (whole system, millions of LOC),
   **depth** (ingests "business logic, written documentation … institutional knowledge …
   not just syntax"), and **currency** ("updates continuously … the map never … go[es]
   stale"). Concedes: **"other tools build graphs too. That's not unique."** Differentiator
   = graph "at scale where it can understand maybe 10 different projects across dozens of
   repositories that even your own engineers … might not fully know are interacting."

### Concrete claims / numbers / tools (exhaustive, from Q&A too)
- Under the hood: uses **Anthropic, Gemini, OpenAI** models; deploys **specialized agents**
  per ingestion (e.g. "a few million lines of COBOL" → agents that "understand the business
  logic and the structured functions"; ".NET … or legacy database" → other specialized
  agents) that build the graph and map dependencies. "**Four different kinds of agents**"
  split tasks "based upon … the functionality that they touch."
- **Apollo 11 documentation run** (blog "To the Moon and Back," April 8): picked up
  everything "from … references to pop culture in the 1960s … [to] the actual architecture
  logic … [and] the famous … [1202] error codes."
- **Language/framework agnostic** — "any language or any framework," databases, legacy
  frameworks: "We do not care."
- Largest customers = "the largest banks and insurance companies that operate globally,"
  ingesting "tens of millions to hundreds of millions of lines of code."
- **Pricing:** "Blitzy does not … charge … for tokens." Different philosophy: not iterative
  back-and-forth. It **"frontloads the requirements of the [SDLC]"** (business logic,
  business/product requirements) and produces an **"agent action plan"** (a blueprint /
  "the modern way to do a product or code review") *before* it builds; you review, then it
  produces production-ready code you merge to version control.
- **Completion:** "we shoot for 100% … what we see on average is somewhere between **80 to
  90%** … complete autonomous production ready code," justified by "the highest score on
  the [SWE-bench]." The residual 10–20% is the **"last mile"** — blocked by access
  (no CI/CD access, no cloud keys) for compliance/security reasons in banks/insurance.
- **Velocity:** "on average about **5x**"; "at the highest … we've seen things like **30x**."
- **Cloud modernization:** monolith → microservices on EKS/AKS/GKE; ingest constraints
  ("do not mark my S3 bucket … public," "do not … [give] a public IP"); runs unit/QA tests
  autonomously; validates by running tests and returning a pass/fail report.
- **Missing-dependency discovery:** builds a **"technical specification"** (blueprint of
  what the app does) and "document[s] … back to the reviewer … 'this thing is missing …
  I see this file … but I don't see this one'" — possibly an un-ingested repository.
- **Optimal vs suboptimal:** compares against "other … data structures," and ingests your
  NFRs (e.g. "response time under four milliseconds for 99% of the requests") to recommend
  an optimal model and flag suboptimal ones.
- Analogies: **Legos on the floor in a dark room** (recommends moving hazards once "the
  lights go on"). Blogs: "To the Moon and Back: Adventures with Apollo 11"; "A Quick Chat
  with Blitzy" (three codebase experiments); prompting your codebase's "specific voice."
- Sales note: biggest pushback from FDEs/CTOs is *"there's no way you can do this … too
  good to be true"*; converted by a POC — "the proof is in the pudding."

### Genuinely novel / contrarian
- **"Infinite context" via recursive decomposition + JIT graph slices + recomposition** —
  rhetorically the *opposite* of Sahaj's "acknowledge the finite container," but
  mechanically the *same* idea (never load the whole system into one window).
- **Non-token, frontloaded-SDLC pricing** with an **agent-action-plan review gate** before
  any code is written.
- A KG that "stays current automatically" as a first-class product claim against drift.

### How it SUPPORTS the thesis
Blitzy *is* the KG thesis productized: **"context is the thesis,"** the graph ingests
business logic + institutional knowledge (not just syntax) = a fused business/technical
ontology; JIT slices = progressive disclosure; specialized agents + orchestrator = role
isolation + a conductor; documentation/technical-spec outputs = living documentation.

### How it CHALLENGES / complicates the thesis
- **Tension with Sahaj's "never read the code":** Blitzy explicitly "deploy[s] agents that
  … go out and understand the business logic … inside that codebase," i.e. LLM-heavy
  ingestion of raw code to *build* the graph — the opposite of deterministic-first parsing.
  Reconciliation: both converge on *the graph as the durable artifact* and *JIT slices*;
  they differ on **how the graph is built** (LLM ingestion vs deterministic parsing).
- **Vendor black box + self-reported metrics** (80–90%, 5–30x, "highest SWE-bench"): a bank
  CTO will demand independent evidence; "too good to be true" is their own reported reaction.
- **"Stays current automatically"** is asserted, not explained (contrast Sahaj's concrete
  fingerprint/delta mechanism).

### Transferable ideas for PRIME.AI
JIT **graph-slice retrieval per task** (not whole-repo dumps); a **blueprint/agent-action-
plan review gate** before code generation (governance + human-in-the-loop); using the KG
to **surface cross-repo dependencies unknown even to staff** (risk discovery for ING);
**constraint/guardrail ingestion** (compliance as context: private S3, latency SLAs);
explicit **"last-mile" access boundaries** in regulated banks; and the **drift** narrative
("the map goes out of date as fast as you can drive") as the wedge for a *living* KG.

---

## TALK 3 — Harshad Nawathe (Sahaj Software), "Reverse Engineering XXL Codebases with Agentic AI"

> The richest engineering talk and the closest to our methodology. The distillation below
> merges the SPOKEN talk with the slide deck (`sahaj-deck.txt`) and calls out what the
> spoken version adds (war stories, numbers, failures, tool choices, Q&A).

### Thesis in one sentence
Because the LLM context window is a **finite, fragile processing container**, you must
**stop letting agents read raw code**; instead use **deterministic tooling** to build a
structured symbol index / knowledge graph, then run a **multi-layer pipeline of
role-isolated agents** (each seeing only its contract) under an orchestrating **Conductor**,
governed by four context-engineering principles — captured as **APS: Acknowledge, Partition,
Synthesize.**

### The precise problem (spoken war story — March "this year")
A real legacy codebase: **10,000+ files**, "a decade or more" old, "generations of
developers," no current documentation; the ask was to refactor / rewrite / estimate, or
"just … move faster … [with] Claude Code." The naïve **reverse-engineering prompt** (deck,
verbatim opener): *"You are a Principal Engineer specializing in Java platforms,
distributed systems, and modernization. Analyze the repository … to reconstruct the
application's architecture. Identify business domains, bounded contexts, workflows, and the
underlying domain model. Infer entities, aggregates, value objects, relationships, and
ownership boundaries…"* Run on 10,000+ files, "Claude started … reading all of the code
line by line, file by file … compaction occurred … it's inventing new classes … not there
in the code base at all … **very high confidence, but zero accuracy.** That's where you …
lose the ground." Deck: **"Compaction Kills Context … Larger context window? Same problem.
Bigger bucket."** Spoken analogy: *"similar to … saying I will increase the RAM … if my
data set is larger than the main memory. No, you will … hit a limit."*

### The reframe — the two ideas that carry the talk
1. **"What if the agents never read the code?"** Why is the agent reading code? To get
   architecture/integration maps — for which you need the **structure**, not the text (you
   otherwise also feed it "import statements … copyright comments … dead code"). *"Your LLM
   is a thinking machine. To take out the structure from a code is not a thinking problem …
   It's a mechanical problem. Your compilers have solved it decades ago. You need a
   parser."*
2. **Deterministic grounding (deck):** *"Cognitive tasks → LLM agents … Deterministic tasks
   → purpose-built tools … LLMs read for meaning — not for structure. Structure is already
   encoded in build files, LSP servers, symbol indexes. Don't burn context tokens on work a
   compiler does for free."* Spoken: "If you are using LLM for the mechanical task … we are
   using [the] most expensive and … fragile resource … for … the cheapest task."

### The pipeline (deck + spoken detail)
- **Layer 0 — Scout.** Build the skeleton "before anyone reads a line of code." Reads
  **build files only** (`pom.xml`, `build.gradle`, `package.json`); the codebase was
  **Spring (not Spring Boot)** with **Maven** poms. Tools: build-tool introspection, glob
  for module sizing. Produces project-skeleton JSON + module-summary markdown (module
  registry, inter-module dependencies, per-module stats). **Reads code? Never.**
- **Layer 1 — Cartographers** (a *swarm*). "Map every symbol in every file … build the
  static relationship graph." Reads Scout output. Tools: **LSP servers, symbol indexers,
  dependency analyzers** — used **JDTLS** [Eclipse JDT Language Server]; "Cl[aude] can latch
  to it through an MCP." Produces the **symbol index** (classes, methods, interfaces,
  annotations, file paths, incoming/outgoing calls). *"It basically gives you a really good
  knowledge graph."* Output: JSON + CSV (index) and markdown (humans). **Reads code? Never —
  only tool output.**
- **Layer 2 — Specialists.** "Extract domain knowledge from the map." Reads the symbol
  index; **surgical reads only** ("targeted, bounded, intentional" — they "know what part
  of the code they want to read," never sweep). Named agents: **Archaeologist** (excavate
  the buried domain model — find `@Entity` classes via the index and go straight to them),
  **Taxonomist** (classify services / entities / gateways / layers), **BeanStalkJack**
  (trace Spring bean wiring & DI from Spring config files). Produces entity models, bean
  graphs, concept taxonomies, entity→table mappings, domain-model docs. *Honest aside:* the
  bean job "could have been done in a deterministic way if this was … Spring Boot" (dump the
  application context); "we chose to use LLM for it. Maybe there could have been a better
  strategy."
- **Layer 3 — Surveyors.** "Map the boundaries … how the system moves." Reads all Layer-2
  artifacts + symbol index; surgical reads. Agents: **Port Mapper** (inbound/outbound
  integration points — REST controllers, `RestTemplate`/outgoing HTTP clients, Kafka
  template), **Surveyor** (service/module boundary lines — the inherited code "did not
  contain clear separation" between customer/cart/product, so the Surveyor *derived the
  functional domains* for future microservice decomposition), **Choreographer** (runtime
  workflows, call sequences, transactional boundaries). Produces service-boundary maps,
  integration topology, workflow graphs.
- **Layer 4 — Chronicler.** Synthesize Layers 0–3 into "the definitive domain
  documentation." **Code access: None — never reads code.** Produces architecture, domain
  model, service topology, integration map, workflow catalog — **plus a module-wise
  `CLAUDE.md`** ("much better" than `claude init`'s output) and **onboarding guides**
  ("I want to add a new … [endpoint], where should I go").
- **Contracts.** Every stage output is **immutable**; "no stage is allowed to … change the
  output of the previous stage"; each agent is "only aware of the contract" and its folder —
  i.e. isolation by construction.

### Orchestration — the Conductor
Deck's "Who Watches the Workers?": who decides how many Cartographers, what happens on
failure, what runs in parallel vs waits. The **Conductor** coordinates all layers as a
**hub-and-spoke** system — **hub = pipeline state** (central), **spokes = isolated agents**;
"state flows in, instructions flow out." It reads **pipeline state only** (completed /
failed / pending), decides **scale**, handles **failures** ("retry, replan, or escalate
with context preserved"), maintains the **dependency graph**, and has "**the leanest
[context] in the entire system — state only, no content.**" It "orchestrat[es] everything,
[but] it's not actually executing anything." → a **resumable** pipeline.

### Principles of Context Engineering (deck, verbatim — slide-ready)
- **Progressive Disclosure** — "Reveal information … strictly as [the] role requires.
  **Structure before content. Boundaries before reads.**"
- **Deterministic Grounding** — "fast, deterministic tooling for structural work. Reserve
  LLM context exclusively for semantic reasoning."
- **Role Isolation** — "One agent, one competency, one narrow context. **Specialisation
  eliminates hallucination and instruction drift[].**"
- **Subagent Isolation** — "Delegate cognitive tasks to disposable subagent contexts. Keep
  the orchestration layer uncontaminated."

Deck also names the **Four Perils of Context Overload**: **Context Contamination**
("Irrelevant tokens corrupt reasoning quality"), **Low Signal-to-Noise Ratio**, **Lost in
the Middle** ("Facts buried deep … get silently ignored"), **Attention Dilution**. And the
**APS** macro-structure — *Constraints Dictate Architecture* ("In-memory algorithms assume
unbounded resources … Sufficient scale forces a pivot: local computation → systemic
coordination"; opened with a `std::sort` slide).

### What the pipeline produced (deck + spoken numbers — exhaustive)
- **Reusable Index — 10,000+ classes and methods**, queryable on demand.
- **Documentation Artifacts — 200+ documents (~15 MB)**, generated from current code.
- **Data Layer — 400+ database tables** mapped to entity classes.
- **API Catalog — 80+ REST and 60+ SOAP endpoints**, fully indexed.
- **Service Boundaries — 15+** identified/documented, ready for decomposition.
- **Workflow Library — 80+ workflow traces** with sequence diagrams.
- **Architecture — C4 diagrams at three levels of detail.**
- **Incremental** — "input fingerprints tracked; only changed artifacts are regenerated" →
  a **living, resumable database**, delta-driven.

### Lessons from production (deck + spoken war stories)
- **Validate early.** *"Trust in generated documentation must be earned, not assumed."*
  Don't dump 200 docs on a team; validate **each stage** with the developers/product owners
  who own that area and tune stage by stage.
- **Evolve the tools.** *The LSP failure:* LSP is a per-file **service**; at "50 … to 100
  milliseconds" per call × 10,000 files the pipeline was "very very slow." "In [an] IDE you
  work on a single file … here you're working on 10,000 files." They replaced LSP with a
  **tree-sitter** parser (multiple Python-process instances) that produced the same symbol
  index / AST in **~10 seconds**. Because the inter-stage **contracts** were structured,
  swapping the Cartographer core "did not [affect] the specialist layer at all."
- **Evolve freely.** "Decoupled layers evolve independently. The contract … is the only
  thing that must be honoured."
- **Respect the economics.** The KG was great for a **blast-radius check** (call graph →
  infer blast radius of a change), but when they tried to use it to *replace Claude's
  grep/glob* it was **slower than grep/glob**. "Match the instrument to the problem. The
  full pipeline justifies its cost only when a holistic view is needed."

### Q&A — what the spoken talk adds beyond the deck
- **Dead code.** Hard under static analysis; the app had many **feature toggles** (a
  "highly customizable application," switches flipped per client). They "creat[ed] a library
  of … feature toggles" and, via the call graph, could reason about conditionally reachable
  code. Mooted (not built) a **"pathologist"** agent for code smells / unreachable
  methods/classes, and a **"historian"** agent (code history / churn via telemetry & logs) —
  skipped because "our focus was … functional decomposition, not … tech due diligence."
- **"Why not just give the whole thing to one agent to spin up sub-agents?"** In March,
  "Claude wasn't … creating explorer agents … unless you ask it"; now it does ("let me spin
  up [an] explorer agent"). **But** you must supply the **"recipes"** for anything bespoke:
  "how you process a spring bean graph," SOAP endpoints, "a home-grown middleware … this
  middleware works like this," and **Apache Camel routes**. *"We cannot fully rely on this
  one because then we don't get that deterministic output."* They only discovered the Camel
  gap because the KG "was not able to find a path" for a known-solved defect; a developer
  showed the file was "connected through a camel route," so they "added one more recipe."
  (The interviewer likens a recipe to "a scalar" [caption unclear — probably "a skill" /
  reusable capability]; Harshad agrees.)
- **"Isn't Layers 0–1 just long pre-processing?"** Yes originally, but tree-sitter made it
  "pretty fast." He then name-checks the emerging tool landscape converging on the same
  idea: **"GitLab orbit"** [uncertain product name] which "creates a DuckDB-based index …
  and … semantic search," plus **"graphify"** [uncertain], **Serena MCP**, and "codebase
  memory" — "all … pointing to the same thing … a queryable … knowledge graph which can be
  queried and enriched into the next level."

### Genuinely novel / contrarian
- **"What if the agents never read the code?"** — a deliberate inversion that most of the
  market violates.
- Treating the **context window as a finite processing container** and borrowing
  **external-sort / big-data** thinking (APS) for agent design.
- A concrete, named **role-isolated agent cast** (Scout, Cartographers, Archaeologist,
  Taxonomist, BeanStalkJack, Port Mapper, Surveyor, Choreographer, Chronicler, Conductor)
  bound by **immutable contracts** that make tools hot-swappable.

### How it SUPPORTS the thesis
This is the KG/ontology + context-engineering thesis rendered as an engineering blueprint:
build a **symbol index / knowledge graph deterministically**; derive a **DDD domain model**
(entities, aggregates, bounded contexts); never contaminate context; role-isolate agents;
orchestrate. *"It basically gives you a really good knowledge graph."* Deterministic
grounding is a neuro-symbolic split in practice (structure from compilers, meaning from the
LLM).

### How it CHALLENGES / complicates the thesis
- **"Respect the economics"** — the KG was *slower than grep/glob* for some tasks; the full
  pipeline "justifies its cost only when a holistic view is needed." A KG is not the right
  instrument for everything (echoes Hightower).
- **Bespoke recipes are unavoidable** — home-grown middleware, SOAP, Camel routes needed
  hand-written recipes; the pipeline is *not* turnkey. For ING's bespoke core-banking stack
  this is a real, recurring engineering cost.
- **The ideal is not always reached** — they used an LLM for Spring beans where a
  deterministic dump was possible ("maybe there could have been a better strategy").
- **Trust must be earned** — generated documentation needs stage-by-stage human validation.

### Transferable ideas for PRIME.AI
The **5-layer pipeline + Conductor** is a ready reference architecture. Adopt the **four
context-engineering principles** and **four perils** verbatim as slide content. **Build the
index with tree-sitter/LSP; never sweep code.** Use **immutable inter-stage contracts** so
tools stay swappable. Ship a **living, delta/fingerprint-based KG**. Institutionalize
**validate-early** governance. Reuse the **blast-radius check** as a bank-grade
change-risk control. Keep **feature-toggle libraries**, **pathologist** (dead code) and
**historian** (churn) as roadmap agents. Track the converging tool ecosystem (JDTLS,
tree-sitter, DuckDB code indexes, Serena MCP, "codebase memory").

---

## TALK 4 — Frank Coyle, "Why Agentic Systems Need Ontologies" (AI Engineer)

### Thesis in one sentence
Probabilistic LLM agents-in-loops need an **ontology / knowledge graph as a neuro-symbolic
validator and guardrail** that keeps their output "on track" and "honest."

### Argument spine & concrete content
- **Two lineages.** *Agents* (McCarthy, Selfridge, Minsky's "Society of Mind"; "AI" coined
  1956; agent = "perceive … decide … act"). *Ontologies* (Aristotle's "categories of being";
  W.V.O. Quine; **Gruber, 1993: "a formal specification of a shared conceptualization"** —
  "that's what we want to give to our agents … our conceptualization of our domains").
- **Neuro-symbolic convergence.** Probabilistic LLMs + formal ontologies = **neuro-symbolic
  AI**. *"Neuro-symbolic AI … represents a way to keep the LLM on its guardrails, because
  LLMs are by nature probabilistic."* On hallucination: *"that's the feature … We imagine
  things that may not exist, and then we turn them into reality."*
- **Ontology basics.** Entities + relationships + properties; graph DBs beat relational
  "because … [relational was] too restrictive" (add a column → redo the structure) — with a
  graph "you can just attach another … property … relationship." Build **top-down** (experts
  define purchase orders, customers, reps — like 1980s **expert systems**, which "**couldn't
  scale**" → AI winter) or **bottom-up** (from data). Reuse existing taxonomies: **schema.org,
  FOAF, Dublin Core**; **Wikipedia is based on DBpedia.**
- **Reasoning technologies (sit "to the side of your graph").** **RDFS** domain/range
  (teaches has domain *teacher* → "Bob teaches Scooter" infers Bob is a teacher; "all
  teachers are persons" → Bob is a person; range *student* → Scooter is a student). **OWL**
  transitive property (ancestor) and **functional property** ("only one" — has father/mother;
  can imply two labels are the same individual, or act as a **constraint**).
- **Loops.** Böhm–Jacopini (1966): sequence + conditional + loop ⇒ **Turing complete**;
  agents now have loops. *Dangers:* loops "can break" (infinite loop), "can **drift**" (as
  agents talk to each other, "go off the rails"), and "can **cost you money**" ("token
  counts crank up"). "We are … going back to the world of expert systems."
- **The Claude code example (the crux).** `while True`; the LLM is given a model + prompt +
  a **tool**. *"LLMs can't do anything. All they can do is give us the next word with a high
  probability."* The LLM returns `stop_reason = tool_use` and the tool's parameters; you
  execute the tool. **In the RED zone (his slide): after the tool runs, feed the result to a
  validator that "operat[es] with … ontologies about our domain," to decide "whether the
  response of the LLM is reasonable"** — if reasonable, proceed; if not, "go back to the LLM
  … or get a human in the loop." *"Surround the input with checks."*
- **Typing + no side effects.** **Pydantic** adds types at the boundary ("Pydantic at the
  door, ontology at the ledger"); agents "should try to have no side effects" — validate
  through the ontology *before* touching the database.
- **Banking-shaped catches (OWL).** "A **second refund on the same order** is a problem";
  "a payout sent to the **support desk instead of the buyer**" (OWL **disjoint** — customer
  vs support rep are separate entities); a **made-up status** like "probably shipped"
  (constrain status to paid/shipped/refunded). "Very tricky to do that in … English."
- Closes on his teaching credo (Sister Corita Kent / John Cage): *"Nothing is a mistake.
  There is no win … no fail. There's only make."*

### Novelty, support, challenge, transfer
**Novel/contrarian:** hallucination-as-feature; ontology as a *reasoner/validator* in the
agent loop rather than as passive metadata. **Supports** the thesis directly — the ontology
is the neuro-symbolic guardrail, and its example violations (double refund, wrong payee,
invalid status) are exactly the payments-compliance checks ING cares about; "shared
conceptualization" is the same shared language Pocock and Eifrem describe. **Challenges:**
his own history lesson — top-down expert systems "couldn't scale"; a hand-built ontology can
ossify, so the graph must be maintainable/evolvable; and loops "cost money." **Transfer:**
a **neuro-symbolic validation layer** over agent output; **OWL/RDFS constraints as
executable compliance rules**; **Pydantic-typed boundaries**; **no-side-effects-until-
validated**; reuse of standard taxonomies (for banking, the analogue is FIBO — not named by
Coyle but implied by his schema.org argument).

---

## TALK 5 — Emil Eifrem (Neo4j), "Thinner Agents on a Smarter Substrate"

### Thesis in one sentence
Stop building **thick agents with data sources wired in by hand**; instead put **thin agents
on a smarter shared ontology-based semantic layer** built from **three pillars — a
business ontology, a technical ontology, and execution traces.**

### Argument spine & concrete content
- **Motivating example = a bank.** An agent that automates **opening a bank account**. Two
  parts: **business logic** (interpret intent → plan/act loop) and **data sources**. To
  "validate identity" it wires up two sources — the **DMV registry** and a **passport
  verification service.** It works — but as many teams build many such agents, **four
  problems** appear: (1) every team re-discovers where data lives (a startup has "one
  Postgres"; an enterprise has "a hundred databases … Snowflake and Databricks … S3
  buckets"); (2) duplication → "Is it the right … version? Can I trust it? Am I allowed to
  access it?"; (3) violates **DRY** — changes force manual rewiring of every agent; (4) **no
  learning** — "when your agent wakes up tomorrow, it's not smarter," and "no cross-agent
  learning," because the wiring is "encoded in … code and prompts."
- **The markdown line (the one the dossier flagged).** *"Markdown files, skills to the
  rescue. And yes and no … it is **part of the solution, but it is not the solution**."*
  Quotes **Swyx** (Latent Space): "you got to learn your databases. You cannot vibe code
  with just markdown files." Proof points: "a **Fortune 20 global bank**, a massive … Bay
  Area … tech platform company, and a leading fintech."
- **The three pillars.** (1) **Business-facing ontology** — the org's key concepts
  ("customers, accounts, debit cards, checks, transactions") and relationships, "expressed
  in a way that makes sense to all the human beings" ("you don't say `if_name` … you have a
  customer and they have a `first name`"). (2) **Technical ontology** — metadata of every
  data source/asset ("14 Oracle databases … 15 Neo4j databases … Snowflake … Databricks …
  S3 … schemas"), **plus a mapping** to the business ontology (customer's `first name` →
  system of record → Oracle column `F_name`). (3) **Execution traces / runtime signals** —
  as agents "walk this graph and … execute, they leave … traces … What have I tried? Was I
  successful? … the execution traces," yielding a **score** used to bias future choices
  ("very successful using the DMV lookup … more likely to choose [it] … in the right
  context").
- **The account-opening graph.** A **process-guided agent** follows a business process
  encoded in the ontology; at the "check compliance" node it flips to the technical ontology
  — "resolve a government issued ID" → two data sources (motor-vehicle records, passport
  verification) — and leaves execution traces that "lead[] out to some kind of a score."
- **Payoff.** The three pillars solve all four problems: easy discovery; trust
  (**top-down** human curation **+ bottom-up** execution traces — "what actually worked in
  reality"); a **single governed place** mapping intent → sources (DRY); and **self-learning
  within and across agents.** "**Thin agents on top of a smarter shared substrate … a ton
  more agents without having to re-engineer them every time.**" (Graph track name-drops JP
  Morgan Chase, Gates Foundation, monday.com, NYT, Berkeley.)

### Novelty, support, challenge, transfer
**Novel:** the crisp **three-pillar** decomposition and the idea that **execution traces
make the substrate self-improving** (bottom-up trust to complement top-down curation).
**Supports** the thesis most directly of all six talks — this *is* the KG/ontology semantic
layer, in a banking example that maps almost 1:1 onto ING (account opening, compliance,
government-ID resolution, Oracle systems of record). **Challenges:** it is a Neo4j vendor
view; the genuinely hard part — *constructing and maintaining the technical ontology across
100+ heterogeneous sources* — is explicitly deferred ("three key ways … not in this talk"),
and trace-based self-learning is nascent. **Transfer:** adopt the **three-pillar substrate**
as PRIME.AI's core; build the **business↔technical mapping** (the `F_name` pattern) as the
bridge from ING's domain language to its systems of record; treat **execution traces as a
scored learning loop**; use **process-guided agents** that follow an encoded business
process; enforce **DRY governance** and **dual (top-down + bottom-up) trust**.

---

## TALK 6 — Matt Pocock, "Software Fundamentals Matter More Than Ever" (AI Engineer)

### Thesis in one sentence
Because "**AI in a good code base … does really, really well**" and drowns in a bad one,
**bad code is now the most expensive it has ever been** — so software fundamentals (design,
shared language, testing, modularity) matter *more* than ever, not less.

### Argument spine & concrete content
- **Against specs-to-code.** The specs-to-code movement says "change the spec, not the code …
  run the compiler again." He tried it: "I kept running the compiler … and I would just end
  up with garbage … **vibe coding by another name**." Grounds it in **Ousterhout, *A
  Philosophy of Software Design*** ("Complexity is anything … that makes it hard to
  understand and modify the system"; good code bases are "easy to change") and **The
  Pragmatic Programmer**'s **software entropy** ("every time you make a change … not thinking
  about the design of the whole system, your code base is going to get worse").
- **"Code is cheap" is wrong.** *"Bad code is the most expensive it's ever been."* → *"good
  code bases matter more than ever, which means software fundamentals matter more than ever.
  That's the thesis."*
- **Five failure modes → five skills** (repo `mattpocock/…skills`; the "Grill Me" skill
  "has like 13,000 stars"):
  1. **"AI didn't do what I wanted."** Pragmatic Programmer: "no one knows exactly what they
     want"; Brooks's *Design of Design* **"design concept"** — "the invisible … theory of
     what you're building," which is **"not an asset … not something you can put in a
     markdown file."** Skill **"Grill Me"**: *"Interview me relentlessly about every aspect
     of this plan until we reach a shared understanding. Walk down each branch of the design
     tree … resolving dependencies between decisions one by one."* Produces a PRD / issues;
     "better than … default plan mode."
  2. **"AI is too verbose."** Analogy: working with a domain expert (microchips) requires a
     **shared language**. **Domain-Driven Design → ubiquitous language:** "conversations
     among developers, and expressions of the code, and conversations with domain experts
     are all derived from the same domain model … essentially a **markdown file full of …
     terms that you and the AI have in common**." Skill scans the codebase and generates the
     ubiquitous-language markdown (tables of terminology); kept open during planning; "allows
     the AI to think in a less verbose way."
  3. **"It doesn't work."** Feedback loops: static types ("if you're not using TypeScript …
     that's crazy"), browser access, automated tests. LLMs use them badly — "**outrunning
     your headlights** … the rate of feedback is your speed limit." Skill: **TDD** (test →
     pass → refactor).
  4. **Testable = well-designed.** Ousterhout **deep modules** ("lots of functionality
     hidden behind a simple interface") vs **shallow modules** ("tiny … blobs" AI loves to
     create and then "doesn't understand"). Skill: **improve-codebase-architecture** — wrap
     related code in deep modules; "test at the interface."
  5. **"Your brain can't keep up."** Treat deep modules as **gray boxes**: *"Design the
     interface, delegate the implementation"* (not for finance/critical paths). Modules must
     be "part of our ubiquitous language" and named in the PRD. **Kent Beck: "Invest in the
     design of the system every day."** specs-to-code "**divest[s]**" from design.
- **Closing frame.** AI is "a really great on-the-ground programmer, a tactical programmer,
  a sergeant on the ground … you need someone … thinking on the strategic level. And that's
  you."

### Novelty, support, challenge, transfer
**Novel:** repackaging Ousterhout/Brooks/Beck/Pragmatic-Programmer as **AI-enablement
tooling** (skills), and the sharp claim that AI *raises* the price of bad code. **Supports**
the thesis: **ubiquitous language = a shared, business-facing vocabulary between humans,
code and AI** (a lightweight business ontology); **deep modules/boundaries = the legible
structure** agents must navigate (Sahaj's "structure before content," Hightower's
legibility). **Challenges/complicates:** Pocock's remedy is **markdown + good architecture,
not a formal graph** — he is the "markdown camp" that Eifrem calls "part of the solution but
not the solution." Crucially, though, his **"design concept … not something you can put in a
markdown file"** *agrees* with Eifrem that files alone are insufficient — the shared
understanding is richer than any document. **Transfer:** ship a **ubiquitous-language
artifact** as the human-readable projection of the ING ontology; enforce **deep-module
boundaries** so agents (and the KG) have clean interfaces; use a **Grill-Me interrogation
step** to build a shared "design concept" before any agent action plan; keep humans as the
**strategic layer** above tactical agents.

---

## CONVERGENT FINDINGS ACROSS ALL SOURCES — the shared intellectual spine

Six speakers from very different vantage points (a platform-engineering contrarian, two
reverse-engineering practitioners, a graph-DB CEO, a Berkeley ontologist, and a
fundamentals teacher) converge on one architecture. The agreements are strong enough to
form the spine of the PRIME.AI narrative; the two disagreements are narrow and reconcilable.

**1. Context — not the model — is the bottleneck.** Blitzy states it outright ("the gap
isn't the model … it's the context … context is the thesis"); Sahaj makes context a finite
container to be engineered; Eifrem makes the substrate the product; Pocock makes the
codebase the multiplier ("AI in a good code base does really, really well"); Coyle makes the
ontology the guardrail; and Hightower delivers the line that unifies them — *"if you think
context is amazing for agents, wait till you give it to humans."* **Model choice is a
commodity; context engineering is the differentiator.**

**2. The context window is finite and fragile → never dump raw material; disclose
progressively.** Sahaj's "Compaction Kills Context / Bigger bucket" and "Four Perils"
(contamination, low signal-to-noise, lost-in-the-middle, attention dilution) are the sharp
version; Blitzy's "never ask any one model to hold the whole system" + JIT slices is the
same idea from the opposite rhetorical pole ("infinite context"); Coyle warns loops "drift"
and "cost money." **Consensus: retrieve the minimal relevant slice, structured, on demand.**

**3. Deterministic grounding / a neuro-symbolic split of labour.** Use deterministic tools
(compilers, parsers, LSP, symbol indexes, graphs, types, ontologies) for **structure**, and
reserve the LLM for **meaning**. Sahaj: "LLMs read for meaning — not for structure … don't
burn context tokens on work a compiler does for free." Coyle: Pydantic types + an ontology
reasoner around a probabilistic core. Hightower: "infer once, export, run without inference"
— pay for reasoning once, run deterministically forever. Even Pocock's static types + TDD
are deterministic feedback around an LLM. **This split is the operational core of the
thesis.**

**4. A knowledge graph / ontology is the substrate that makes agents scale.** Eifrem's
three-pillar semantic layer, Coyle's ontology-as-validator, Sahaj's symbol-index "knowledge
graph," and Blitzy's "dynamic knowledge graph" are four names for one thing; Hightower's
"infrastructure as data … structure to infrastructure" and his demand for blueprints is the
same instinct from a sceptic. Sahaj's Q&A shows an entire tool ecosystem converging here
(DuckDB code indexes, Serena MCP, "codebase memory"). **The KG is the exported, queryable,
living representation of the system.**

**5. A shared, business-facing "ubiquitous language."** Gruber's ontology = "a formal
specification of a **shared** conceptualization" (Coyle); Eifrem's business ontology
("customer … `first name`, not `if_name`"); Pocock's DDD ubiquitous language; Sahaj's DDD
domain model (entities, aggregates, bounded contexts); Blitzy "translat[ing] domain
knowledge back … in language that you can understand." **The graph must speak the bank's
language, not the database's.**

**6. Markdown is necessary but not sufficient.** The dossier's prior note is confirmed and
extended. Eifrem: markdown/skills are "part of the solution, but not the solution." Pocock —
usually cast as the markdown champion — actually agrees at the deepest level: the shared
"design concept" is *"not something you can put in a markdown file."* Sahaj found a
module-wise `CLAUDE.md` "very useful" but only as an *output* of the structured pipeline, not
a substitute for it. **Files project the ontology for humans; the governed graph + traces
are the source of truth.**

**7. Thin, role-isolated agents on a smart substrate, coordinated by an orchestrator.**
Sahaj's 5-layer cast + lean, state-only **Conductor** ("role isolation … eliminates
hallucination and instruction drift"); Blitzy's **orchestrator + four specialized agent
types**; Eifrem's **thin agents**; Coyle's **agent + validator** loop. **Specialise the
agents; centralise the state; keep each context narrow.**

**8. Guardrails, validation, and human-in-the-loop on probabilistic output.** Coyle's
ontology reasoner ("keep the LLM … honest," "no side effects" until validated); Sahaj's
"validate early — trust must be earned, not assumed"; Blitzy's **agent-action-plan review
gate** + autonomous test runs; Pocock's TDD/type feedback loops. **Never trust generated
output un-validated; gate it.**

**9. Economics and cost governance are first-class.** Hightower's invoice/ZTA is the loudest,
but Sahaj independently reaches "respect the economics" (the KG was *slower than grep* for
some tasks; the full pipeline "justifies its cost only when a holistic view is needed"),
Coyle notes loops "cost money," and Blitzy built a whole non-token pricing model around the
concern. **Match the instrument to the problem; build expensive artifacts once and reuse
them.**

**10. Fundamentals and design endure; AI is a layer *on top of* your substrate.** Hightower:
"most AI agents sit as a layer on top … bad infrastructure → just burns tokens"; Pocock: AI
is the tactical sergeant, you are the strategist; Sahaj: it is "software engineering first
principles — separation of concerns"; Coyle: we are "going back to … expert systems." **If
the substrate (architecture, ontology, boundaries) is bad, AI amplifies the mess. The KG is
the discipline that makes the substrate good — not an excuse to skip it.**

**11. Legibility & living documentation vs. drift.** Blitzy's "map goes out of date as fast
as you can drive," Sahaj's fingerprint/delta "living database," and Hightower's
"maintain-first, work backwards" all attack the same enemy: **documentation that decays.**
The KG's job is to *stay current automatically.*

### The two genuine tensions — and how to reconcile them for ING
- **"Never read the code" (Sahaj/deterministic) vs. "deploy agents to understand the code"
  (Blitzy/LLM-ingestion).** Reconciliation: both make **the graph the durable artifact** and
  both serve agents **JIT slices**; they differ only on *how the graph is built*. PRIME.AI
  should default to **deterministic construction** (tree-sitter/LSP/AST — cheaper, grounded,
  auditable, ZTA-aligned) and use LLM ingestion only for the genuinely semantic residue
  (buried business rules in COBOL, bespoke middleware) that no parser can recover — exactly
  the "recipes" Sahaj had to hand-write.
- **Markdown camp (Pocock) vs. graph camp (Eifrem).** Reconciliation: **markdown is the
  human-facing projection; the graph + execution traces are the machine-facing source of
  truth.** They are layers of one system, not alternatives.

### The assembled stack for PRIME.AI (what the six talks jointly prescribe)
A **DDD ubiquitous-language / business ontology** (Pocock + Eifrem + Coyle) mapped to a
**technical ontology / symbol-index knowledge graph** built **deterministically** and kept
**living/incremental** (Sahaj + Blitzy), queried by **thin, role-isolated agents** via
**progressive disclosure / JIT slices** under a lean **orchestrator** (Sahaj + Blitzy +
Eifrem), with a **neuro-symbolic validation/guardrail layer and human review gates** over
all probabilistic output (Coyle + Sahaj + Blitzy + Pocock), and a **cost architecture that
infers once and runs deterministically thereafter** (Hightower). Every one of these layers
is asserted, independently, by at least three of the six speakers — which is the strongest
evidence the dossier can offer that the KG/ontology + context-engineering thesis is the
industry's convergent answer, not a single vendor's pitch.

---

## APPENDIX A — Slide-ready quotes (verbatim, attributed)

- **Hightower:** "Infer once, export, and run without inference … I guarantee you that one
  sentence is probably going to save your company tens of millions of dollars."
- **Hightower:** "If you think context is amazing for agents, wait till you give it to
  humans."
- **Hightower:** "Most AI agents sit as a layer on top of the existing thing. So if you have
  bad and terrible hard to maintain infrastructure, your agent is just going to be sitting
  there … burn[ing] tokens."
- **Hightower:** "We think AI is going to give us air cover for … kick[ing] that can down
  the road. And I think it's a drastic mistake."
- **Blitzy (Matthew):** "The gap isn't the model … It's the context. And context is the
  thesis for everything."
- **Blitzy (customer):** "It was like being in a pitch black dark room with nothing but a
  flashlight … you have no idea what's three feet to your left or three feet to your right."
- **Blitzy (Matthew):** "You spend years modernizing and mapping a moving target and the map
  goes out of date almost as fast as you can drive."
- **Sahaj (deck):** "Structure before content. Boundaries before reads."
- **Sahaj (deck):** "Don't burn context tokens on work a compiler does for free."
- **Sahaj:** "Your LLM is a thinking machine. To take out the structure from … code is not a
  thinking problem … It's a mechanical problem. Your compilers have solved it decades ago."
- **Sahaj (deck):** "Trust in generated documentation must be earned, not assumed."
- **Coyle:** "Neuro-symbolic AI … represents a way to keep the LLM on its guardrails."
- **Coyle:** "Pydantic at the door, ontology at the ledger."
- **Eifrem:** "Markdown files, skills to the rescue. And yes and no … it is part of the
  solution, but it is not the solution."
- **Eifrem:** "Thin agents on top of a smarter shared substrate … a ton more agents without
  having to re-engineer them every time."
- **Pocock:** "Bad code is the most expensive it's ever been."
- **Pocock:** "The rate of feedback is your speed limit."
- **Pocock (Kent Beck):** "Invest in the design of the system every day."

## APPENDIX B — Caption-uncertainty log

- **Confidently corrected:** snake oil (*stink oil*), Redis (*Reddus*), ORM (*an OM*), Visio
  (*Vizio*), Jira (*juro*), Ansible/Chef (*anore chef*), Quora (*Kora*), Rube Goldberg
  (*R Goldberg*), web scale (*webs*); McKinsey (*McKenzie*), COBOL (*cobalt*), SWE-bench
  (*swenchro*), HashiCorp (*Hashi Cororb*), Apollo-11 1202 error (*122 er*), Copilot
  (*C-pilot*), POC (*a PC*); Claude Code (Pocock: *Clojure Code*).
- **Genuinely uncertain — do not quote as fact:** Sahaj's "a scalar" (interviewer's term for
  a reusable capability — probably "a skill"); Sahaj's emerging-tool names **"graphify"** and
  **"GitLab orbit"** (the DuckDB-index + semantic-search tool he references as ~1–2 months
  old — product names unverified; **Serena MCP** and "codebase memory" are stated more
  clearly). Pocock's course name ("*Clojure Code for Real Engineers*") is almost certainly a
  provocative "*Vibe/Claude Code for Real Engineers*" but is left as-heard. Blitzy's blog
  dates and the "13,000 stars" (Pocock) figure are speaker-reported, not independently
  verified.
