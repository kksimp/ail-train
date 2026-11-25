# Text wrapping to a width

The first input line holds the width N (an integer). The remaining lines are text, split into paragraphs by blank
lines (a line with no words is blank; several blank lines act as one separator; leading/trailing blank lines are
ignored). Words are runs of non-whitespace characters.

Wrap each paragraph greedily: put words on a line, separated by single spaces, as long as the line stays at most N
characters; otherwise start a new line. A word longer than N is placed alone on its own line, unbroken.
Print the wrapped paragraphs in order, with exactly one empty line between consecutive paragraphs.

If the first line is missing, is not an integer (an optional `-` and digits), or is less than 1, print `bad width`
and nothing else. A text with no words prints nothing.

Example input:

    10
    the quick  brown fox
    jumps

    over extraordinarily lazy dogs

Example output:

    the quick
    brown fox
    jumps

    over
    extraordinarily
    lazy dogs
