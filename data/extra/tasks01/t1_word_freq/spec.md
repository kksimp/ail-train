# Word frequency table

Read all of standard input as text. A word is a maximal run of ASCII letters (A-Z, a-z); every other character
(digits, punctuation, spaces, newlines) separates words. Words are compared in lower case.

Print the 5 most frequent words, one per line, as `word count` (a single space between). Order by count
descending; words with equal counts are ordered alphabetically (byte order). If fewer than 5 distinct words
exist, print all of them.

If the input contains no words, print `no words`.

Example input:

    The cat and the hat.
    THE end, and so on: cat!

Example output:

    the 3
    and 2
    cat 2
    end 1
    hat 1

Digits are not letters, so `abc123def` is two words, `abc` and `def`. Apostrophes also separate: `don't` is `don`, `t`.
