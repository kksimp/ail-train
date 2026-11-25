# Bounding boxes per group

Reads labelled points and prints the bounding box of each label.

Input: each non-blank line of the form `NAME X Y` (exactly three whitespace-separated fields; NAME is any text without spaces, X and Y are integers made of an optional `-` and digits) adds the point (X, Y) to group NAME. Any other non-blank line is skipped and counted. Blank lines are ignored.

Output: one line per group, in order of the group's first appearance, `NAME MINX MINY MAXX MAXY COUNT`, separated by single spaces. Then a last line `skipped K` with the number of skipped lines.

Example input:
```
a 1 5
b 0 0
a -2 7
oops
a 3 6
```
Output:
```
a -2 5 3 7 3
b 0 0 0 0 1
skipped 1
```

Edge cases: empty input prints only `skipped 0`. Group names are case-sensitive.
