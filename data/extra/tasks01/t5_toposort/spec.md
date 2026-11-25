Standard input describes a directed graph, one item per line:
- `A -> B` means A must come before B (the separator is exactly ` -> ` with spaces; both names are non-empty and contain no spaces);
- a line with a single name and no spaces declares a node with no edges;
- blank lines and any other line are ignored. Repeated edges count once.

Print the lexicographically smallest topological order (compare names by bytes; always take the smallest available node):
`order: ` followed by the names separated by single spaces. If there are no nodes at all, print `order:`.

If the graph has a cycle, print instead `cycle: ` followed by the names, sorted and separated by single spaces, of every node that
could not be placed (the nodes on a cycle or reachable only through one). A self edge `A -> A` is a cycle.

Example input:
```
build -> test
lint
build -> package
test -> package
```
Output:
```
order: build lint test package
```
