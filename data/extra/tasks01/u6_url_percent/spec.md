# url percent-encoding

Reads commands from standard input, one per line, and prints one result line per command.

Commands (command word, one space, then the argument, which is the rest of the line and may be empty or contain spaces):
- `enc TEXT`: percent-encodes TEXT, which is printable ASCII. The letters `A-Z a-z`, digits, and the characters `-` `.` `_` `~` stay as they are; every other character becomes `%` and the two-digit upper-case hexadecimal of its ASCII code (a space is `%20`).
- `dec TEXT`: decodes TEXT. `%XX` (two hex digits, either case) becomes the character with that code; `+` becomes a space; every other character stays. The line prints `invalid` if a `%` is not followed by two hex digits, or if a decoded `%XX` code is outside 32 to 126.
- Any other non-empty line prints `bad command`. Empty lines print nothing.

Example:
```
enc a b&c=d/e
dec hello%20world%21+ok
dec 100%
```
prints
```
a%20b%26c%3Dd%2Fe
hello world! ok
invalid
```
Empty input prints nothing.
