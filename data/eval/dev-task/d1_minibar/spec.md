# minibar

Write `minibar`, a command-line program. It reads minibar usage records for a hotel from standard input and prints a bill per room.

## Input

Each line is a record `ROOM ITEM QTY`: three fields separated by one or more spaces. `ROOM` is any text without spaces (for example `101` or `12B`). `ITEM` is the item taken. `QTY` is a whole number of items.

Lines that are empty or contain only spaces are ignored completely (they are not counted anywhere).

## Prices (whole dollars per item)

| item | price |
|---|---|
| water | 3 |
| soda | 4 |
| juice | 5 |
| beer | 7 |
| wine | 22 |
| chocolate | 6 |

## Rules

- A record is valid when it has exactly three fields, `ITEM` is one of the items in the table (exact, lower case), and `QTY` is an integer written with digits and an optional leading `-` that is greater than 0.
- Every other non-blank line is invalid and is only counted.
- A valid record adds `price * QTY` to its room's total.

## Output

If there is no valid record, print `no charges`. Otherwise print one line per room that has charges, `ROOM: TOTAL`, with rooms in ascending order of their text compared byte by byte (so `101` comes before `12B`, and `9` comes after `101`), then the line `total: SUM` where `SUM` is the sum over all rooms.

After that, if at least one invalid line was counted, print `skipped: N` where `N` is the number of invalid lines.

## Example

Input:

```
101 water 2
205 beer 3
101 wine 1
205 gold 1
12B soda x
12B chocolate 4
```

Output:

```
101: 28
12B: 24
205: 21
total: 73
skipped: 2
```
