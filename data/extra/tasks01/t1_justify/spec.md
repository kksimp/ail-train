# Full justification

The first input line holds the width N (an integer). All remaining lines together form one text; its words are the
runs of non-whitespace characters, in order (line breaks do not matter).

Break the words into lines greedily: a line takes words while the words plus one space between each pair fit in
N characters; otherwise a new line starts. Then justify every line except the last: pad the gaps between its words
with spaces so the line is exactly N characters wide. Every gap gets the same number of spaces, and when the extra
spaces do not divide evenly, the leftmost gaps get one more space each.

The last line, any line with a single word, and any word longer than N are printed as they are (no padding).
If the first line is missing, not an integer (optional `-`, digits) or less than 1, print `bad width` and nothing
else. A text with no words prints nothing.

Example input:

    16
    This is an example of text
    justification.

Example output (lines 1 and 2 are padded to 16 characters; the first has 4 spaces per gap, the second 2 then 1):

    This    is    an
    example  of text
    justification.
