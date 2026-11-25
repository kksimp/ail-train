# Bracket matcher

Read standard input. Each line is checked independently for balanced brackets of three kinds: `()`, `[]`, `{}`. All
other characters are ignored. Columns are 1-based character positions in the line.

Scan the line left to right with a stack of open brackets. Stop at the first problem and print one line for the input line:
- a closing bracket while no bracket is open: `unmatched C at COL`
- a closing bracket whose partner is not the most recently opened bracket:
  `mismatch at COL: found C but O from OCOL is open` (O is the open bracket on top of the stack, OCOL its column)
- if the scan ends with brackets still open, report the one opened last: `unclosed O at OCOL`
If no problem is found (including an empty line) print `ok`.
Print exactly one result line per input line, in order.

Example input:
    (a[b]{c})
    (a]
    x)
    f(g(

Example output:
    ok
    mismatch at 3: found ] but ( from 1 is open
    unmatched ) at 2
    unclosed ( at 4

Empty input prints nothing.
