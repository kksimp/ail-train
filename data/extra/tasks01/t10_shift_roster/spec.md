Shift rotation roster

The program reads a repeating shift pattern and a list of staff, and prints each person's roster and any uncovered shifts.

Input:
- Line 1: `pattern P`, where P is a non-empty string of the letters D (day), N (night) and O (off).
- Line 2: `days K`, with K an integer from 1 to 60.
- Then one line per person: `name offset` (offset a non-negative integer). Blank lines are ignored.
If either of the first two lines is missing or invalid, print `bad header` and stop.

On day d (1-based) a person works the pattern letter at index (d - 1 + offset) mod length(P).

Output, in this order:
1. One line per valid person, in input order: `name ROSTER`, where ROSTER is the K letters for days 1..K.
2. For each day 1..K in order, and for shift D before shift N: if nobody works that shift that day, print
   `uncovered day d shift S`.
3. One line per valid person, in input order: `worked name W`, W being the number of days with a letter other than O.
A person line that does not have exactly two fields or whose offset is not a non-negative integer prints
`bad line N` (N is the 1-based line number in the input) at its position among the roster lines, before the roster of later people,
and the person is ignored.

Example input:
```
pattern DDNO
days 6
ann 0
bob 2
cy x
```
Output:
```
ann DDNODD
bob NODDNO
bad line 5
uncovered day 2 shift N
uncovered day 4 shift N
uncovered day 6 shift N
worked ann 5
worked bob 4
```
