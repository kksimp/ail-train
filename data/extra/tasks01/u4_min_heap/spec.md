# Min-heap commands

Read commands from standard input, one per line, and operate on a min-heap of integers that starts empty.
Words are separated by spaces; blank lines are ignored.

Commands and output (one output line per command):
- `push N`: insert the integer N. Prints `ok`.
- `pop`: remove the smallest value and print it; prints `empty` if the heap is empty.
- `peek`: print the smallest value without removing it; prints `empty` if the heap is empty.
- `size`: print the number of values in the heap.
- `drain`: remove all values and print them smallest first, separated by single spaces; prints `empty` if there are none.

Any other line (unknown command, missing or non-integer N, extra words) prints `error` and changes nothing.
Duplicates are kept. N may be negative.

Example input:
    push 5
    push 2
    peek
    pop
    pop
    pop
Output:
    ok
    ok
    2
    2
    5
    empty
