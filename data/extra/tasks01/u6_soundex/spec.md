# soundex

Reads lines from standard input. Each non-empty line holds words separated by spaces (runs of spaces count as one; leading and trailing spaces are ignored). For every non-empty line print the American Soundex code of each of its words, separated by single spaces. Lines that are empty print nothing.

Soundex of a word:
1. Ignore every character that is not an ASCII letter and treat letters as upper case. If no letter is left the code is `----`.
2. The code starts with the first letter.
3. Letters map to digits: B F P V -> 1; C G J K Q S X Z -> 2; D T -> 3; L -> 4; M N -> 5; R -> 6. The letters A E I O U Y have no digit and neither do H and W.
4. Going through the remaining letters in order, a letter with a digit is appended unless its digit equals the digit of the previous letter (the previous letter's digit counts, with the first letter's digit counting for the second letter). A vowel (A E I O U Y) resets the previous digit to none, so the same digit may appear again after it; H and W are skipped entirely and leave the previous digit unchanged.
5. The code is cut or padded with `0` to a letter plus three digits.

Example:
```
Robert Rupert Ashcraft
Pfister Tymczak o'brien
```
prints
```
R163 R163 A261
P236 T522 O165
```
Empty input prints nothing.
