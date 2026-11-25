Standard input lists directed edges, one per line: `u v` (two names separated by whitespace) meaning an edge from u to v.
Blank lines and lines that do not have exactly two words are ignored.

Detect a directed cycle with a depth-first search that is fully determined as follows:
start a search from each node in turn in byte-sorted order (skipping nodes already finished), and from each node follow its
out-neighbours in byte-sorted order. The first time the search reaches a node that is still on the current search path,
the cycle is the part of the path from that node onwards, closed by repeating the node.

Print `cycle: ` followed by the cycle's nodes separated by single spaces (first node repeated at the end),
or print `acyclic` if there is no cycle (also for empty input). A self edge `a a` is the cycle `a a`.

Example input:
```
a b
b c
c a
c d
```
Output:
```
cycle: a b c a
```
