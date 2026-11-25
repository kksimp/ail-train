# Top-k frequent words

The first input line is an integer K (digits only, K >= 1, surrounding spaces ignored). If it is not such an
integer (or the input is empty), print `bad k` and stop.

All remaining lines are text. A word is a maximal run of ASCII letters (`a`-`z`, `A`-`Z`); every other character
(digits, punctuation, spaces, apostrophes) separates words. Words are compared in lowercase.

Print the K most frequent words, one per line, as `WORD COUNT`, ordered by count descending and, for equal counts,
by word ascending (byte order). If there are fewer than K distinct words, print all of them. If the text has no
words, print nothing after the first line check.

Example input:
```
3
The cat and the hat. The END, and the cat!
```
Output:
```
the 4
and 2
cat 2
```
(`hat` and `end` appear once and rank below the three shown.)
