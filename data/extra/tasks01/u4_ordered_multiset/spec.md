# Ordered multiset with rank queries

Read commands from standard input, one per line, and maintain a multiset of integers (duplicates allowed), initially empty.
Words are separated by spaces; blank lines are ignored.

Commands and output (one output line per command):
- `add X`: insert one copy of X. Prints `ok`.
- `remove X`: remove one copy of X; prints `ok`, or `missing` if X is not present.
- `count X`: print how many copies of X are stored.
- `rank X`: print how many stored values are strictly smaller than X (X need not be present).
- `kth K`: print the K-th smallest value counting duplicates, K starting at 1; prints `none` if K is less than 1 or larger than the size.
- `floor X`: print the largest stored value that is <= X, or `none`.
- `ceil X`: print the smallest stored value that is >= X, or `none`.
- `size`: print the total number of stored values.

Any other line (unknown command, missing or non-integer argument, extra words) prints `error` and changes nothing.

Example input:
    add 5
    add 3
    add 5
    add 9
    rank 5
    kth 3
    count 5
    remove 5
    floor 8
    ceil 6
Output:
    ok
    ok
    ok
    ok
    1
    5
    2
    ok
    5
    9
