# regex: a tiny regular expression matcher

The first line of stdin is a pattern; every following line is a text to test. The pattern language has only three
kinds of item: a literal character (any character except `.` and `*`), `.` (matches any single character), and `x*`
where x is a literal or `.` (matches zero or more of x). There are no other operators. A match must cover the whole
text (anchored at both ends). The pattern may be empty, and so may a text line.

A `*` that is the first character of the pattern, or that directly follows another `*`, makes the pattern invalid:
print only `invalid pattern`.
Otherwise print one line per text, `"TEXT": yes` or `"TEXT": no`, in input order. A trailing newline at the end of
the input is not an extra empty text; an empty line in the middle is an empty text.
If the input has no lines at all, print `no pattern`.

Example: pattern `a*b.c` with the texts `aaabxc`, `bzc`, `abc` and `aab` prints
```
"aaabxc": yes
"bzc": yes
"abc": no
"aab": no
```
