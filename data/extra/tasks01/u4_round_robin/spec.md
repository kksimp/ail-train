# Round-robin scheduler

The first line holds the time quantum Q (an integer 1 to 100). Every following line is a command; blank lines are ignored. Words are separated by spaces. The ready queue starts empty.

Commands and output:
- `add NAME BURST`: append a process to the back of the queue. NAME is a single word; BURST is an integer from 1 to 1000 (total time it needs). Prints `ok`; prints `dup` and changes nothing if a process with that NAME is still in the queue.
- `run N`: N is a non-negative integer. Perform N time slices. In each slice the front process runs for min(Q, remaining) time units; print `NAME ran T` for it (T = units used). If it has no time left print `NAME done`; otherwise it goes to the back of the queue. If the queue is empty before a slice, print `idle` once and stop (the remaining slices are skipped).
- `status`: print the queue front to back as `NAME:REMAINING` separated by single spaces, or `empty`.
- `clock`: print the total number of time units run so far (across all `run` commands).

Any other line (unknown command, wrong number of words, BURST out of range or not an integer, N invalid) prints `error` and changes nothing.
If the first line is not an integer from 1 to 100, print `bad quantum` and nothing else.

Example input:
    3
    add a 5
    add b 2
    run 3
    status
    clock
Output:
    ok
    ok
    a ran 3
    b ran 2
    b done
    a ran 2
    a done
    empty
    7
