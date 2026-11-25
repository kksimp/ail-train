# blockdiff

Print a line diff of two blocks of text read from standard input.

Input: lines. The first line that is exactly `---` separates block A (the lines before it) from block B (all lines after it; any later `---` lines are ordinary lines of B). If there is no `---` line, all lines are block A and B is empty.

Diff rule: let `a` and `b` be the line lists and `L[i][j]` the length of the longest common subsequence of `a[i..]` and `b[j..]`. Starting with `i = 0, j = 0`, repeat until both lists are used up:
- if both remain and `a[i] == b[j]`: emit `  ` + line (two spaces), and advance both;
- otherwise, if `j` is at the end of `b`, or `i` is not at the end of `a` and `L[i+1][j] >= L[i][j+1]`: emit `- ` + `a[i]` and advance `i`;
- otherwise emit `+ ` + `b[j]` and advance `j`.

After the diff lines print a summary line `+ADDED -REMOVED =SAME` with the counts of `+`, `-` and unchanged lines. Empty input prints `+0 -0 =0`.

Example input:
```
a
b
c
---
a
c
d
```
Example output:
```
  a
- b
  c
+ d
+1 -1 =2
```
