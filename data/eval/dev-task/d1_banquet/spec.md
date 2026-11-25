# banquet

Write `banquet`, a command-line program. It reads the table layout of a banquet hall and the guest groups from standard input, seats the groups and prints the seating plan.

## Input

One command per line, fields separated by one or more spaces. Lines that are empty or contain only spaces are skipped silently (they still count when numbering lines: the first input line is line 1). Group names are any text without spaces. Numbers are made only of digits (1 to 6 digits, leading zeros allowed, no sign).

- The first non-blank line must be `tables COUNT CAPACITY`: `COUNT` tables (1 to 12) each with `CAPACITY` seats (1 to 1000). If the first non-blank line is anything else, or the input has no non-blank line, print exactly `error: no tables line` and stop; nothing else is printed.
- `group NAME SIZE`: a group of `SIZE` guests (at least 1). If a group with that name was already given, the line is bad.
- `apart A B`: the groups named `A` and `B` must not sit at the same table. It applies to them whenever they are given, even if the `apart` line comes before the `group` lines or names a group that never appears. `A` and `B` must differ, otherwise the line is bad.

Any other line after the first (including a second `tables` line, an unknown command, a wrong number of fields, or an invalid or zero number) is bad. A bad line prints `line K: bad line`, where `K` is its line number, and changes nothing. These messages are printed first, in input order, before the seating plan.

## Rules

Take the groups sorted by size, largest first; groups of equal size stay in the order they were given. For each group in that order, look at the tables from table 1 upward and put the group at the first table where both hold: the guests already there plus the group's size do not exceed `CAPACITY`, and no group already at that table has been declared `apart` from this group. If there is no such table, the group is unseated. A group is never split across tables.

## Output

After any bad-line messages:

- One line per table, in order: `Table I (USED/CAPACITY): GROUPS` where `I` counts from 1, `USED` is the number of guests seated there, and `GROUPS` lists the groups in the order they were placed, each as `NAME(SIZE)`, separated by single spaces; an empty table shows `-`.
- `Unseated: ` followed by the unseated groups in the order they were processed (largest first), each `NAME(SIZE)`, separated by `, `; or `none`.
- `Seated: S of T guests`, where `T` is the total size of all groups given and `S` the number seated.

## Example

Input:

```
tables 3 8
group ann 4
group bob 3
apart ann cy
group cy 5
group dan 3
group eve 9
apart bob bob
group fay 2
group ann 1
```

Output:

```
line 8: bad line
line 10: bad line
Table 1 (8/8): cy(5) bob(3)
Table 2 (7/8): ann(4) dan(3)
Table 3 (2/8): fay(2)
Unseated: eve(9)
Seated: 17 of 26 guests
```

(Order of processing: eve 9, cy 5, ann 4, bob 3, dan 3, fay 2. `ann` cannot join `cy`, so `ann` goes to table 2.)
