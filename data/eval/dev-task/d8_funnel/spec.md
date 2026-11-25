# funnel

Reads a funnel definition and a log of user events and prints how many users reach each step of the funnel.

## Input

Lines of text, each ending with a newline (there are no carriage returns). Lines are numbered from 1.

- Line 1 defines the funnel: `funnel: ` (with one space after the colon) followed by 2 to 5 step names separated by commas, with no spaces, e.g. `funnel: view,cart,pay`. A step name is 1 to 10 lowercase letters `a-z`. All the names must be different.
- Every later line is either empty (ignored, but it still counts for numbering) or an event of three fields separated by single spaces:

```
TS USER STEP
```

- TS: 1 to 6 ASCII digits (a time; leading zeros are allowed).
- USER: 1 to 8 characters, each a lowercase letter or a digit.
- STEP: 1 to 10 lowercase letters. It need not be a step of the funnel (other events are valid but never advance anyone).

## Rules

1. If line 1 is missing or is not a valid funnel definition as described above, print `bad funnel` and stop; nothing else is printed.
2. A later non-empty line is checked in this order and the first rule it breaks decides its message: it does not split on single spaces into exactly three fields: `bad format`; TS is not valid: `bad time`; USER is not valid: `bad user`; STEP is not valid: `bad step`. For each such line print `line N: MESSAGE` (N the line number) in input order, before the table. A rejected line is otherwise ignored.
3. Order the valid events by TS ascending as numbers; events with equal TS keep their input order.
4. Each user starts needing funnel step 1. Go through the user's events in that order: whenever an event's STEP equals the next funnel step the user needs, the user has reached that step and now needs the one after it. Events of any other step are skipped (a step done early, or done twice, does not count). So a user has reached step K only if they reached steps 1 to K-1 first, as just described.
5. Percentages are rounded to the nearest integer, an exact half rounded up: A * 100 / B becomes (A * 200 + B) divided by (2 * B), integer division. If B is 0 the percentage is `0%`.

## Output

After any line messages, a header line and one line per funnel step in funnel order, with fields separated by single tab characters:

```
step	users	of_first	of_prev
NAME	COUNT	P1%	P2%
```

COUNT is the number of users who reached the step. P1 is COUNT as a percentage of the number of users who reached the first step. P2 is COUNT as a percentage of the number of users who reached the previous step; for the first step it is printed as `-` (without a `%` sign).

Then two lines:

```
users: N
completed: C
```

N is the number of distinct users in the valid events, and C the number of users who reached the last step.

## Example

Input:

```
funnel: view,cart,pay
1 ann view
2 ann cart
3 ann pay
1 bob view
5 bob cart
4 bob pay
2 cy cart
3 cy view
2 dee view
badrow
10 dee cart
7 eve view

9 eve Cart
```

Output (fields separated by tab characters):

```
line 11: bad format
line 15: bad step
step	users	of_first	of_prev
view	5	100%	-
cart	3	60%	60%
pay	1	20%	33%
users: 5
completed: 1
```
