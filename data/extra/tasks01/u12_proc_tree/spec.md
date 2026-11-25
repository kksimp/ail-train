# Process tree

Build a process tree from a process list and print it.

Input: one process per line, `PID PPID NAME...` where PID and PPID are integers >= 0 and NAME is the rest of the line (one or more words,
joined with single spaces). Blank lines are ignored. A line with fewer than 3 words, or a non-integer or negative PID/PPID, is malformed.
A line repeating an earlier PID is a duplicate and is ignored. Malformed and duplicate lines are each counted as ignored.

A process is a root if its PPID is 0 or names no listed process (a process whose PPID equals its own PID is not a root).
Print each root and its descendants depth first; roots and the children of every process are ordered by PID ascending.
Each line is two spaces of indent per depth, then `PID NAME`.

After the tree print `processes=N depth=D ignored=I`: N is the number of distinct processes, D the number of levels in the deepest
tree (0 if none), I the ignored count. Processes not reachable from any root (they form a parent cycle) are not printed in the
tree; if there are any, print `orphans: P1 P2 ...` with their PIDs ascending, between the tree and the summary line.

Example input:
    1 0 init
    20 1 sshd
    7 1 cron
    21 20 sshd: user
Output:
    1 init
      7 cron
      20 sshd
        21 sshd: user
    processes=4 depth=3 ignored=0
