# Graphify Tool

This tool provides access to the project's knowledge graph for codebase exploration and navigation.

## Usage

### Querying the Knowledge Graph

When investigating code architecture, use `graphify query "<your question>"` to search the knowledge graph. This returns a focused subgraph relevant to your inquiry, which is typically much smaller and more manageable than a full grep search or the entire GRAPH_REPORT.md file.

### Exploring Relationships

For understanding connections between code components, use `graphify path "<component A>" "<component B>"` to find the relationship path between two code elements.

### Getting Concept Explanations

For deep understanding of specific concepts, use `graphify explain "<concept>"` to get a focused explanation of a particular technical concept or pattern in the codebase.

### Navigation

If the project has a wiki (`graphify-out/wiki/index.md`), use it for broad navigation through the codebase architecture and concepts instead of raw source code browsing.

### Updating the Graph

After making code changes, run `graphify update .` to keep the knowledge graph current. This updates the graph's AST (Abstract Syntax Tree) representation without any API costs.

## Important Rules

1. **Always prioritize the knowledge graph** for codebase questions - it's the most efficient way to explore the project's architecture
2. **Use focused queries** rather than broad searches to get manageable, relevant results
3. **Check the wiki** (`graphify-out/wiki/index.md`) first for high-level navigation and understanding
4. **Only read GRAPH_REPORT.md** when query/path/explain don't provide enough context for your needs
5. **Run `graphify update .`** after code modifications to keep the graph current with the latest AST

## When to Use

- Code architecture questions and patterns
- Understanding component relationships
- Finding connections between different parts of the codebase
- Getting explanations of technical concepts
- Navigating the project's structure efficiently