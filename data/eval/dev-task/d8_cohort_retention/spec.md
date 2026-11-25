# cohort_retention

Reads user activity events (one user active in one month) and prints a cohort retention table.

## Input

Lines of text, each ending with a newline (there are no carriage returns). Each non-empty line is an event with exactly two fields separated by a single space:

```
USER MONTH
```

- USER: 1 to 8 characters, each a lowercase letter `a-z` or a digit `0-9`.
- MONTH: 1 or 2 ASCII digits whose value is from 1 to 24 (a leading zero is allowed, so `07` is month 7).

An empty line (zero characters) is ignored but still counts when numbering lines. Lines are numbered from 1.

## Rules

1. A non-empty line is checked in this order and the first rule it breaks decides its message:
   - it does not split on single spaces into exactly two fields: `bad format`
   - USER is not valid: `bad user`
   - MONTH is not valid: `bad month`

   For each such line print `line N: MESSAGE` (N the line number) on standard output, in input order, before anything else. A rejected line is otherwise ignored.
2. The valid events are what is left. The same user may be active in the same month on several lines; that counts once.
3. If there are no valid events, print `no events` (after any line messages) and stop.
4. A user's cohort is the earliest month in which the user is active. The cohort size is the number of users in it.
5. Let LO and HI be the smallest and largest month over all valid events. The table has one column for each offset O from 0 to HI - LO.
6. For a cohort C and offset O, the cell is `-` if C + O is greater than HI. Otherwise it is the percentage of the cohort's users that are active in month C + O: ACTIVE * 100 / SIZE rounded to the nearest integer, an exact half rounded up (in integers: (ACTIVE * 200 + SIZE) divided by (2 * SIZE), integer division), followed by `%`.

## Output

After the line messages, a header line, then one row per cohort in ascending month order. Fields are separated by single tab characters.

Header: `cohort`, `users`, then `+0`, `+1`, ... up to `+(HI-LO)`.

Row: `mC` (the letter m and the cohort month as a plain number), the cohort size, then one cell per offset.

## Example

Input:

```
ann 1
bob 1
cy 1
ann 2
bob 2
ann 3
dee 2
dee 3
zed
bob 4x
eve 03

cy 3
```

Output (fields separated by tab characters):

```
line 9: bad format
line 10: bad month
cohort	users	+0	+1	+2
m1	3	100%	67%	67%
m2	1	100%	100%	-
m3	1	100%	-	-
```
