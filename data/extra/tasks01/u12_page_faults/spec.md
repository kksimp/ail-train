# Page replacement faults

Compare FIFO and LRU page replacement for a reference string.

Input: a line `frames N` (N >= 1), then any number of lines holding page numbers as whitespace-separated integers; together
they form the reference string in order. A token that is not an integer is skipped and counted. If the first non-blank line is not a valid
`frames N` line, print `bad frames` and stop.

Simulation: memory holds at most N pages. A reference to a resident page is a hit; otherwise it is a fault, and when memory is
full one page is evicted first. FIFO evicts the page that has been resident longest (a hit does not change its position). LRU evicts
the page used least recently (a hit makes the page most recent). A new page is added as newest.

Output, FIFO block then LRU block:
    NAME faults=F hits=H
    NAME trace=SYMBOLS      (one char per reference: F for fault, H for hit; empty if no references)
    NAME frames=[P1 P2 ...] (final resident pages, oldest/least recent first)
and last `skipped K`.

Example input:
    frames 3
    1 2 3 4 1 2
Output:
    FIFO faults=6 hits=0
    FIFO trace=FFFFFF
    FIFO frames=[4 1 2]
    LRU faults=6 hits=0
    LRU trace=FFFFFF
    LRU frames=[4 1 2]
    skipped 0

Edge: with no references the traces are empty and frames=[].
