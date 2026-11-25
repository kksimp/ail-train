# Mastermind feedback

Read a Mastermind secret code and a series of guesses from standard input and print the feedback pegs for each guess.

## Input

- Line 1: the secret code, exactly 4 characters, each one of the capital letters `A` to `F` (repeats allowed). This line is always valid. Surrounding whitespace on any line is ignored.
- Every following line is one guess. Lines that are empty after trimming whitespace are skipped.
- If the input has no lines at all, print nothing.

## Rules

A guess is valid when, after trimming, it is exactly 4 characters long and every character is one of `A` to `F`. Anything else is invalid.

For a valid guess:

- black = the number of positions where the guess and the secret have the same letter.
- white = the number of additional letters that are right but in the wrong position. Count it as follows: for each letter `A` to `F`, take the smaller of how many times it occurs in the secret and how many times it occurs in the guess, and add these up to get the total matches; white = total matches - black.

## Output

One line per non-skipped guess, in input order, using the trimmed guess text:

- valid guess: `GUESS B W` (guess, black, white, separated by single spaces). If black is 4, append ` solved`, giving `GUESS 4 0 solved`.
- invalid guess: `GUESS invalid`

## Example

Input:

```
ABCD
AABB

DCBA
ABCD
ABCDE
AAAA
```

Output:

```
AABB 1 1
DCBA 0 4
ABCD 4 0 solved
ABCDE invalid
AAAA 1 0
```
