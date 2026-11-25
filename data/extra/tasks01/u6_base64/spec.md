# base64 tool

Reads commands from standard input, one per line, and prints one result line per command.

Commands (the command word, then one space, then the argument, which is the rest of the line and may contain spaces):
- `enc TEXT`: prints the standard Base64 encoding of TEXT (alphabet `A-Za-z0-9+/`, padded with `=`). TEXT is printable ASCII.
- `dec DATA`: prints the decoded text, or `invalid` if DATA is not valid Base64. DATA is valid when its length is a multiple of 4, every character is in the alphabet except that 1 or 2 `=` may end it, and every decoded byte is printable ASCII (codes 32 to 126). Unused low bits of the last group are ignored.
- Any other non-empty line prints `bad command`. A command word with no argument (`enc` alone) has an empty argument.
- Empty lines print nothing.

Example:
```
enc Hello
dec SGVsbG8=
dec SGVsbG8
```
prints
```
SGVsbG8=
Hello
invalid
```
Empty input prints nothing.
