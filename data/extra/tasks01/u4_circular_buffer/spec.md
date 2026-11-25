# Circular buffer

The first line holds the capacity C (an integer 1 to 100). The buffer starts empty and keeps at most C integers.
Every following line is a command; blank lines are ignored. Words are separated by spaces.

Commands and output (one output line per command):
- `push N`: append N at the newest end. If the buffer is already full the oldest value is overwritten and `overwrote X` is printed (X is the discarded value); otherwise `ok`.
- `pop`: remove and print the oldest value, or `empty`.
- `peek`: print the oldest value without removing it, or `empty`.
- `dump`: print the contents from oldest to newest separated by single spaces, or `empty`.
- `size`: print how many values are stored.
- `sum`: print the sum of the stored values.

Any other line (unknown command, missing or non-integer N, extra words) prints `error` and changes nothing.
If the first line is not an integer from 1 to 100, print `bad capacity` and nothing else.

Example input:
    3
    push 1
    push 2
    push 3
    push 4
    dump
    pop
    sum
Output:
    ok
    ok
    ok
    overwrote 1
    2 3 4
    2
    7
