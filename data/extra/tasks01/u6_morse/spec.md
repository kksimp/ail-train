# morse

Reads commands from standard input, one per line, and prints one result line per command.

Alphabet: International Morse for the letters A-Z (`A` is `.-`, `B` is `-...`, ..., `Z` is `--..`) and the digits 0-9 (`0` is `-----`, `1` is `.----`, ..., `5` is `.....`, ..., `9` is `----.`).

Commands (command word, one space, then the argument, which is the rest of the line):
- `enc TEXT`: TEXT is split into words on spaces (runs of spaces count as one separator, leading and trailing spaces are ignored). Each letter (either case) or digit becomes its code, the codes of one word are joined by one space, and the words are joined by ` / `. If TEXT contains any other character the line prints `error`.
- `dec CODE`: CODE is split on spaces into tokens (extra spaces are ignored). Each token is a letter/digit code, or `/` meaning a word break, which becomes one space. Output is upper case. A token that is not a known code prints `error` for the whole line.
- Any other non-empty line prints `bad command`. Empty lines print nothing.

Example:
```
enc SOS 2024
dec ... --- ... / ..--- ----- ..--- ....-
```
prints
```
... --- ... / ..--- ----- ..--- ....-
SOS 2024
```
Empty input prints nothing.
