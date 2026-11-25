# roman

Converts between decimal numbers and Roman numerals, one token per line.

Input: each line holds one token after trimming whitespace; empty lines are skipped silently. A token is either a decimal number (digits only) or a Roman numeral (upper-case letters only).

Output, per non-empty line:
- Decimal token with value 1 to 3999: the canonical Roman numeral (subtractive form: 4=IV, 9=IX, 40=XL, 90=XC, 400=CD, 900=CM). Leading zeros are allowed in the input (`007` is 7).
- Roman token made only of the letters I V X L C D M: its value, but only if it is canonical, i.e. converting the value back gives exactly the same text; otherwise print `line K: not canonical TOKEN`. The empty case cannot occur.
- Decimal token outside 1..3999: `line K: out of range`.
- Anything else: `line K: invalid`.
K is the 1-based physical line number.

Finally print `converted N` with the number of successful conversions.

Example input:
```
1994
MCMXCIV
IIII
0
hello
```
Output:
```
MCMXCIV
1994
line 3: not canonical IIII
line 4: out of range
line 5: invalid
converted 2
```
