---
name: graphify
description: Graphify tool for knowledge graph queries
---

# Graphify

Graphify provides three main query types for exploring the codebase knowledge graph:

## `graphify query "<question>"`
Scopes the search to answer a specific question about the codebase. Returns a focused subgraph usually much smaller than GRAPH_REPORT.md or raw grep output. Best for:
- Finding relationships between specific concepts
- Understanding how code changes propagate
- Exploring community structure and cross-file dependencies

## `graphify path "<A>" "<B>"`
Finds and displays the shortest path between two nodes A and B in the graph. Useful for:
- Tracing how a change in one module affects another
- Understanding dependency chains
- Code navigation and refactoring planning

## `graphify explain "<concept>"`
Provides a focused explanation of a specific concept, drawing from the knowledge graph. Useful for:
- Understanding architectural decisions
- Learning about a particular component
- Getting context on how things work together

After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
"""

Use `/graphify` before doing any codebase exploration to leverage the installed graphify skill.