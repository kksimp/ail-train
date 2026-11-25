Standard input lists undirected edges, one per line: `u v` (two names separated by whitespace).
Blank lines and lines that do not have exactly two words are ignored. A self edge `a a` is allowed.

Decide whether the graph is bipartite (its nodes can be split into two sides so that every edge joins different sides)
with this fixed search: take the nodes in byte-sorted order; each node not yet coloured starts a breadth-first search and gets
side 0; the search removes nodes from its queue in order and looks at each node's neighbours in byte-sorted order; an uncoloured
neighbour gets the opposite side and joins the queue; a neighbour with the same side as the node being examined is a conflict.

If a conflict is found, print `not bipartite` and then `conflict: U V` for the first conflict found (U the node being examined, V the neighbour).
Otherwise print `bipartite`, then `left: ` and `right: ` lines listing the nodes of side 0 and side 1 sorted and separated by single spaces
(a side with no nodes prints just `left:` or `right:`). Empty input is bipartite with both sides empty.

Example input:
```
a b
b c
c d
a d
```
Output:
```
bipartite
left: a c
right: b d
```
