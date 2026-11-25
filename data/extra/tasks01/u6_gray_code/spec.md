# gray code

Reads commands from standard input, one per line, and prints one result line per command.

Commands: a command word, one space, then one argument.
- `bin N`: N is a decimal number from 0 to 4294967295 (digits only, at most 10 of them, leading zeros allowed). Prints N in binary without leading zeros (`0` for zero).
- `dec BITS`: BITS is 1 to 32 characters, each `0` or `1`. Prints its value in decimal.
- `gray N`: N as for `bin`. Prints the reflected binary Gray code of N (N xor N shifted right by 1) in binary without leading zeros.
- `ungray BITS`: BITS as for `dec`, read as a Gray code. Prints the decimal number whose Gray code it is.
- A line whose command word is known but whose argument is not valid prints `error`; any other non-empty line (unknown command word, or no argument) prints `bad command`. Empty lines print nothing.

Example:
```
bin 10
gray 10
ungray 1111
dec 1010
gray 4294967296
```
prints
```
1010
1111
10
10
error
```
Empty input prints nothing.
