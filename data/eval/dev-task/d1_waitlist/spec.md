# waitlist

Write `waitlist`, a command-line program. It simulates a restaurant seating parties at tables with a first-come waitlist. It reads a list of events from standard input and prints what happens for each event, then a final summary.

## Input

One event per line, fields separated by one or more spaces. Lines that are empty or contain only spaces are skipped silently (they still count when numbering lines: the first input line is line 1). Names (`ID`, `PARTY`) are any text without spaces. `SEATS` and `SIZE` are numbers made only of digits (1 to 6 digits, leading zeros allowed, no sign) and must be at least 1.

- `table ID SEATS`: a new table with `SEATS` seats becomes available (empty).
- `arrive PARTY SIZE`: a party of `SIZE` people arrives.
- `leave PARTY`: the named party leaves, whether it is seated or still waiting.

## Rules

State: the tables in the order they were added (each empty or occupied by one party), and the waitlist, a queue of waiting parties in arrival order. A party takes a whole table; a party fits a table if `SIZE <= SEATS`.

Process events in order. Each prints exactly one line, except where noted.

`table ID SEATS`
- If a table with this `ID` already exists, the line is bad (see below).
- Otherwise add it and print `table ID added`. Then try to seat a waiting party at this new table (see "Seating from the waitlist").

`arrive PARTY SIZE`
- If a party with this name is already seated or waiting, print `PARTY already here` and do nothing else.
- Else if `SIZE` is larger than the seats of every existing table (or there are no tables), print `PARTY too large` and do nothing else (the party is not put on the waitlist).
- Else, among the empty tables that fit, choose the one with the fewest seats; if several have the same number of seats, the one added first. Seat the party there and print `PARTY seated at ID`.
- Else (it fits some table but none that fit is empty) add it to the end of the waitlist and print `PARTY waits (position N)`, where `N` is the number of parties on the waitlist including this one.

`leave PARTY`
- If the party is seated: its table becomes empty, print `PARTY left`, then try to seat a waiting party at that table.
- Else if the party is waiting: remove it from the waitlist and print `PARTY removed from waitlist`.
- Else print `PARTY not found`.

Seating from the waitlist: when a table has just been added or just become empty, look through the waitlist from the oldest party to the newest and seat the first party that fits that table (a larger party that does not fit is skipped and stays in line). Print `PARTY seated at ID` for it, on its own line after the line of the triggering event, and remove it from the waitlist. At most one party is seated this way. If none fits, nothing is printed.

Bad line: a line whose first word is not `table`, `arrive` or `leave`, or that has the wrong number of fields (3 for `table` and `arrive`, 2 for `leave`), or whose number is not valid (not digits, more than 6 digits, or 0), or a `table` line with an `ID` that already exists. It prints `line K: bad line`, where `K` is the line number, and changes nothing.

## Output

The lines described above, in order, then two summary lines:

- `waiting: ` followed by the waitlist from oldest to newest, each as `PARTY(SIZE)`, separated by `, `, or `none` if the waitlist is empty.
- `free tables: ` followed by the IDs of the empty tables in the order the tables were added, separated by `, `, or `none`.

## Example

Input:

```
table t1 2
table t2 4
table t3 4
arrive ann 3
arrive bob 2
arrive cy 4
arrive dee 4
arrive eve 2
arrive fay 9
arrive eve 1

arrive gus 0
leave bob
leave ann
leave zed
leave dee
```

Output:

```
table t1 added
table t2 added
table t3 added
ann seated at t2
bob seated at t1
cy seated at t3
dee waits (position 1)
eve waits (position 2)
fay too large
eve already here
line 12: bad line
bob left
eve seated at t1
ann left
dee seated at t2
zed not found
dee left
waiting: none
free tables: t2
```
