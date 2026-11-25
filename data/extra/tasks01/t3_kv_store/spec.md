# key-value store

Read commands from standard input, one per line, and maintain a string-to-string store that starts empty. A line is split on single spaces. Keys contain no spaces. An empty line is ignored.

Commands:
- `set K V`: V is everything after the single space that follows K (it may contain spaces, and is not empty). Prints `ok`.
- `get K`: prints the value, or `(nil)` if K is absent.
- `del K`: prints `deleted` if K was present (and removes it), else `missing`.
- `count`: prints the number of keys.
- `keys`: prints the keys in ascending byte order separated by single spaces, or `(empty)` if there are none.
- `incr K`: if K is absent, sets it to `1`; if its value is an integer (optional leading `-`), adds 1; either way prints the new value. If the value is not an integer, prints `error: not an integer` and changes nothing.

Any other line (unknown command, wrong number of arguments, `set` with a missing key or value) prints `error: bad command`.

Example:
```
set name Ada Lovelace
get name
incr hits
incr hits
del name
count
get name
```
prints
```
ok
Ada Lovelace
1
2
deleted
1
(nil)
```
