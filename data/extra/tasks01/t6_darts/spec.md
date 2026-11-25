# Darts scoring (301, double out)

Standard input: each line is one single-player game, the darts thrown in order, separated by spaces. A player starts at 301 and counts down to exactly 0.
A dart token is: `S1`..`S20` (single, face value), `D1`..`D20` (double, twice the value), `T1`..`T20` (triple, three times), `25` (outer bull, 25), `B` (bullseye, 50, counts as a double), or `M` (miss, 0).
Darts are thrown in turns of three. A dart that would leave the score below 0, at exactly 1, or at exactly 0 without being a double or `B`, is a bust:
the whole turn is void (the score returns to what it was before the turn's first dart) and the turn's remaining darts are thrown but score nothing. The next turn starts after the third dart.
Reaching exactly 0 with a double or `B` finishes the game at once.

For each line print `finished in N darts` (N counts every dart thrown up to and including the finishing one), or `remaining R after N darts` when the line ends without a finish
(N = number of tokens on the line, R the score then; a half-finished turn counts as it stands). Print `invalid` when any token is not in the list above or when any dart follows the finishing dart.
An empty line is a game with no darts: `remaining 301 after 0 darts`. A final newline does not add a game; empty input prints nothing.

Example:
    input:  T20 T20 T20 T20 S1 S20 D20
            T20 T20 T20 S1 S1 S1
    output: finished in 7 darts
            remaining 118 after 6 darts
