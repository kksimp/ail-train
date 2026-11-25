# Edit distance of word pairs

Each input line holds two strings separated by a single `|`, for example `kitten|sitting`. Either string may be
empty. Do not trim anything: spaces are part of the strings (but a trailing `\r` is not).

For every well-formed line print `A -> B: D` where D is the Levenshtein edit distance between A and B (the minimum
number of single-character insertions, deletions and substitutions turning A into B).

A line is malformed if it does not contain exactly one `|`. Print `line N: malformed` for it, where N is its
1-based line number. Completely empty lines are skipped silently (but still count for line numbering).

After all lines, print `pairs: P, malformed: M` with the number of well-formed pairs and malformed lines.

Example input:
```
kitten|sitting
abc|abc
|abc
a|b|c
flaw|lawn
```
Output:
```
kitten -> sitting: 3
abc -> abc: 0
 -> abc: 3
line 4: malformed
flaw -> lawn: 2
pairs: 4, malformed: 1
```
