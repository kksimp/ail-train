# Interval set add, remove and query

Maintain a set of integer points described by half-open intervals [L, R) (L included, R excluded). It starts empty.
Read commands from standard input, one per line. Words are separated by spaces; blank lines are ignored.

Commands and output (one output line per command):
- `add L R`: add every integer point from L up to but not including R to the set. Prints `ok`.
- `remove L R`: remove those points from the set. Prints `ok`.
- `query X`: prints `yes` if the point X is in the set, else `no`.
- `total`: prints how many integer points are in the set.
- `show`: prints the set as maximal runs, in ascending order, formatted `[L,R)` and separated by single spaces; touching or overlapping intervals are merged (so `[1,3)` and `[3,5)` appear as `[1,5)`). Prints `empty` for an empty set.

For `add` and `remove` the interval must satisfy L < R, otherwise print `bad` and change nothing. Any other line (unknown command, missing or non-integer argument, extra words) prints `error` and changes nothing. Negative values are allowed.

Example input:
    add 1 5
    add 8 10
    remove 3 9
    show
    total
    query 2
    query 9
    add 5 8
    show
Output:
    ok
    ok
    ok
    [1,3) [9,10)
    3
    yes
    yes
    ok
    [1,3) [5,8) [9,10)
