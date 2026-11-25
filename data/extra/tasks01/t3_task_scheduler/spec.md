# priority task scheduler

Read commands from standard input, one per line (words separated by spaces; blank lines ignored). The scheduler holds pending tasks, each with a unique name and a priority from 1 to 9 (9 is the most urgent). Among equal priorities the task added first runs first.

Commands:
- `add NAME PRIO`: add a task. Prints `added NAME`.
- `next`: remove and run the most urgent task. Prints `run NAME PRIO`, or `idle` if nothing is pending.
- `bump NAME N`: raise the priority of a pending task by N (an integer of at least 1), capped at 9. The task keeps its place in the add order. Prints `NAME now P`.
- `cancel NAME`: remove a pending task. Prints `cancelled NAME`.
- `list`: print the pending tasks in the order they would run, one `NAME:PRIO` per line, or `empty` if none.

Errors print `error: MESSAGE` and change nothing: `bad command` (unknown command or wrong word count), `bad priority` (PRIO not an integer from 1 to 9, or N not an integer of at least 1), `duplicate NAME` (a pending task has that name; a name can be reused after the task ran or was cancelled), `no such task NAME`.

The checks for `add` run in the order bad command, bad priority, duplicate; for `bump` bad command, bad priority, no such task.

Example:
```
add a 3
add b 5
add c 5
bump a 4
list
next
next
```
prints
```
added a
added b
added c
a now 7
a:7
b:5
c:5
run a 7
run b 5
```
