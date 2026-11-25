# Poker hand ranking

Standard input: each line is one five-card poker hand, cards separated by spaces. A card is two characters: a rank
(`2 3 4 5 6 7 8 9 T J Q K A`) followed by a suit (`S H D C`), all upper case, e.g. `TH` is the ten of hearts.

For each line print the category of the hand, one of (best first):
`straight flush`, `four of a kind`, `full house`, `flush`, `straight`, `three of a kind`, `two pair`, `pair`, `high card`.
A straight is five consecutive ranks; the ace counts high (`TJQKA`) or low (`A2345`); there is no wrap-around (`QKA23` is not a straight).
A straight flush is a straight whose cards share one suit (a royal flush is just a straight flush).

Print `invalid` instead when the line does not hold exactly five cards, a card is not a valid rank and suit, or the same card appears twice.
Empty lines are hands too (`invalid`). A final newline does not add a line; empty input prints nothing.

Example:
    input:  AS KS QS JS TS
            2H 2D 2C KD KS
            2H 3D 5C 9S KD
    output: straight flush
            full house
            high card
