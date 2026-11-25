# Licence plate pattern classes

Reads licence plates, one per line, and assigns each to a pattern class.

Input: any number of lines. Lines that are empty after trimming whitespace are skipped; each other line is trimmed first.

Describe a plate by its shape: every uppercase letter `A`-`Z` becomes `L`, every digit becomes `D`, and every other character stays as it is (so lowercase letters, spaces and punctuation stay).

Class, first match wins:
- `classic`: shape is `LLL-DDD`
- `euro`: shape is `LL-DD-LL`
- `californian`: shape is `DLLLDDD`
- `vanity`: shape has 2 to 7 characters, all `L` or `D`, and starts with `L`
- `invalid`: anything else

Output: one line per processed input line: the trimmed plate, `: `, the class.

Example input:
```
ABC-123
AB-12-CD
7ABC123
LOVE2U
abc-123
```
Example output:
```
ABC-123: classic
AB-12-CD: euro
7ABC123: californian
LOVE2U: vanity
abc-123: invalid
```

Empty input prints nothing.
