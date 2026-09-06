---
name: prime-evidence-discipline
description: Enforce research-paper evidence standards on any claim destined for the ING pitch. Use whenever writing, editing, or reviewing a number, a benchmark, a vendor claim, or a statement about ING, and before any artefact is marked ready for the client.
---

# Evidence discipline

The deck will be presented to a systemically important bank. Assume a hostile, numerate
reader who will look up your sources. One unsupportable number discredits every other number
on the page. This skill is the standard every claim must clear.

## The four tiers

Tag every non-obvious claim with its tier. Tags stay in the research dossier; they are
stripped from the client-facing deck, but a claim's tier decides *how it may be phrased*.

| Tier | Meaning | Permitted phrasing on a slide |
| --- | --- | --- |
| **T1 — Independent** | Peer-reviewed paper, RCT, regulator or standards body, audited report | State plainly. Cite. |
| **T2 — Credible but interested** | Vendor engineering blog, conference talk by a practitioner, non-audited industry survey | Attribute in-line: "Neo4j reports…", "In Anthropic's published experience…" |
| **T3 — Our own measurement** | Numbers from the BTA Payments engagement | State the baseline, the method, the period, and the n. Never a bare percentage. |
| **T4 — Inference or design intent** | What we believe will happen; how the target architecture would behave | Must read as intent: "designed to…", "our target is…". Never past tense, never a number. |

**Anything that cannot be assigned a tier does not go on a slide.**

## Rules

1. **No bare percentages.** `~30%` is not a claim, it is a rumour. A T3 number is only
   admissible in the form: *metric, baseline, method, population, period*. If any of the five
   is missing, either recover it or drop the number.
2. **Never mix tiers in one sentence.** "Knowledge graphs cut hallucination and delivered 30%
   faster payments delivery" fuses a T1/T2 claim with a T3 claim and makes both suspect.
3. **Attribute interested parties.** Neo4j on graphs, Palantir on ontologies, Microsoft on
   Copilot, and every systems integrator on its own accelerator are T2 by definition.
   Attribution is not a weakness — unattributed vendor numbers are.
4. **Carry the counter-evidence.** Any section arguing AI delivery gains must also hold the
   strongest contrary finding available (e.g. the METR RCT, DORA's stability results,
   GitClear's churn data). Present them yourself, framed, rather than being shown them.
5. **Never assert an ING internal fact that is not public.** ING's estate is known to us only
   through the existing draft deck and public record. Everything else is
   `[ASSUMPTION — validate with client]`, and it says so.
6. **Distinguish "we did this" from "this is possible".** The BTA Payments engagement is the
   most valuable asset in the pack precisely because it is real. Diluting it with aspiration
   destroys its value.
7. **Prefer a smaller defensible number to a larger fragile one.** A defended 18% beats an
   attacked 30%. The audience is buying confidence, not optimism.
8. **Every URL must have been fetched.** Do not cite from memory. Do not cite a paper whose
   abstract you have not read. Broken or hallucinated citations are the worst possible failure
   in front of this audience.

## Review checklist

Before any artefact is marked ready:

- [ ] Every number traceable to a source or an internal measurement definition
- [ ] Every source URL actually retrieved, not recalled
- [ ] Every vendor claim attributed to the vendor
- [ ] Every ING statement either public-sourced or tagged as an assumption
- [ ] The strongest counter-argument to the central thesis is present and answered
- [ ] No T4 intent is phrased as T3 achievement
- [ ] Every slide number has a backing entry in the dossier

## The question that governs everything

> *"Where did that number come from?"*

If the honest answer is anything other than a source you can name and a method you can
describe, the number does not go in front of the client.
