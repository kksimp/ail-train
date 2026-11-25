# Union-find queries

The first line holds N (1 <= N <= 1000): elements are numbered 0 to N-1, each starting alone in its own set.
Every following line is a command; blank lines are ignored. Words are separated by spaces.

Commands and output (one output line per command):
- `union A B`: merge the sets of A and B; prints `merged`, or `same` if they were already together.
- `find A B`: prints `yes` if A and B are in the same set, else `no`.
- `size A`: prints the number of elements in A's set.
- `count`: prints the current number of sets.
- `largest`: prints the size of the biggest set.

A command whose element is not an integer in 0..N-1, or any other line (unknown command, wrong number of words) prints `error` and changes nothing.
If the first line is not a valid N, print `bad header` and nothing else.

Example input:
    5
    union 0 1
    union 1 2
    find 0 2
    size 2
    count
    union 0 2
Output:
    merged
    merged
    yes
    3
    3
    same
