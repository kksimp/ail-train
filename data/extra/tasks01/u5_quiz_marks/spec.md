# Quiz scoring with negative marking

Line 1 is the answer key: 1 to 30 characters, each one of `A B C D`. Otherwise print `error: bad key` and stop.

Each later non-blank line is a submission `NAME ANSWERS`: ANSWERS has exactly as many characters as the key, each one of
`A B C D` or `-` (skipped). A line with a different shape, a bad character, or a NAME already submitted is invalid: skipped and counted.
A correct answer scores +4, a wrong answer -1, a skipped question 0.

Print one line per valid submission sorted by SCORE descending then NAME (byte order): `RANK NAME SCORE C/W/S` (counts of
correct, wrong, skipped). RANK is a competition rank (equal scores share a rank, the next rank skips: 1, 2, 2, 4).
Then `correct per question: n1 n2 ...` (how many valid submissions got each question right, in order, separated by spaces).
Then `mean: X.Y`: the average score over valid submissions, to one decimal, rounded to the nearest tenth with halves rounding
away from zero (a negative mean prints `-` then the magnitude; a mean that rounds to zero prints `0.0`).
Finally `invalid: K` if K > 0. If there is no valid submission print `no submissions` (then the `invalid` line if any).

Example: key `ABC`, with `amy ABD` (score 7) and `bo -B-` (score 4):
```
1 amy 7 2/1/0
2 bo 4 1/0/2
correct per question: 1 2 0
mean: 5.5
```
