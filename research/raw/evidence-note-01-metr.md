# Evidence Note 01 — The METR studies, and the reframe they hand us

> Verified directly by fetching the primary sources on 6 Sep 2026. This note exists because
> the widely-circulated "AI makes developers 19% slower" talking point **has been superseded**,
> and because METR's own factor analysis contains the single most useful argument in the
> entire evidence base for our thesis.

---

## 1. What the two studies actually say

### Study 1 — early 2025 `[T1 — independent RCT]`
- **Source:** METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source
  Developer Productivity* — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  · paper https://arxiv.org/abs/2507.09089
- **Design:** 16 experienced developers, **246 real issues** from repositories they had
  contributed to for years (averaging **22k+ stars, 1M+ lines of code**). Each issue randomly
  assigned AI-allowed / AI-disallowed. Tasks averaged ~2 hours. Screen-recorded.
  Paid $150/hr. Tooling was primarily **Cursor Pro with Claude 3.5/3.7 Sonnet**.
- **Result:** developers took **19% longer** with AI allowed (CI **+2% to +39%**).
- **The perception gap, which is the memorable part:** developers *expected* a **24% speed-up**;
  after experiencing the slowdown they still believed they had been **20% faster**.

### Study 2 — the 2026 update that supersedes it `[T1, but METR itself calls it unreliable]`
- **Source:** METR, 24 Feb 2026 — https://metr.org/blog/2026-02-24-uplift-update/
  (the 2025 page now carries a banner: *"These results are out of date."*)
- **Design:** began Aug 2025. **57 developers, 143 repos, 800+ tasks**, median 10 years'
  experience. Pay reduced to $50/hr. 10 developers carried over from study 1.
- **Raw results — direction reversed:**
  - Returning developers: **-18%** (i.e. an 18% *speed-up*), CI **-38% to +9%**
  - Newly recruited developers: **-4%** speed-up, CI **-15% to +9%**
- **METR's own caveat, and it is emphatic:** the data is *"an unreliable signal"*. Developers
  increasingly **refuse to participate** because they don't want to work without AI, and
  **30–50% of developers admitted withholding tasks** they didn't want to do unaided. Both
  biases push the measured speed-up *down*, so METR states the estimate is likely a
  **lower bound**, and that developers are *"likely… more sped up from AI tools now — in early
  2026 — compared to our estimates from early 2025."*

---

## 2. Why this matters tactically

**Do not lead with "AI makes developers slower."** As of Feb 2026 that is an out-of-date
reading of a superseded study, and anyone in the room who follows this literature will say so.
Being caught a year behind on the single most-cited study in the field would be worse than not
citing it at all.

**Equally, do not quietly drop it.** The perception-versus-reality finding stands untouched and
is the most important methodological warning in the field: **self-reported productivity gains
are unreliable in a measurable, directional way.** Developers in study 1 believed they were 20%
faster while being 19% slower.

That finding is not an argument against our proposal. It is an argument **for our measurement
model** — and it pre-emptively disarms the most dangerous question we face, which is
*"how do you know your 30% is real?"* The honest answer is: *because we measured it the way
METR measured it, not the way the industry usually claims it.*

---

## 3. The reframe — the best argument in the evidence base

From METR's own discussion of study 1, verbatim:

> *"Our results also suggest that AI capabilities may be comparatively lower in settings with
> very high quality standards, or with many implicit requirements (e.g. relating to
> documentation, testing coverage, or linting/formatting) that take humans substantial time to
> learn."*

Read that against ING's context:

| METR's stated condition for AI underperformance | ING core banking payments |
| --- | --- |
| Very high quality standards | Yes — regulated payments, supervised |
| Many **implicit** requirements | Yes — FSAs, coding standards in Forge, INGenious conventions, scheme rules, internal controls |
| Requirements that take humans substantial time to learn | Yes — this is exactly the onboarding problem |
| Developers with deep existing knowledge of the codebase | **Partly** — true for veterans, false for the majority and for every new joiner |

METR has, in effect, published the specification for when agentic AI fails. **Every failure
condition it names is a condition of implicit, unwritten knowledge.**

And that is precisely what an ontology and a knowledge graph are for:

> **METR found that AI underperforms where requirements are implicit.
> Our entire method is making the implicit explicit — in a governed model that agents can query.**

This is a genuinely strong position because it is *not* a rebuttal of the inconvenient
evidence. It accepts the finding completely and shows that the proposed architecture targets
the stated cause. It also explains, without special pleading, why a naive "point Copilot at
the repo" deployment underperforms while a grounded one need not — which is the difference we
are actually selling.

Note honestly the one place the comparison cuts against us: METR's developers had **deep**
knowledge of their codebases, and AI still slowed them down. So the claim must be scoped:
the substrate helps most where human context is *scarce* — new joiners, unfamiliar modules,
cross-team dependencies, legacy components — and helps least where a veteran is working in
code they wrote. That scoping is defensible and it is also just true.

---

## 4. Slide-safe formulations

**Permitted:**
- "In a randomised trial of experienced developers on codebases they knew well, AI tooling made
  them 19% slower — while they believed it had made them 20% faster. METR's 2026 follow-up
  suggests the picture has since reversed, but its authors caution the newer data is
  confounded. We take one lesson from both: **measure, don't self-report.**"
- "METR found AI underperforms where quality standards are high and requirements are implicit.
  That is a description of core banking. It is also a description of the problem this
  architecture is built to remove."

**Prohibited:**
- "AI makes developers 19% slower" as a present-tense fact — superseded.
- "METR proves AI speeds developers up by 18%" — METR explicitly disclaims this.
- Any use of either number without the confidence interval or the caveat.

---

## 5. Incidental data point worth keeping

METR cites, via SemiAnalysis, that **approximately 4% of GitHub commits are authored by Claude
Code** — https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point
`[T2 — third-party estimate, not audited]`. Useful only as an adoption-scale indicator, and
must be attributed.
