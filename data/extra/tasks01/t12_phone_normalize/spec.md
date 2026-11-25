# Phone number normalization

Reads phone numbers, one per line, and rewrites valid ones in a single canonical form.

Input: any number of lines. Lines that are empty after trimming whitespace are skipped.

For each other line, trim it, then process it as follows:
- The only allowed non-digit characters are the separators space, `-`, `.`, `(` and `)` (ignored), and a single `+` which must be the very first character. Any other character makes the number invalid.
- Collect the digits. If the line started with `+`, the digits must be `1` followed by exactly 10 digits; drop the leading `1`.
- Without a `+`: 10 digits are used as is; 11 digits starting with `1` drop that `1`; any other count is invalid.
- The remaining 10 digits are `AAA BBB CCCC`. The first digit of `AAA` and the first digit of `BBB` must each be `2`-`9`, otherwise the number is invalid.

Output: one line per processed input line: the trimmed original, ` -> `, then `+1-AAA-BBB-CCCC` for a valid number or `INVALID`.

Example input:
```
(415) 555-2671
1.800.555.0199
+44 20 7946 0958
```
Example output:
```
(415) 555-2671 -> +1-415-555-2671
1.800.555.0199 -> +1-800-555-0199
+44 20 7946 0958 -> INVALID
```

Empty input prints nothing.
