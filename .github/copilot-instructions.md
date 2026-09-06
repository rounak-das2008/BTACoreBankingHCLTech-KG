# Workspace: HCLTech × ING — Core Banking BTA Knowledge Graph & Agent Architecture

## What this workspace is

This is a **research and pitch-authoring workspace**, not a software project. There is no
application to build, test, or deploy. The deliverable is a *business-level pitch deck*
backed by a *research-grade evidence dossier*.

**Audience of the deliverable:** ING Bank leadership (business + technology). The deck must
be understandable by non-technical executives, while the research behind it must be deep
enough that the presenter survives hostile technical questioning.

**Subject:** `PRIME.AI` — HCLTech's methodology for applying AI agents across the complete
SDLC on ING's Core Banking / BTA Payments programme, with a **knowledge graph / ontology
semantic layer** as the central technical thesis.

## Non-negotiable working rules

1. **Every factual claim carries a citation.** Inline URL to a primary source. If a claim
   cannot be sourced, it is labelled an assumption or removed. A bank's leadership will
   check numbers. An unsupportable number destroys the whole pitch.
2. **Separate verified fact from inference from aspiration.** Use the labels
   `[VERIFIED]`, `[INFERRED]`, `[ASSUMPTION — validate with client]`. Never present an
   inference about ING's internal estate as fact.
3. **Prefer primary sources**: arXiv papers, standards bodies (BIAN, ISO, EDM Council),
   regulator publications (EU, EBA, ECB, DNB), vendor *engineering* blogs, conference
   talks, annual reports. Deprioritise listicles, SEO content, and vendor marketing.
4. **Vendor marketing must be flagged as such.** Neo4j, Palantir, Microsoft and every SI
   publish self-serving numbers. Mark them. Prefer independent evidence.
5. **Steelman the counter-argument.** Every section that makes a claim must also record the
   strongest objection to it and the honest rebuttal. The METR RCT, DORA's stability
   findings, GitClear's code-quality data and Cognition's "Don't Build Multi-Agents" are
   deliberately kept in scope as counter-evidence.
6. **Do not overclaim.** The methodology must be credible and buildable with the client's
   real stack. Reject anything that reads as science fiction; reject anything that reads as
   a rebranding of what everyone already does.
7. **Everything stays inside this workspace.** No files, config, or state written outside
   this directory. No client material sent to third-party services.

## Client stack (as evidenced by the existing draft deck)

GitHub Copilot custom agents (GHCP) + Anthropic Claude · Azure DevOps (repos, boards,
pipelines) · OpenShift ("BIAB" region) · Red Panda (Kafka-compatible streaming) ·
"Orange Sharing" (SharePoint) · "Forge" (internal developer platform/documentation) ·
"INGenious" (test automation framework) · Teams meeting transcripts · FSA documents
(functional specification/architecture).

Anything about ING beyond this and public record is an assumption to validate.

## Repository layout

| Path | Contents |
| --- | --- |
| `My-prompt.md` | The originating brief from the user. Re-read before major decisions. |
| `HCLTech-ppt-screenshots/` | The existing draft deck (7 slides) being replaced. |
| `sahaj-software-ppt-and-desc/` | Competitor/peer talk being analysed and superseded. |
| `other-sources.md` | Source video list. |
| `research/raw/` | Source extracts: transcripts, PDF text, per-thread research dossiers. |
| `research/` | Synthesised dossier, methodology, and deck artefacts. |
| `.github/skills/` | Agent skills available in this workspace. |
| `.venv/` | Local Python venv for extraction tooling. Not a deliverable. |

## Skills available here

Vendored from [`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT, licence
retained at `.github/skills/LICENSE-mattpocock-skills.txt`), chosen because they encode the
same fundamentals this pitch argues for:

- `grilling/` — relentless interviewing to resolve every branch of a design tree. **Use
  this to stress-test the pitch narrative before it goes to the client.**
- `domain-modeling/` — build and sharpen a shared domain model / ubiquitous language.
  Directly relevant: the deck's thesis is that a ubiquitous language belongs in a graph.
- `codebase-design/` — deep modules, small interfaces. The "good code base" argument.
- `research/` — investigate against high-trust primary sources, capture as cited markdown.
- `writing-for-agents/` — how to write documents agents actually read.

Local additions live alongside them and are prefixed `prime-`.

## House style for the deliverables

- Business slides: one idea per slide, a number or a picture, no wall of text. Assume the
  reader is a director who will spend 20 seconds on it.
- Research dossier: dense, cited, sectioned, tables over prose where comparative.
- Never use "revolutionary", "game-changing", "seamlessly", "unlock", "supercharge".
- Prefer concrete nouns from the client's world (payment, FSA, sprint, defect, release)
  over abstract vendor language.
