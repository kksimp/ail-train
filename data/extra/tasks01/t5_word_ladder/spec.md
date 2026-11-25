Standard input: the first non-blank line holds two words `START END`. Every following non-blank line (trimmed) is one dictionary word.
All words are lowercase. Two words are neighbours if they have the same length and differ in exactly one position.
START itself is always usable even if it is not in the dictionary; END must be in the dictionary (or equal START).

Find the shortest ladder from START to END where each step moves to a neighbour that is in the dictionary.
To make the answer unique, search breadth-first from START, visiting each word's neighbours in byte-sorted order,
and remember for every word the first word that reached it; the ladder is the path of those parents.
Print `length: L` (the number of words in the ladder, START and END included) and then `path: ` followed by the words
joined with ` -> `. If there is no ladder print `no ladder`.
If the first non-blank line is not exactly two words (including empty input) print `bad input`.

Example input:
```
hit cog
hot
dot
dog
lot
log
cog
```
Output:
```
length: 5
path: hit -> hot -> dot -> dog -> cog
```
