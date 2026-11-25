# Run-length encoding and decoding

The first input line is the mode: `encode` or `decode`; anything else (or empty input) prints `bad mode` and nothing
else. Each following line is processed on its own and produces exactly one output line.

encode: replace every maximal run of one repeated character by the run length in decimal followed by that character
(`aaabcc` becomes `3a1b2c`; a space is a character like any other). A line that contains a decimal digit cannot be
encoded: its output is `error`. An empty line encodes to an empty line.

decode: the line must be a sequence of groups, each a count (one or more digits, not starting with `0`) followed by
one non-digit character, which is repeated count times (`3a1b2c` becomes `aaabcc`). Any other line (a count with no
character after it, a character with no count, a count starting with `0`) decodes to `error`. An empty line decodes to
an empty line.

Example input:

    encode
    aaabcc
    hello  world
    x1y
    

Example output:

    3a1b2c
    1h1e2l1o2 1w1o1r1l1d
    error
    
(the last input line is empty and so is the last output line)
