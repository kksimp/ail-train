# Text statistics

Read all of standard input. Lines are separated by `\n`; a final line ending does not start another line, so empty
input has 0 lines and the input `\n` has 1 (empty) line. A word is a maximal run of non-whitespace characters
(whitespace is space or tab). Characters are counted per line, not counting the line ending.

Print exactly these five lines:

    lines: N              number of lines
    words: N              total number of words
    chars: N              total number of characters over all lines
    blank: N              number of lines that contain no words (empty, or only spaces/tabs)
    longest: L (line K)   the greatest line length L and the 1-based number K of the first line with that length

With no lines at all, print `longest: 0 (line 0)`.

Example input (the second line is empty, the third is `a  b   c`):

    hello world

    a  b   c

Example output:

    lines: 3
    words: 5
    chars: 19
    blank: 1
    longest: 11 (line 1)
