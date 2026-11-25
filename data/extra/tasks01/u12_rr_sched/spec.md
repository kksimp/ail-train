# Round-robin scheduler

Read a CPU scheduling job from standard input and simulate round-robin scheduling on one CPU.

Input: the first non-blank line is `quantum Q` with Q an integer >= 1. If it is missing or invalid, print `bad quantum` and stop.
Every later non-blank line is `NAME ARRIVAL BURST` (three words, ARRIVAL >= 0, BURST >= 1, both integers). A line that does not
fit this is ignored, but counted.

Rules: the ready queue is FIFO. A process runs for min(Q, remaining) time units. Processes that arrive at or before the moment a
slice ends are queued first, then the preempted process (if unfinished) goes to the back. If the queue is empty the CPU idles until
the next arrival. Processes with equal arrival times enter in input order.

Output: one line per slice `START-END NAME` in time order, then one line per process in input order
`NAME finish=F turnaround=T wait=W` (turnaround = finish - arrival, wait = turnaround - burst), then `ignored N` with the count
of ignored lines.

Example input:
    quantum 2
    A 0 5
    B 1 3
Output:
    0-2 A
    2-4 B
    4-6 A
    6-7 B
    7-8 A
    A finish=8 turnaround=8 wait=3
    B finish=7 turnaround=6 wait=3
    ignored 0

Edge cases: empty input prints `bad quantum`. With no valid processes only `ignored N` is printed.
