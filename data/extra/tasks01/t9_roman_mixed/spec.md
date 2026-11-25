# roman_mixed

Normalize a list whose items are numbered with a mix of arabic and roman numerals.

Input: one item per line, written `NUMBER. TEXT`: a numeral, a period, then the text (the text may be empty, and spaces after the period and at the end of the line are ignored). Empty lines are ignored but still count for line numbers (the first line is line 1). A numeral is either
- arabic: digits only, value 1 to 3999, no leading zero; or
- roman: the capital letters `I V X L C D M` in canonical form, value 1 to 3999 (so `IIII`, `VX`, `IC` and lowercase are not valid; the canonical form is the standard subtractive one such as `XIV`, `MCMXCIV`).

A line without a period, or with an invalid numeral before its first period, is invalid.

Output: first the valid items sorted by numeric value (items with equal value keep input order), one per line as `ARABIC ROMAN TEXT` (the value in arabic, the value in canonical roman, then the text), with trailing spaces removed. Then, for each invalid line in input order, `invalid line K: LINE` where LINE is the line as given.

Example input:
```
XIV. Conclusion
2. Method
iv. Notes
3. Results
IX. Appendix
```
Example output:
```
2 II Method
3 III Results
9 IX Appendix
14 XIV Conclusion
invalid line 3: iv. Notes
```
