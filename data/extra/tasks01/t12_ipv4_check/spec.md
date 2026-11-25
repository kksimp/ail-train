# IPv4 address validation

Reads one candidate IPv4 address per line, validates it and classifies the valid ones.

Input: any number of lines. Lines that are empty after trimming whitespace are skipped; each other line is trimmed first.

Validation: split the line on `.`. The first problem found, checking the parts left to right (and for each part in the order below), decides the result:
1. If there are not exactly 4 parts: `wrong part count` (checked before anything else).
2. A part is empty: `empty part`.
3. A part contains a character that is not a digit: `non-digit`.
4. A part has more than one digit and starts with `0`: `leading zero`.
5. A part is greater than 255: `out of range` (a part of more than 3 digits is also out of range).

Class of a valid address, first match wins, `a.b.c.d` being the numbers:
- `loopback` if `a` is 127
- `private` if `a` is 10, or `a` is 172 and `b` is 16-31, or `a` is 192 and `b` is 168
- `link-local` if `a` is 169 and `b` is 254
- `multicast` if `a` is 224-239
- `unspecified` if all four numbers are 0
- `public` otherwise

Output: one line per processed input line: `ADDRESS: valid CLASS` or `ADDRESS: invalid (REASON)`, where `ADDRESS` is the trimmed line.

Example input:
```
192.168.1.20
8.8.8.256
1.2.3
```
Example output:
```
192.168.1.20: valid private
8.8.8.256: invalid (out of range)
1.2.3: invalid (wrong part count)
```

Empty input prints nothing.
