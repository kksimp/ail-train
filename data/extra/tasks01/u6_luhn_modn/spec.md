# luhn mod n

Computes and checks Luhn mod N check characters. Reads commands from standard input, one per line, fields separated by single spaces, and prints one result line per command.

The alphabet for base N is the first N characters of `0123456789abcdefghijklmnopqrstuvwxyz` (lower case only). N is 10, 16 or 36. A character's code point is its position in the alphabet.

Commands:
- `gen N STR`: STR is the payload (at least one alphabet character). Prints the check character. Algorithm: go through STR from right to left with factor 2 for the first character and alternating 2, 1, 2, ...; the addend is factor times the code point, and its contribution is (addend div N) + (addend mod N); sum the contributions; the check code point is (N - sum mod N) mod N.
- `chk N STR`: STR is the payload followed by its check character (at least two alphabet characters). Prints `valid` if the same sum over the whole STR, but with factor 1 for the last character and alternating 1, 2, 1, ... from right to left, is divisible by N, else `invalid`.
- If N is not 10, 16 or 36, or STR is missing, too short, or has a character outside the alphabet for N, the line prints `error`. Any other non-empty line (unknown command, wrong number of fields) prints `bad command`. Empty lines print nothing.

Example:
```
gen 10 7992739871
chk 10 79927398713
gen 16 abcdef012345
chk 16 abcdef0123453
```
prints
```
3
valid
3
valid
```
Empty input prints nothing.
