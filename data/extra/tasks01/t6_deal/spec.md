# Card dealing with a seeded generator

Standard input: each line is one deal request `SEED PLAYERS CARDS` (three integers separated by spaces).

Build the 52-card deck in this order: for each suit in the order `S H D C`, the ranks `A 2 3 4 5 6 7 8 9 T J Q K` (so the deck starts `AS 2S 3S ...` and ends `... QC KC`).
Shuffle it with a linear congruential generator: `state = SEED mod 2147483648`; each step does `state = (state * 1103515245 + 12345) mod 2147483648` and returns the new state.
Fisher-Yates: for `i` from 51 down to 1, take `r = next()`, `j = r mod (i + 1)`, and swap deck positions `i` and `j`.
Then deal round robin from the top (position 0): player 1 gets card 0, player 2 card 1, and so on, until every player holds CARDS cards.

For the k-th line (counting from 1) print `deal k`, then one line per player `P<n>: <cards in the order dealt, separated by spaces>`, then `left=<cards remaining in the deck>`.
If the line is not exactly three integers, or SEED < 0, or PLAYERS < 1 or CARDS < 1, or PLAYERS * CARDS > 52, print the single line `deal k: bad request` instead.
Blank lines are bad requests too. Empty input prints nothing.

Example (the shuffle depends on the generator, so the real output is checked by running):
    input:  7 2 3
    output: deal 1
            P1: <3 cards>
            P2: <3 cards>
            left=46
