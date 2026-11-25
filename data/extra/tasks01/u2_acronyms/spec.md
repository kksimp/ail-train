# Acronym extraction

Find acronyms in the text on standard input. Split every line into maximal runs of ASCII letters
(any other character, including digits and punctuation, separates runs). A run is an acronym if it has
2 to 6 letters and all of them are upper case.

Print one line `ACRONYM COUNT FIRSTLINE` for each distinct acronym, in order of first appearance, where
COUNT is its number of occurrences and FIRSTLINE the 1-based number of the line where it first appears.
Then print `total=T distinct=D`. If there are no acronyms print only `no acronyms`.

Example input:
The NASA and ESA teams met.
NASA uses GPS; B2B is not one. OK

Example output:
NASA 2 1
ESA 1 1
GPS 1 2
OK 1 2
total=5 distinct=4
