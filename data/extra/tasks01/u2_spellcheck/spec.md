# Simple spell check against a word list

Standard input has two parts separated by a line that is exactly `---` (after trimming spaces and tabs).
The lines before it are the dictionary: each is trimmed and lower-cased, and empty lines are ignored.
The lines after it are the text, numbered from 1 starting with the first line after the separator.

In each text line, words are maximal runs of ASCII letters. A word is misspelled when its lower-case form is not in the
dictionary. Print every misspelled word occurrence in order as `LINE:COL WORD`, where COL is the 1-based character
column in its line where the word starts and WORD is the word as written (original case).
Then print `misspelled=K unique=U`, K the number of misspelled occurrences and U the number of distinct
misspelled words (compared in lower case). If K is 0 print only `all words ok`.

If the input has no separator line print `bad input`.

Example input:
cat
sat
the
---
The cat sad.
Teh Cat sat

Example output:
1:9 sad
2:1 Teh
misspelled=2 unique=2
