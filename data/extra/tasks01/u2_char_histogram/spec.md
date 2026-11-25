# Character class histogram

Count the characters of standard input (the whole text, newlines included) in seven classes:
`upper` (A-Z), `lower` (a-z), `digit` (0-9), `space` (space and tab), `newline` (the line feed), `punct` (every other
character with code 33 to 126) and `other` (everything else).

Let M be the largest of the seven counts. Print the seven classes in the fixed order above, one per line, as the class name
padded to 8 characters (left-aligned), the count right-aligned in 4 columns, and, if the count is positive,
a space and a bar of `#` characters of length ceil(count * 20 / M) (integer arithmetic: (count * 20 + M - 1) / M).
There is no trailing space on lines without a bar. Then print `total=N`, the total number of characters.

If the input is empty print only `no input`.

Example input (one line, ended by a newline):
Hi, 2 U!

Example output (the input has 9 characters):
upper      2 ####################
lower      1 ##########
digit      1 ##########
space      2 ####################
newline    1 ##########
punct      2 ####################
other      0
total=9
