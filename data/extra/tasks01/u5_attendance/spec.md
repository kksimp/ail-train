# Class attendance summary

Reads attendance records from standard input, one per line: `NAME STATUS`, separated by one or more spaces.
NAME is a word with no spaces. STATUS is one of `P` (present), `L` (late), `A` (absent), `E` (excused).

Print one line per student, in the order each name first appears:
`NAME P=p L=l A=a E=e RATE=r%`
RATE is the attendance rate: (p + l) * 100 / (p + l + a), integer division rounding down. Excused days are left out of the
rate. If p + l + a is 0, print `RATE=n/a` instead (no percent sign).

A blank line is ignored. Any other line that does not have exactly two fields, or whose STATUS is not one of the four
letters, is malformed: it is skipped, and after all student lines a final line `malformed: K` is printed (K = count of
malformed lines), only when K > 0.

If there are no student lines at all (and no malformed lines), print `no records`. If there are only malformed lines, print
just the `malformed: K` line.

Example input:
```
ann P
bob A
ann L
ann E
bob P
```
Output:
```
ann P=1 L=1 A=0 E=1 RATE=100%
bob P=1 L=0 A=1 E=0 RATE=50%
```
