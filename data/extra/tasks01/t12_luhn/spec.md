# Luhn card number check

Reads card numbers from standard input, one per line, and classifies each.

Input: any number of lines. Lines that are empty after trimming spaces are skipped.

For each other line, trim leading and trailing whitespace, then remove every space and every `-` to get the digit string.
- If the digit string has fewer than 12 or more than 19 characters, or any character is not a digit `0`-`9`, the result is `MALFORMED`.
- Otherwise apply the Luhn checksum: from the rightmost digit moving left, double every second digit (the second from the right, the fourth, ...); if a doubled value exceeds 9 subtract 9; the number is `VALID` when the sum of all values is divisible by 10, else `INVALID`.

Output: one line per non-empty input line: the trimmed original line, then `: `, then the result.

Example input:
```
4539 1488 0343 6467
4539-1488-0343-6468
12345
```
Example output:
```
4539 1488 0343 6467: VALID
4539-1488-0343-6468: INVALID
12345: MALFORMED
```

Empty input prints nothing.
