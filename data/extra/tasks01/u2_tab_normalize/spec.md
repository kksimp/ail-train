# Indentation normalizer (tabs to spaces)

Line 1 of standard input is the tab width W, an integer from 1 to 8 (after trimming spaces).
Every following line is rewritten by replacing each tab character by spaces up to the next tab stop:
a tab at (0-based) column c is replaced by W - (c mod W) spaces, and columns count the characters
already produced on that line (earlier tabs included).

Print every rewritten line, then `changed=K` where K is the number of lines that contained at least one tab.

Edge cases:
- Empty input: print `no input`.
- Line 1 is not an integer from 1 to 8: print `bad width`.
- Only line 1 present: print `changed=0`.

Example input (a tab is written as <T>):
4
<T>x
ab<T>y
plain

Example output:
    x
ab  y
plain
changed=2
