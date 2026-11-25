Standard input: the first non-blank line holds two names `SRC DST`. Every following non-blank line should be a weighted
undirected edge `u v w` (names u and v, integer w >= 0). Lines that are not name, name, non-negative integer are ignored.
Only names that appear in a valid edge are nodes.

Find a cheapest route from SRC to DST with Dijkstra's algorithm. To make the route unique: keep a priority queue ordered by
(distance, name); when a node is removed, skip it if a smaller distance is already final; relax its edges in the order the
edges appeared in the input; replace a node's recorded parent only when the new distance is strictly smaller.
Print `distance: D` and then `path: ` followed by the nodes joined with ` -> `.
If DST cannot be reached print `unreachable`. If SRC or DST is not a node, print `unknown node`.
If the first non-blank line is not exactly two words (including empty input) print `bad input`.

Example input:
```
a d
a b 2
b d 5
a c 4
c d 1
```
Output:
```
distance: 5
path: a -> c -> d
```
