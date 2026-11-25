Standard input: the first non-blank line is an integer N >= 0, the number of nodes, labelled 0 to N-1.
Every following non-blank line should be an undirected edge `u v` (two integers separated by whitespace).
A line that is not two integers in the range 0 to N-1 is ignored.

Print `components: K` where K is the number of connected components (isolated nodes count).
Then print one line per component listing its nodes in increasing order separated by single spaces;
components are ordered by their smallest node.
If the first non-blank line is not a non-negative integer (this includes empty input), print `bad header` and nothing else.

Example input:
```
6
0 1
1 2
3 4
9 9
```
Output:
```
components: 3
0 1 2
3 4
5
```
