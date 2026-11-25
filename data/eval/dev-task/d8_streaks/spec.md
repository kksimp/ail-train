# streaks

Reads a win/loss record and reports streak lengths.

## Input

One line of results, each a single character: `W` (win) or `L` (loss), in the order played, with no separators. Leading and trailing spaces on the line are ignored. Only the first line is read.

## Rules

1. If the line is missing or empty (after ignoring spaces), print `no games` and stop.
2. If the line contains any character other than `W` and `L` (lowercase letters count as other), print `bad result: C`, where C is the first such character, and stop.
3. A streak is a maximal run of the same result. Find the longest streak of wins, the longest streak of losses (0 if there are none), and the current streak (the final run of the line).

## Output

Four lines:

```
games: N
longest W: A
longest L: B
current: R M
```

N is the number of games, A and B the longest streak lengths, R the last result (`W` or `L`) and M the length of the final run.

## Example

Input:

```
WWLWWWLLWW
```

Output:

```
games: 10
longest W: 3
longest L: 2
current: W 2
```
