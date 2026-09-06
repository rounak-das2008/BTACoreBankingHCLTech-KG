#!/usr/bin/env python3
"""Builds the PRIME.AI v2 business deck as a real .pptx file.
Content mirrors research/03-slide-deck-content.md.
Diagrams are drawn as native PowerPoint shapes (not images) so they stay editable.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

# ---------- palette ----------
ORANGE = RGBColor(0xE8, 0x5B, 0x1E)   # HCLTech-ish accent
NAVY   = RGBColor(0x1B, 0x2A, 0x4A)
DARK   = RGBColor(0x22, 0x22, 0x22)
GREY   = RGBColor(0x55, 0x55, 0x55)
LGREY  = RGBColor(0xF0, 0xF0, 0xF0)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GREEN  = RGBColor(0x2E, 0x7D, 0x32)
PURPLE = RGBColor(0x5B, 0x3A, 0x8E)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]


def add_slide():
    return prs.slides.add_slide(BLANK)


def add_footer(slide, n):
    box = slide.shapes.add_textbox(Inches(0.4), SLIDE_H - Inches(0.4), Inches(6), Inches(0.3))
    tf = box.text_frame
    tf.text = "Classification: Internal  |  HCLTech + ING  |  PRIME.AI v2"
    tf.paragraphs[0].font.size = Pt(9)
    tf.paragraphs[0].font.color.rgb = GREY
    box2 = slide.shapes.add_textbox(SLIDE_W - Inches(0.8), SLIDE_H - Inches(0.4), Inches(0.5), Inches(0.3))
    box2.text_frame.text = str(n)
    box2.text_frame.paragraphs[0].font.size = Pt(9)
    box2.text_frame.paragraphs[0].font.color.rgb = GREY


def add_title(slide, text, size=30, color=NAVY, top=Inches(0.35), height=Inches(1.0)):
    box = slide.shapes.add_textbox(Inches(0.5), top, SLIDE_W - Inches(1.0), height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.text = text
    p = tf.paragraphs[0]
    p.font.size = Pt(size)
    p.font.bold = True
    p.font.color.rgb = color
    p.font.name = "Calibri"
    rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), top + height - Inches(0.08),
                                   Inches(2.2), Pt(4))
    rule.fill.solid(); rule.fill.fore_color.rgb = ORANGE
    rule.line.fill.background()
    return box


def add_bullets(slide, items, left=Inches(0.6), top=Inches(1.5), width=None, height=None,
                 size=18, color=DARK, bold_first_word=False):
    width = width or (SLIDE_W - Inches(1.2))
    height = height or (SLIDE_H - top - Inches(0.6))
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        level = 0
        text = item
        if isinstance(item, tuple):
            text, level = item
        p.text = f"{text}"
        p.level = level
        p.font.size = Pt(size - level * 2)
        p.font.color.rgb = color
        p.space_after = Pt(10)
    return box


def add_notes(slide, note):
    slide.notes_slide.notes_text_frame.text = note


def styled_box(slide, x, y, w, h, text, fill=NAVY, font_color=WHITE, size=13, bold=True,
               shape=MSO_SHAPE.ROUNDED_RECTANGLE, line_color=None):
    sp = slide.shapes.add_shape(shape, x, y, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line_color:
        sp.line.color.rgb = line_color
        sp.line.width = Pt(1.25)
    else:
        sp.line.fill.background()
    tf = sp.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.text = text
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = font_color
    return sp


def arrow(slide, x1, y1, x2, y2, color=GREY, width=Pt(1.5), dashed=False):
    conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x1, y1, x2, y2)
    conn.line.color.rgb = color
    conn.line.width = width
    if dashed:
        ln = conn.line._get_or_add_ln()
        d = ln.makeelement(qn('a:prstDash'), {'val': 'dash'})
        ln.append(d)
    conn.line.end_arrowhead = True if False else None  # placeholder, python-pptx lacks direct API
    return conn


def add_table(slide, rows, col_widths, left, top, row_h=Inches(0.45), header_fill=NAVY,
              font_size=13):
    n_rows = len(rows)
    n_cols = len(rows[0])
    total_w = sum(col_widths)
    tbl_shape = slide.shapes.add_table(n_rows, n_cols, left, top, total_w, row_h * n_rows)
    tbl = tbl_shape.table
    for c, w in enumerate(col_widths):
        tbl.columns[c].width = w
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = tbl.cell(r, c)
            cell.text = str(val)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            para = cell.text_frame.paragraphs[0]
            para.font.size = Pt(font_size)
            if r == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = header_fill
                para.font.bold = True
                para.font.color.rgb = WHITE
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE if r % 2 else LGREY
                para.font.color.rgb = DARK
    return tbl_shape


# =========================================================================
# SLIDE 1 — Title
# =========================================================================
s = add_slide()
bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
bg.fill.solid(); bg.fill.fore_color.rgb = NAVY
bg.line.fill.background()
bg.shadow.inherit = False

bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(3.15), SLIDE_W, Inches(0.06))
bar.fill.solid(); bar.fill.fore_color.rgb = ORANGE
bar.line.fill.background()

box = s.shapes.add_textbox(Inches(0.8), Inches(2.1), Inches(11.7), Inches(1.0))
tf = box.text_frame; tf.text = "PRIME.AI"
tf.paragraphs[0].font.size = Pt(54); tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = WHITE

box = s.shapes.add_textbox(Inches(0.8), Inches(3.3), Inches(11.7), Inches(0.8))
tf = box.text_frame; tf.text = "Agentic Engineering for Core Banking Delivery"
tf.paragraphs[0].font.size = Pt(24); tf.paragraphs[0].font.color.rgb = RGBColor(0xE0,0xE0,0xE0)

box = s.shapes.add_textbox(Inches(0.8), Inches(4.1), Inches(11.7), Inches(0.6))
tf = box.text_frame
tf.text = "Grounding AI agents in ING's model of its business — not just in a language model"
tf.paragraphs[0].font.size = Pt(16); tf.paragraphs[0].font.italic = True
tf.paragraphs[0].font.color.rgb = RGBColor(0xCC,0xCC,0xCC)

box = s.shapes.add_textbox(Inches(0.8), Inches(6.6), Inches(11.7), Inches(0.5))
tf = box.text_frame
tf.text = "BTA Payments Programme  |  HCLTech + ING Core Banking  |  Classification: Internal"
tf.paragraphs[0].font.size = Pt(12); tf.paragraphs[0].font.color.rgb = RGBColor(0xAA,0xAA,0xAA)

add_notes(s, "One sentence if nothing else lands: 'We ground the agents in the bank's model, not just in the language model.'")

# =========================================================================
# SLIDE 2 — Agenda
# =========================================================================
s = add_slide()
add_title(s, "Agenda")
items = [
    "What we already proved — and what it doesn't yet answer",
    "The one insight that changes the approach",
    "PRIME.AI v2 — the architecture",
    "Seeing it work — one payment, start to finish",
    "What we measure, and what we don't claim",
    "The path to adopt it",
]
top = Inches(1.7)
for i, item in enumerate(items):
    y = top + Inches(0.85) * i
    styled_box(s, Inches(0.7), y, Inches(0.6), Inches(0.6), str(i+1), fill=ORANGE, size=20)
    box = s.shapes.add_textbox(Inches(1.5), y, Inches(10.5), Inches(0.6))
    tf = box.text_frame; tf.text = item
    tf.paragraphs[0].font.size = Pt(20); tf.paragraphs[0].font.color.rgb = DARK
add_footer(s, 2)
add_notes(s, "Signal early this is a v2, not a rescue of v1 — invites less defensiveness about v1's gaps.")

# =========================================================================
# SLIDE 3 — The problem
# =========================================================================
s = add_slide()
add_title(s, "The problem, in your terms")
add_bullets(s, [
    "The payments estate is bigger than anyone's memory — or any model's context window",
    "Knowledge leaves the building when people do",
    "Documentation is out of date the day it's written",
    "Regulatory deadlines do not move (IPR, ISO 20022, EPI/Wero)",
    "Every change must be provable — to your auditors, and to DNB",
], top=Inches(1.6), size=18)
callout = styled_box(s, Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.1),
    "AI, pointed at a system nobody fully understands, produces confident answers fast —\nthat is not a solution, it is a new risk.",
    fill=RGBColor(0x8B,0x1A,0x1A), size=17)
add_footer(s, 3)
add_notes(s, "Lead with risk, not speed — this audience buys delivery-risk reduction; velocity is a consequence. T4 framing, no numbers yet.")

# =========================================================================
# SLIDE 4 — What we already proved
# =========================================================================
s = add_slide()
add_title(s, "What we already proved — stated honestly")
add_bullets(s, [
    "BTA Payments stream: 1 squad, 10 engineers, 7 agents, one full delivery cycle",
    "Endpoint delivery: 2 sprints -> 1.4 sprints observed",
    "Capacity recovered was reinvested in the DG requirements, not banked as margin",
], top=Inches(1.6), size=18)
callout = styled_box(s, Inches(0.8), Inches(4.2), Inches(11.7), Inches(1.3),
    "What we did not yet measure: defect escape rate, change-failure rate, rework/churn —\nthe stability half of the picture.",
    fill=RGBColor(0x8B,0x1A,0x1A), size=17)
box = s.shapes.add_textbox(Inches(0.8), Inches(5.7), Inches(11.7), Inches(1.0))
tf = box.text_frame; tf.word_wrap=True
tf.text = "Conclusion: the acceleration is real; the evidence pack around it is not yet complete."
tf.paragraphs[0].font.size = Pt(18); tf.paragraphs[0].font.italic = True; tf.paragraphs[0].font.color.rgb = NAVY
add_footer(s, 4)
add_notes(s, "T3 claim, stated with what's missing rather than hiding it. Hostile Q: 'How do you know quality didn't suffer?' Honest answer: 'We don't have that evidence yet -- which is exactly what v2's measurement model closes.'")

# =========================================================================
# SLIDE 5 — The insight (mindmap-ish radial)
# =========================================================================
s = add_slide()
add_title(s, "The insight that changes the approach")
box = s.shapes.add_textbox(Inches(0.7), Inches(1.5), Inches(11.9), Inches(0.6))
tf = box.text_frame; tf.word_wrap = True
tf.text = "Six independent sources, one conclusion: the bottleneck was never the model. It's context."
tf.paragraphs[0].font.size = Pt(18); tf.paragraphs[0].font.bold = True; tf.paragraphs[0].font.color.rgb = NAVY

center = styled_box(s, Inches(5.1), Inches(3.15), Inches(3.1), Inches(1.1),
    "Context is\nthe bottleneck", fill=ORANGE, size=18)

nodes = [
    ("Sahaj Software\n\"Compaction kills context\"\nDeterministic grounding", Inches(0.5), Inches(2.3)),
    ("Neo4j — Eifrem\n\"Thin agents on a\nsmarter substrate\"", Inches(9.6), Inches(2.3)),
    ("UC Berkeley — Coyle\nOntology as guardrail\nNeuro-symbolic AI", Inches(0.5), Inches(5.0)),
    ("Kelsey Hightower\n\"Infer once, export,\nrun without inference\"", Inches(9.6), Inches(5.0)),
    ("Matt Pocock\nUbiquitous language\nGood codebases compound AI", Inches(3.1), Inches(5.6)),
    ("Blitzy AI\n\"Context is the thesis\"", Inches(7.2), Inches(5.6)),
]
for text, x, y in nodes:
    styled_box(s, x, y, Inches(3.0), Inches(1.0), text, fill=NAVY, size=12, bold=False)

add_footer(s, 5)
add_notes(s, "T2, six named practitioner sources (full citations in dossier). This slide earns the right to propose an architecture rather than another prompt library.")

# =========================================================================
# SLIDE 6 — Thesis
# =========================================================================
s = add_slide()
bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
box = s.shapes.add_textbox(Inches(1.2), Inches(2.5), Inches(10.9), Inches(2.5))
tf = box.text_frame; tf.word_wrap = True
tf.text = "We build and maintain one governed, living model of ING's payments estate — and run thin, specialised, accountable agents on top of it."
tf.paragraphs[0].font.size = Pt(32); tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = WHITE
tf.paragraphs[0].alignment = PP_ALIGN.CENTER
box2 = s.shapes.add_textbox(Inches(1.2), Inches(5.3), Inches(10.9), Inches(0.6))
tf2 = box2.text_frame
tf2.text = "Not a bigger prompt library. Not a faster model. A substrate."
tf2.paragraphs[0].font.size = Pt(18); tf2.paragraphs[0].font.italic = True
tf2.paragraphs[0].font.color.rgb = ORANGE
tf2.paragraphs[0].alignment = PP_ALIGN.CENTER
add_notes(s, "Give the room ten seconds of silence on this slide. It is the whole pitch.")

# =========================================================================
# SLIDE 7 — PRIME.AI re-grounded (table)
# =========================================================================
s = add_slide()
add_title(s, "PRIME.AI, re-grounded")
rows = [
    ["", "v1 (today)", "v2 (proposed)"],
    ["P", "Prompt driven", "Progressive disclosure — agents see only what their role needs"],
    ["R", "Reusable", "Role-isolated — one agent, one competency, one narrow context"],
    ["I", "Intent focused", "Intent-traceable — regulation -> requirement -> code -> test -> release"],
    ["M", "Modular", "Model-grounded — grounded in the bank's model, not just the language model"],
    ["E", "Engineering", "Evidenced — every velocity claim paired with a stability claim"],
]
add_table(s, rows, [Inches(0.6), Inches(2.6), Inches(9.2)], Inches(0.6), Inches(1.6), row_h=Inches(0.82), font_size=14)
box = s.shapes.add_textbox(Inches(0.6), Inches(6.6), Inches(11.9), Inches(0.6))
tf = box.text_frame
tf.text = "Same name. Same team's work carried forward. A firmer foundation underneath it."
tf.paragraphs[0].font.size = Pt(15); tf.paragraphs[0].font.italic = True; tf.paragraphs[0].font.color.rgb = GREY
add_footer(s, 7)
add_notes(s, "Reframe as evolution, not indictment of v1 -- protects the team that built it while fixing the substance.")

# =========================================================================
# SLIDE 8 — Seven planes architecture
# =========================================================================
s = add_slide()
add_title(s, "The architecture: seven planes", size=28)
box = s.shapes.add_textbox(Inches(0.6), Inches(1.25), Inches(12.0), Inches(0.4))
tf = box.text_frame
tf.text = "No language model ever touches raw estate data directly — it queries a governed model of it."
tf.paragraphs[0].font.size = Pt(14); tf.paragraphs[0].font.italic = True; tf.paragraphs[0].font.color.rgb = GREY

planes = [
    ("P6 — Governance & Evidence", "Agent identity · immutable log · approval gates", RGBColor(0x8B,0x1A,0x1A)),
    ("P5 — Orchestration (the Conductor)", "State in, instructions out · retry / escalate", RGBColor(0x6A,0x1B,0x9A)),
    ("P4 — Agent Fleet", "Comprehend · Specify · Construct · Verify · Operate · Curate", PURPLE),
    ("P3 — Semantic Bridge", "business concept <-> technical artefact", RGBColor(0x1B,0x5E,0x20)),
    ("P2 — Business Ontology", "BIAN · ISO 20022 · FIBO", GREEN),
    ("P1 — Estate Graph", "repos · services · tables · topics · tests · releases", RGBColor(0x2E,0x5E,0x8B)),
    ("P0 — Ground Truth (no LLM)", "build introspection · LSP · schema · Git · pipelines · traces", NAVY),
]
top = Inches(1.85)
h = Inches(0.72)
gap = Inches(0.05)
for i, (title, sub, color) in enumerate(planes):
    y = top + (h + gap) * i
    box = styled_box(s, Inches(0.6), y, Inches(12.1), h, "", fill=color, size=13)
    tf = box.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].text = title
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(15)
    tf.paragraphs[0].font.color.rgb = WHITE
    tf.paragraphs[0].alignment = PP_ALIGN.LEFT
    p2 = tf.add_paragraph()
    p2.text = sub
    p2.font.size = Pt(12)
    p2.font.color.rgb = RGBColor(0xE8,0xE8,0xE8)
    p2.alignment = PP_ALIGN.LEFT
    for para in tf.paragraphs:
        para.alignment = PP_ALIGN.LEFT
    tf.margin_left = Inches(0.25)
add_notes(s, "This single diagram is the technical spine of the whole deck -- everything in the appendix zooms into one box here.")

# =========================================================================
# SLIDE 9 — Ground truth
# =========================================================================
s = add_slide()
add_title(s, "Layer 1: never let a model do a parser's job")
add_bullets(s, [
    "Structure is already encoded in build files, language servers, database schemas, pipeline configs",
    "Extracting it is mechanical, not cognitive — we use compilers, parsers and static analysis to build the map",
    "Language models are never spent re-deriving what a parser already knows",
], top=Inches(1.7), size=18)
callout = styled_box(s, Inches(0.8), Inches(4.6), Inches(11.7), Inches(1.3),
    "This is also the cost answer: infer once, export the fact, query it forever —\nnever pay inference twice for the same fact.",
    fill=GREEN, size=17)
add_footer(s, 9)
add_notes(s, "T2 (Sahaj, Hightower). Direct pre-emption of 'isn't this expensive' -- most of the estate is mapped for free.")

# =========================================================================
# SLIDE 10 — Business ontology
# =========================================================================
s = add_slide()
add_title(s, "Layer 2: one model of the estate, in the bank's language")
add_bullets(s, [
    "Technical side: every repo, service, endpoint, table, topic, test, pipeline, release — one connected graph, not 200 disconnected documents",
    "Business side: we do not invent a payments ontology — we ground it in standards your architects already use:",
    ("BIAN — service domains and the banking service landscape", 1),
    ("ISO 20022 — the payments message model mandated across SEPA, T2, CBPR+", 1),
    ("FIBO — financial instruments and party concepts", 1),
    "A Customer has a first name, never an f_name — legible to a business reader, not just a database",
], top=Inches(1.6), size=17)
add_footer(s, 10)
add_notes(s, "T1/T2 mixed. Hostile Q: 'Why not build our own?' Answer: 'Your engineers already speak this language -- adopting it is lower risk and lower cost than inventing one.'")

# =========================================================================
# SLIDE 11 — Worked example
# =========================================================================
s = add_slide()
add_title(s, "One payment, start to finish", size=28)
chain = [
    "EU Instant Payments\nRegulation",
    "Requirement:\nVerification of Payee",
    "BIAN service domain:\nPayment Execution",
    "User story +\nacceptance criteria",
    "Services, endpoints,\ntables, topics",
    "Tests that\nprove it",
    "Release that\nshipped it",
    "Evidence pack:\none query",
]
n = len(chain)
box_w = Inches(1.42)
gap = Inches(0.15)
total_w = box_w * n + gap * (n - 1)
start_x = (SLIDE_W - total_w) / 2
y = Inches(3.2)
prev_cx = None
for i, text in enumerate(chain):
    x = start_x + (box_w + gap) * i
    fill = GREEN if i == n - 1 else (NAVY if i % 2 == 0 else PURPLE)
    styled_box(s, x, y, box_w, Inches(1.3), text, fill=fill, size=10.5)
    cx = x + box_w
    if prev_cx is not None:
        conn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, prev_cx, y + Inches(0.65), x, y + Inches(0.65))
        conn.line.color.rgb = GREY
        conn.line.width = Pt(2)
    prev_cx = cx
add_footer(s, 11)
add_notes(s, "Ask any of your engineers today to produce this chain for a payment in under a minute -- that's the demo. T4 unless already demoed live, then promote to T3 and say so.")

# =========================================================================
# SLIDE 12 — Agent fleet reorganized
# =========================================================================
s = add_slide()
add_title(s, "The agent fleet, reorganised around the work", size=26)
rows = [
    ["Family", "Does", "New?"],
    ["Comprehend", "Understands the existing estate", "New -- the gap in v1"],
    ["Specify", "Requirement -> story -> acceptance criteria", "was: Story Generator"],
    ["Construct", "Writes the change", "was: Code / Unit Test Generator"],
    ["Verify", "Independently checks the change", "New -- separated from Construct"],
    ["Operate", "Reproduces, triages, roots-causes, fixes", "was: Defect Triage / Mechanic"],
    ["Curate", "Keeps the graph itself true and current", "New -- prevents drift"],
    ["Govern", "Assembles evidence, enforces policy", "New -- the audit answer"],
]
add_table(s, rows, [Inches(1.8), Inches(5.8), Inches(4.3)], Inches(0.6), Inches(1.55), row_h=Inches(0.62), font_size=13)
add_footer(s, 12)
add_notes(s, "Hostile Q: 'Isn't Verify just Construct checking its own work?' Answer: 'No -- different agent, different context, different inputs.'")

# =========================================================================
# SLIDE 13 — Orchestration
# =========================================================================
s = add_slide()
add_title(s, "Who watches the workers? Orchestration", size=26)
add_bullets(s, [
    "Every agent fleet needs an answer to: how many workers run, what happens when one fails, what runs in parallel vs what must wait",
    "Our orchestrator — the Conductor — holds only pipeline state, never code or documents",
    "Failure is a designed state: retry, replan, or escalate to a named human with context preserved",
], top=Inches(1.5), size=16, height=Inches(2.0))

cx, cy = Inches(5.6), Inches(3.6)
conductor = styled_box(s, cx, cy, Inches(2.1), Inches(0.9), "Conductor\n(state only)", fill=ORANGE, size=13)
agents = ["Comprehend", "Specify", "Construct", "Verify"]
positions = [(Inches(0.7), Inches(5.3)), (Inches(3.9), Inches(5.3)), (Inches(7.1), Inches(5.3)), (Inches(10.3), Inches(5.3))]
for name, (x, y) in zip(agents, positions):
    styled_box(s, x, y, Inches(2.0), Inches(0.8), name, fill=NAVY, size=12)
    conn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x + Inches(1.0), cy + Inches(0.9), x + Inches(1.0), y)
    conn.line.color.rgb = GREY; conn.line.width = Pt(1.5)
human = styled_box(s, Inches(9.7), Inches(1.5), Inches(2.6), Inches(0.8), "Human: retry / replan / escalate", fill=RGBColor(0x8B,0x1A,0x1A), size=11)
conn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, cx + Inches(2.1), cy + Inches(0.2), Inches(9.7), Inches(1.9))
conn.line.color.rgb = GREY; conn.line.width = Pt(1.5)
add_footer(s, 13)
add_notes(s, "T2 (Sahaj's Conductor pattern, adopted). Direct answer to 'what happens when an agent gets it wrong at 2am'.")

# =========================================================================
# SLIDE 14 — Deterministic vs cognitive
# =========================================================================
s = add_slide()
add_title(s, "Where AI is not allowed to touch", size=28)
rows = [
    ["Task", "Deterministic tool", "AI agent"],
    ["Parse code, build call graph", "YES", "--"],
    ["Dependency & impact analysis", "YES", "--"],
    ["Schema / contract diff", "YES", "--"],
    ["Lint, static analysis, security scan", "YES", "--"],
    ["Test execution & coverage measurement", "YES", "--"],
    ["Infer meaning of legacy code", "--", "YES"],
    ["Draft requirement / story", "--", "YES"],
    ["Propose the code change", "--", "YES"],
    ["Root-cause a defect narrative", "--", "YES"],
]
add_table(s, rows, [Inches(6.0), Inches(3.0), Inches(3.0)], Inches(0.6), Inches(1.45), row_h=Inches(0.52), font_size=13)
callout = styled_box(s, Inches(0.6), Inches(6.7), Inches(12.1), Inches(0.6),
    "Rule: if a compiler, parser or query could answer it, a language model is not asked to.",
    fill=NAVY, size=14)
add_notes(s, "T4 design rule (Sahaj/Hightower). Publishing where we DON'T use AI is what makes the rest believable.")

# =========================================================================
# SLIDE 15 — Guardrails
# =========================================================================
s = add_slide()
add_title(s, "Guardrails: keeping probabilistic agents honest")
add_bullets(s, [
    "The graph isn't only retrieval — it's a validator",
    "Constraints in the model catch what a plausible-sounding sentence would not:",
    ("A second refund against the same payment", 1),
    ("A payout routed to a support agent instead of the beneficiary", 1),
    ("An invented status such as \u201cprobably settled\u201d", 1),
    "Nothing reaches a human approval gate until it passes this check",
], top=Inches(1.7), size=18)
add_footer(s, 15)
add_notes(s, "T2 (Coyle's neuro-symbolic argument). Frame as belt-and-braces -- a separate symbolic check, not the same model marking its own work.")

# =========================================================================
# SLIDE 16 — Governance
# =========================================================================
s = add_slide()
add_title(s, "Governance is not overhead — it's the same graph")
add_bullets(s, [
    "Every agent is a named principal with least-privilege access — never a shared account",
    "Every proposal, approval and change is an entry in an immutable log",
    "A human approves every change that reaches production — the agent proposes, a person owns",
], top=Inches(1.7), size=18)
callout = styled_box(s, Inches(0.8), Inches(4.6), Inches(11.7), Inches(1.3),
    "The audit evidence pack and the engineering traceability graph are the same artefact —\nproduced once, used twice.",
    fill=GREEN, size=17)
add_footer(s, 16)
add_notes(s, "This slide exists because the current deck has none like it -- for this audience that omission is louder than anything we could add elsewhere.")

# =========================================================================
# SLIDE 17 — Measurement
# =========================================================================
s = add_slide()
add_title(s, "How we'll measure it — and what we won't hide", size=26)
rows = [
    ["Velocity", "Paired with"],
    ["Lead time for change", "Change failure rate"],
    ["Defect detection in-sprint", "Defect escape rate"],
    ["First-time-right rate", "Code churn within 21 days"],
]
add_table(s, rows, [Inches(5.9), Inches(5.9)], Inches(0.6), Inches(1.5), row_h=Inches(0.55), font_size=15)
callout = styled_box(s, Inches(0.6), Inches(4.1), Inches(12.1), Inches(2.6),
    "Independent research (METR, 2025-26) found developers can be measurably slower with AI on "
    "unfamiliar, high-standards codebases -- while believing they were faster.\n\n"
    "That finding describes exactly the conditions of core banking payments work -- which is why "
    "we measure, rather than ask engineers how it felt.",
    fill=RGBColor(0x8B,0x1A,0x1A), size=15)
add_notes(s, "T1 for METR; T4 for our measurement commitment. The 'we read the inconvenient study and it changed our design' slide -- never cut for time.")

# =========================================================================
# SLIDE 18 — Roadmap
# =========================================================================
s = add_slide()
add_title(s, "Roadmap: four steps, each valuable alone", size=26)
steps = [
    ("1. Map", "weeks 1-4", "Queryable map of the payments stream", "No AI risk at all", NAVY),
    ("2. Mean", "weeks 5-12", "Business ontology grounded in BIAN/ISO 20022", "Standards adoption, not invention", PURPLE),
    ("3. Work", "months 3-6", "Existing agents re-grounded + Verify/Curate added", "Same agents, evidenced improvement", RGBColor(0x2E,0x5E,0x8B)),
    ("4. Govern & Scale", "month 6+", "Evidence packs on demand; extend beyond payments", "Becomes a reusable asset", GREEN),
]
box_w = Inches(2.85)
gap = Inches(0.25)
start_x = Inches(0.6)
y = Inches(1.8)
prev_cx = None
for i, (title, when, delivers, risk, color) in enumerate(steps):
    x = start_x + (box_w + gap) * i
    box = styled_box(s, x, y, box_w, Inches(0.65), f"{title}\n({when})", fill=color, size=13)
    tbox = s.shapes.add_textbox(x, y + Inches(0.8), box_w, Inches(2.2))
    tf = tbox.text_frame; tf.word_wrap = True
    tf.text = delivers
    tf.paragraphs[0].font.size = Pt(12.5); tf.paragraphs[0].font.color.rgb = DARK
    p2 = tf.add_paragraph(); p2.text = ""
    p3 = tf.add_paragraph(); p3.text = risk
    p3.font.size = Pt(11.5); p3.font.italic = True; p3.font.color.rgb = GREY
    cx = x + box_w
    if prev_cx is not None:
        conn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, prev_cx, y + Inches(0.32), x, y + Inches(0.32))
        conn.line.color.rgb = GREY; conn.line.width = Pt(2)
    prev_cx = cx
add_footer(s, 18)
add_notes(s, "Lead with step 1's lack of AI risk -- the easiest yes a bank has ever been asked to give.")

# =========================================================================
# SLIDE 19 — What we're not claiming
# =========================================================================
s = add_slide()
add_title(s, "What we are not claiming")
add_bullets(s, [
    "Not claiming agents write production payment logic unsupervised — a human approves every change",
    "Not claiming a percentage of code is \u201cAI-written\u201d — that framing invites a question we can't comfortably answer",
    "Not claiming the ontology is complete on day one — it covers payments and grows by use",
    "Not claiming every engineer gets faster — independent evidence says otherwise for unfamiliar codebases, which is precisely the condition this architecture targets",
], top=Inches(1.7), size=18)
add_footer(s, 19)
add_notes(s, "Read this slide slowly. It is the slide that makes every other slide believable.")

# =========================================================================
# SLIDE 20 — The ask
# =========================================================================
s = add_slide()
bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
box = s.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(0.9))
tf = box.text_frame; tf.text = "The ask"
tf.paragraphs[0].font.size = Pt(34); tf.paragraphs[0].font.bold = True; tf.paragraphs[0].font.color.rgb = WHITE
items = [
    "Approve Step 1 (Map) for the BTA Payments stream — four weeks, deterministic tooling only",
    "Agree the measurement baseline together, before we run it — not after",
    "Nominate an estate owner on ING's side to hold the model once it exists",
]
top = Inches(2.2)
for i, item in enumerate(items):
    y = top + Inches(1.1) * i
    styled_box(s, Inches(0.8), y, Inches(0.6), Inches(0.6), str(i+1), fill=ORANGE, size=20)
    box = s.shapes.add_textbox(Inches(1.6), y, Inches(10.9), Inches(0.9))
    tf = box.text_frame; tf.word_wrap = True; tf.text = item
    tf.paragraphs[0].font.size = Pt(19); tf.paragraphs[0].font.color.rgb = WHITE
add_notes(s, "Close on a small, low-risk, concrete yes -- not a transformation commitment.")

# =========================================================================
# APPENDIX DIVIDER
# =========================================================================
s = add_slide()
bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
bg.fill.solid(); bg.fill.fore_color.rgb = GREY; bg.line.fill.background()
box = s.shapes.add_textbox(Inches(1), Inches(3.2), Inches(11), Inches(1))
tf = box.text_frame; tf.text = "Appendix — held in reserve"
tf.paragraphs[0].font.size = Pt(36); tf.paragraphs[0].font.bold = True; tf.paragraphs[0].font.color.rgb = WHITE
tf.paragraphs[0].alignment = PP_ALIGN.CENTER

# =========================================================================
# A1 — Full roster mapping
# =========================================================================
s = add_slide()
add_title(s, "A1 — Full agent roster (old -> new)", size=24)
rows = [
    ["Old agent (v1)", "New family", "Writes to graph"],
    ["User Story Generation", "Specify", "Requirements, stories, traceability edges"],
    ["Test Case Generation", "Specify / Verify", "Test cases, coverage edges"],
    ["Code Generation", "Construct", "Proposed change linked to story"],
    ["Unit Test Case Generation", "Construct / Verify", "Test evidence"],
    ["INGenious Test Script Generator", "Verify", "Automation evidence"],
    ["Defect Triage", "Operate", "Defect -> code linkage"],
    ["Mechanic", "Operate", "RCA, fix, release linkage"],
    ["(none in v1)", "Comprehend", "Structure, boundaries, domain model"],
    ["(none in v1)", "Curate", "Freshness, drift flags, corrections"],
    ["(none in v1)", "Govern", "Evidence packs, control attestations"],
]
add_table(s, rows, [Inches(4.2), Inches(2.8), Inches(5.1)], Inches(0.6), Inches(1.4), row_h=Inches(0.48), font_size=12)

# =========================================================================
# A2 — Competitive position
# =========================================================================
s = add_slide()
add_title(s, "A2 — Competitive position")
add_bullets(s, [
    "Sahaj Software: strongest comprehension-only approach found publicly — five layers, eleven agents, a lean orchestrator, four context-engineering principles",
    "Applied to reverse-engineering a legacy Java estate into documentation — and it stops there",
    "PRIME.AI v2 adopts the same discipline, and additionally:",
    ("Turns the output into a queryable, living graph — not a document set", 1),
    ("Grounds the business layer in BIAN / ISO 20022 / FIBO — not a generic taxonomy", 1),
    ("Spans the full lifecycle forward from requirement to release — not comprehension alone", 1),
    ("Adds the governance plane a regulated bank requires", 1),
    "No public competitor combines all four",
], top=Inches(1.6), size=16)

# =========================================================================
# A3 — Assumptions
# =========================================================================
s = add_slide()
add_title(s, "A3 — Assumptions to validate with ING")
add_bullets(s, [
    "Which graph technology is permitted in ING's approved estate",
    "Where source-code-derived artefacts may be processed and stored, and under which model-hosting arrangement",
    "Whether ING already holds a BIAN- or ISO-20022-aligned service catalogue to adopt rather than derive",
    "The actual baseline behind the existing 30% figure — which sprints, which definition of done",
    "Who owns the substrate after the engagement ends",
    "What controls already apply to non-human actors in the pipeline today",
], top=Inches(1.6), size=17)

# =========================================================================
# A4 — Glossary
# =========================================================================
s = add_slide()
add_title(s, "A4 — Glossary")
add_bullets(s, [
    "BIAN — Banking Industry Architecture Network; a standard service-domain landscape for banks",
    "ISO 20022 — the payments message standard behind SEPA, T2, CBPR+",
    "FIBO — Financial Industry Business Ontology (EDM Council)",
    "Knowledge graph — a queryable network of entities and relationships, not a document set",
    "Ontology — a formal, shared definition of the concepts and relationships in a domain",
    "Orchestrator / Conductor — the component that schedules agents and holds pipeline state only",
], top=Inches(1.6), size=17)

# ---------- save ----------
out_dir = "/Users/rounakdas/Downloads/HCLTech - ING Core Banking BTA KG and Agent Architecture/research"
out_path = os.path.join(out_dir, "PRIME.AI-v2-Business-Deck.pptx")
prs.save(out_path)
print(f"Saved: {out_path}")
print(f"Slides: {len(prs.slides.__iter__.__self__._sldIdLst)}")
