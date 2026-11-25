# Deque operations

Read commands from standard input, one per line, and operate on a double-ended queue of integers, initially empty.
Words are separated by spaces; blank lines are ignored.

Commands and output (one output line per command):
- `push_front N` / `push_back N`: add N at that end. Prints `ok`.
- `pop_front` / `pop_back`: remove and print the value at that end, or `empty` if the deque is empty.
- `front` / `back`: print the value at that end without removing it, or `empty`.
- `rotate K`: K is an integer (possibly negative). A positive K moves the K front values, one at a time, to the back; a negative K moves |K| back values, one at a time, to the front. K is taken modulo the size, so any magnitude works; on an empty deque nothing happens. Prints `ok`.
- `reverse`: reverse the order. Prints `ok`.
- `show`: print the values from front to back separated by single spaces, or `empty`.

Any other line (unknown command, missing or non-integer argument, extra words) prints `error` and changes nothing.

Example input:
    push_back 1
    push_back 2
    push_back 3
    push_front 0
    rotate 1
    show
    rotate -2
    show
Output:
    ok
    ok
    ok
    ok
    ok
    1 2 3 0
    ok
    3 0 1 2
