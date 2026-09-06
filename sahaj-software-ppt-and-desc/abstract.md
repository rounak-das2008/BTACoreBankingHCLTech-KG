# Description

## Abstract
Point an AI coding agent at an unfamiliar codebase and ask it to explain the architecture, and for a few hundred files, it works beautifully. Point the same agent - with the same well-engineered prompt - at a ten-thousand-file enterprise Java monolith, and it quietly falls apart: the context window fills, compaction kicks in, the model starts forgetting details, and then it starts inventing them. This isn’t a prompt-quality problem. It’s a physics problem: a fixed-size processing container being asked to hold an unbounded amount of code.

This talk is a production report on solving it. Working on a real, ten-thousand-file legacy Java system, we built a five-layer, eleven-agent pipeline that reverse-engineers architecture, domain models, service boundaries, and workflows - without ever asking a single agent to read the whole codebase. Deterministic tools (build introspection, LSP, tree-sitter) handle structure; LLM agents are reserved exclusively for semantic reasoning; and a lightweight orchestrator (the Conductor) coordinates specialised agents tracking only the pipeline state, never code content. The result: 10,000+ classes indexed, 200+ living documents, 400+ database tables mapped, 140+ API endpoints catalogued, and documentation that regenerates incrementally as the code changes.

I’ll walk through the architecture layer by layer - Scout, Cartographers, Specialists, Surveyors, Chronicler, Conductor - and distill it into four transferable principles of context engineering: progressive disclosure, deterministic grounding, role isolation, and subagent isolation. I’ll also share what broke along the way: a symbol-indexing layer that had to be rebuilt for speed, the point where the full pipeline stopped being worth its cost, and why decoupled agent layers let us fix any one of them without touching the rest.

## Targe audience
Engineers and architects using AI agents on real codebases - especially anyone who has hit the wall where a coding agent starts hallucinating on a large, unfamiliar system - plus teams designing multi-agent pipelines for structural or high-volume analysis work.

## Key takeaways
A concrete architecture pattern for multi-agent pipelines that stay within context limits by design, not by luck
A working example of separating deterministic (tool) work from cognitive (LLM) work at scale
Four reusable principles of context engineering, and the production lessons that shaped them
How to tell when the full pipeline is worth building - and when a thinner approach is the better call

Youtube Video URL: https://www.youtube.com/watch?v=FCODql2UWM8
