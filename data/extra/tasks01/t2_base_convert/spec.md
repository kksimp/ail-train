# base_convert

Answers base-conversion queries, one per line.

Input: each line is `FROM TO VALUE`: FROM and TO are bases written in decimal (2 to 36), VALUE is a non-negative number written in base FROM using digits `0-9` and letters `a-z` (upper-case letters are accepted too and mean the same). Fields are separated by one or more spaces. Empty lines are skipped silently.

Output: for each query, one line with VALUE converted to base TO using lower-case letters and no leading zeros (zero prints `0`). Values fit in 62 bits.

Error lines (the query is not answered, and the error is printed instead, with K the 1-based physical line number):
- `line K: bad format` if the line does not have exactly three fields or FROM/TO is not a decimal integer.
- `line K: bad base` if FROM or TO is outside 2..36 (checked first).
- `line K: bad digit C` if VALUE contains a character C (shown in lower case) that is not a valid digit for base FROM; the first offending character is reported. An empty VALUE cannot occur since the line would then have two fields.

Finally print `ok N errors M`.

Example input:
```
10 2 37
16 10 ff
2 16 1111111
8 10 9
```
Output:
```
100101
255
7f
line 4: bad digit 9
ok 3 errors 1
```
