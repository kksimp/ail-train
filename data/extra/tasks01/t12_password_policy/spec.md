# Password policy checker

Reads candidate passwords from standard input, one per line, and reports which policy rules each one breaks.

Input: any number of lines (ASCII). Empty lines are skipped. A line is the password exactly as written: do not trim it.

Rules, checked in this order (the rule names are the output tokens):
1. `short`: fewer than 8 characters.
2. `no-upper`: no uppercase letter `A`-`Z`.
3. `no-lower`: no lowercase letter `a`-`z`.
4. `no-digit`: no digit `0`-`9`.
5. `no-symbol`: no character that is neither a letter, a digit nor a space.
6. `space`: contains a space.
7. `repeat`: three or more identical characters in a row (e.g. `aaa`).

Output: one line per non-empty input line. If no rule is broken print `PASSWORD: OK`. Otherwise print `PASSWORD: FAIL ` followed by the broken rule names in the order above, separated by commas, with `PASSWORD` replaced by the input line.

Example input:
```
Abcdef1!x
abc
Aaa111!!!z
```
Example output:
```
Abcdef1!x: OK
abc: FAIL short,no-upper,no-digit,no-symbol
Aaa111!!!z: FAIL repeat
```

Empty input prints nothing.
