# Bowling score per line

Standard input: each line is one complete ten-frame game of bowling, as the pins knocked down by each roll, separated by spaces.
Scoring is the usual one: a strike (10 on the first roll of a frame) scores 10 plus the next two rolls; a spare scores 10 plus the next roll;
an open frame scores its two rolls. The tenth frame gives bonus rolls after a strike (two) or a spare (one), and nothing else.

For every line print one result:
- the total score as a number, when the rolls form exactly one complete valid game;
- `incomplete` when the rolls are valid so far but the game has not finished (this includes an empty line);
- `invalid` when a token is not an integer from 0 to 10, when two rolls of one frame (other than a strike or the bonus rolls) sum above 10, or when rolls remain after the game is finished.
  Check the rolls in order: the first problem found decides, so `incomplete` is only printed when no `invalid` problem occurs before the rolls run out.

A final newline does not add a game; empty input prints nothing.

Example:
    input:  10 10 10 10 10 10 10 10 10 10 10 10
            9 0 9 0 9 0 9 0 9 0 9 0 9 0 9 0 9 0 9 0
            5 5 5
    output: 300
            90
            incomplete
