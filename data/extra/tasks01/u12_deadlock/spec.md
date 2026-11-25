# Deadlock detection

Detect deadlocks in a wait-for graph.

Input: one edge per line, `P -> Q`, meaning process P waits for process Q. Names are non-empty words of letters, digits, `_` or `-`.
Blank lines and lines starting with `#` are skipped. Any other line that is not exactly `NAME -> NAME` (three words) with valid names is
malformed: it is ignored and counted. Repeated edges count once.

A process is deadlocked if it lies on a cycle of the graph (a process waiting for itself is a cycle). Deadlocked processes that can reach
each other form one deadlock group. A process that is not deadlocked but waits (directly or through others) for a deadlocked process is blocked.

Output, in order:
- one line per deadlock group `deadlock N: P1 P2 ...` with members sorted by byte order; groups are numbered from 1 and ordered by their first (smallest) member.
- if any process is blocked, `blocked: P1 P2 ...` sorted.
- a last line `status=S groups=G deadlocked=D blocked=B ignored=I` where S is `deadlock` if G > 0, else `ok`.

Example input:
    A -> B
    B -> C
    C -> A
    D -> A
    E -> F
Output:
    deadlock 1: A B C
    blocked: D
    status=deadlock groups=1 deadlocked=3 blocked=1 ignored=0

Edge cases: empty input prints `status=ok groups=0 deadlocked=0 blocked=0 ignored=0`.
