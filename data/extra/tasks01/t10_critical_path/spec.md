Critical path of tasks with durations

The program reads a project plan from standard input, one task per line: `name duration deps`.
`name` is a word without spaces, `duration` a non-negative integer (days), and `deps` either `-` (no dependencies)
or a comma-separated list of task names that must finish first. Tasks may appear in any order. Blank lines are ignored.

A line with a field count other than 3, a bad duration, or a name already defined earlier prints `bad line N`
(1-based line number) and is ignored.

After reading everything:
1. If some dependency names no defined task, print `error: unknown dependency D in T` for the first such pair
   (tasks in input order, dependencies in the order written) and stop.
2. If the dependencies contain a cycle, print `error: cycle` and stop.
3. Otherwise compute earliest times. A task starts when all its dependencies have finished: start = the latest
   dependency finish (0 with none), finish = start + duration. Print one line `name start finish` per task, taking
   tasks in dependency order and, among tasks that are ready, the alphabetically smallest name first (byte order).
   Then print `length L`, where L is the largest finish (0 when there are no tasks).
   Then print `critical: a -> b -> c`: the chain ending at the task with the largest finish (ties: smallest name), where each
   earlier element is the dependency of the next with the largest finish (ties: smallest name). With no tasks print `critical: none`.

Example input:
```
test 2 build
design 3 -
build 4 design
docs 2 design
ship 1 test,docs
```
Output:
```
design 0 3
build 3 7
docs 3 5
test 7 9
ship 9 10
length 10
critical: design -> build -> test -> ship
```
