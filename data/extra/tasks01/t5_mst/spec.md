Standard input lists weighted undirected edges, one per line: `u v w` (three words separated by whitespace), where u and v are
names and w is an integer (may be negative or zero). Blank lines and lines that are not exactly name, name, integer are ignored.
Repeated edges and self edges are allowed (a self edge never helps).

Compute a minimum spanning forest (a minimum spanning tree of every connected component) and print three lines:
`total: W`   the sum of the weights of the chosen edges,
`edges: K`   the number of chosen edges,
`components: C`   the number of connected components among all named nodes.
Empty input prints `total: 0`, `edges: 0`, `components: 0`.

Example input:
```
a b 4
b c 1
a c 2
c d 7
x y 5
a b oops
```
Output:
```
total: 15
edges: 4
components: 2
```
