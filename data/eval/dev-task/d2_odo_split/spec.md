# odo_split

Write a command-line program that reads a sequence of odometer readings from standard input and splits them into trips.

## Input

Zero or more lines, each normally holding one odometer reading: a non-negative whole number of kilometres written with the digits `0`-`9` only (at most 9 digits, leading zeros allowed), possibly surrounded by spaces or tabs. Any other line (blank, letters, a sign, decimals, several words) is not a reading and is ignored silently.

## Rules

Process the readings in order, remembering the previous accepted reading `prev` (none at the start), the current trip's distance `dist` and its number of legs `legs` (both start at 0).

For each reading `r`:
1. If `r < prev`, the reading is a fault: ignore it completely (`prev` does not change).
2. If `r == prev` (the vehicle did not move), the current trip ends. If it has at least one leg, print it (see below) and start a new trip with `dist = 0`, `legs = 0`. If it has no legs, nothing is printed. `prev` stays `r`.
3. If `r > prev` and there is a previous reading, this is a leg: add `r - prev` to `dist` and 1 to `legs`; then `prev = r`.
4. The very first accepted reading just sets `prev`.

At the end of input, a current trip with at least one leg is printed too. Trips are numbered from 1 in the order printed.

## Output

For each trip: `trip N: D km in L legs` (always the word `legs`, even when L is 1). Finally `trips T` with the number of trips printed (`trips 0` for empty input).

## Example

Input:

    1000
    1040
    abc
    1075
    1075
    1075
    1070
    1100
    1130
    -5
    1130
    1131

Output:

    trip 1: 75 km in 2 legs
    trip 2: 55 km in 2 legs
    trip 3: 1 km in 1 legs
    trips 3
