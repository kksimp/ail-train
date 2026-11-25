# Word n-gram counts

The first line of standard input is an integer N (1, 2 or 3). All remaining lines are text.

Words are the whitespace-separated tokens of the text lines, converted to lower case (ASCII letters only).
An n-gram is N consecutive words joined by single spaces. Count how often each distinct n-gram occurs
(overlapping n-grams all count).

Output: the five most frequent n-grams, most frequent first, ties broken by n-gram text in ascending
byte order (fewer than five lines if fewer distinct n-grams exist). Each line is `COUNT GRAM`.
Then one final line `distinct=D total=T`, where D is the number of distinct n-grams and T the total
number of n-grams counted.

Edge cases:
- Empty input (no lines at all): print `no input`.
- The first line is not 1, 2 or 3 (after trimming spaces): print `bad n`.
- Fewer than N words: print only `distinct=0 total=0`.

Example input:
2
the cat and The cat sat

Example output:
2 the cat
1 and the
1 cat and
1 cat sat
distinct=4 total=5
