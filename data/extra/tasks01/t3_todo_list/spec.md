# todo list manager

Read commands from standard input, one per line. Blank lines are ignored. Items get ids 1, 2, 3, ... in the order they are added; ids are never reused, even after removal.

Commands:
- `add TEXT`: TEXT is everything after the first space (not empty). Prints `added ID`.
- `done ID` / `undo ID`: mark the item done / not done. Prints `ID done` / `ID open`.
- `rm ID`: remove the item. Prints `removed ID`.
- `list`: print every item in id order as `[x] ID TEXT` (done) or `[ ] ID TEXT` (open), or `(empty)` if there are no items.
- `open`: like `list` but only the open items, or `(none open)`.
- `clear`: remove all done items. Prints `cleared N` with the number removed.
- `count`: prints `open O done D`.

Errors print `error: MESSAGE` and change nothing: `bad command` (unknown command, missing or extra arguments; for `done`, `undo`, `rm` the argument must be a positive integer, otherwise it is also `bad command`) and `no item ID` when no such item exists.

Example:
```
add buy milk
add write code
done 1
list
clear
count
```
prints
```
added 1
added 2
1 done
[x] 1 buy milk
[ ] 2 write code
cleared 1
open 1 done 0
```
