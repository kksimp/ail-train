The first non-blank line of standard input is a start node name (the whole trimmed line).
Every following non-blank line should be an undirected edge: exactly two names separated by whitespace, `u v`.
A line that does not have exactly two words is skipped and counted.

Print one line per node, sorted by name in byte order, for the start node and every node named in an edge:
`NAME DIST`, where DIST is the fewest edges from the start node, or `-1` if the node is unreachable.
If any lines were skipped, print a last line `skipped N`.
Empty input (no non-blank line) prints nothing.

Example input:
```
a
a b
b c
d e
oops
```
Output:
```
a 0
b 1
c 2
d -1
e -1
skipped 1
```
