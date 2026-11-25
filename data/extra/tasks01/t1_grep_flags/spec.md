# Grep-like filter with flags

The first input line is `FLAGS PATTERN`: a flags word, one space, then the pattern (the rest of the line, which
may itself contain spaces; it is a literal substring, not a regular expression). All later lines are searched.

FLAGS is either `-` (no flags) or a word made of the letters `i`, `v`, `n`, `c` (each may repeat):

    i   ignore ASCII case when matching
    v   invert: select the lines that do NOT contain the pattern
    n   prefix each printed line with its 1-based line number (counting data lines after the first) and a colon: `3:text`
    c   print only the number of selected lines, nothing else

A line is selected when it contains the pattern (with `v`: when it does not). Print the selected lines in order.

Errors, checked in this order, each printing one phrase and nothing else: if the first line has no space or the
pattern is empty, print `bad pattern`; otherwise if FLAGS has any other letter, print `bad flags`.

Example input:

    in the
    The rain in Spain
    stays mainly
    IN the plain

    nothing

Example output (flags `in` = ignore case plus line numbers, pattern `the`):

    1:The rain in Spain
    3:IN the plain
