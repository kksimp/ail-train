# Binary search queries

The first input line holds a non-decreasing list of integers separated by spaces (it may be empty, meaning an empty
list; duplicates are allowed). Every later line is one query:

- `find X`: print the 0-based index of the first occurrence of X, or `-1` if X is absent.
- `lower X`: print the index of the first element that is >= X (the list length if there is none).
- `upper X`: print the index of the first element that is > X (the list length if there is none).
- `count X`: print how many elements equal X.

X is an integer (optional `-` then digits). Any other non-blank line (unknown command, missing or non-integer
argument, extra words) prints `error line N`, where N is the 1-based input line number. Blank query lines are skipped.
Each valid query prints exactly one line with its answer.

Example input:
```
1 2 2 2 5 9
find 2
find 3
lower 3
upper 2
count 2
count 7
oops
```
Output:
```
1
-1
4
4
3
0
error line 8
```
Empty input prints nothing.
