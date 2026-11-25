# Stop-word filtered vocabulary

Standard input: line 1 is a comma-separated list of stop words (may be empty; entries are trimmed and
lower-cased; empty entries are ignored). All remaining lines are text.

Words of the text are maximal runs of ASCII letters after lower-casing (any other character, such as an
apostrophe, digit or hyphen, separates words). A word whose text is a stop word is dropped.

Print one line `WORD COUNT` for every remaining distinct word, most frequent first, ties in ascending byte order of the
word. Then print `total=N unique=U stopped=S`: N is the number of kept word occurrences, U the number of distinct kept
words and S the number of occurrences dropped as stop words.

Edge cases: completely empty input prints `no input`.

Example input:
the, a
The cat and a hat; the end.

Example output:
and 1
cat 1
end 1
hat 1
total=4 unique=4 stopped=3
