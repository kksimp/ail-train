# room_assign

Write `room_assign`, a command-line program. It reads a hotel's room inventory, nightly rates and booking requests from standard input, assigns a room to each booking and prints what happened to every request, followed by a summary.

## Input

One command per line, fields separated by one or more spaces. Lines that are empty or contain only spaces are skipped silently (but they still count when numbering lines: the first line of the input is line 1).

- `inventory TYPE COUNT`: the hotel has `COUNT` rooms of type `TYPE`. A later `inventory` line for the same type replaces its count (rooms already given out stay given out).
- `rate TYPE PRICE`: the price of one night in a `TYPE` room, in whole dollars. A later `rate` line for the same type replaces the price.
- `book GUEST TYPE NIGHTS`: a request by guest `GUEST` for one room of type `TYPE` for `NIGHTS` nights.

`TYPE` and `GUEST` are any text without spaces. `COUNT`, `PRICE` and `NIGHTS` are numbers made only of digits (1 to 6 digits, leading zeros allowed, no sign). `COUNT` and `PRICE` may be 0; `NIGHTS` must be at least 1.

## Rules

Process the lines in order.

- A line is a bad line if its first word is not one of the three commands, or it has the wrong number of fields (3 for `inventory` and `rate`, 4 for `book`), or its last field is not a valid number as described above (for `book`, `NIGHTS` of 0 is also bad). A bad line prints `line K: bad line`, where `K` is the line number, and changes nothing.
- A valid `book` for a type that has no `inventory` yet or no `rate` yet prints `line K: unknown type TYPE`.
- Otherwise, if all rooms of that type are already given out (the number given out is at least the current count), print `GUEST: no TYPE room free`.
- Otherwise the guest gets the next room of that type. Rooms of a type are numbered 1, 2, 3, ... in the order they are given out, and the room is named `TYPE-N`. The gross cost is `NIGHTS * PRICE` (price at that moment). If `NIGHTS` is 7 or more, a discount of one tenth, rounded down (integer division of the gross cost by 10), is subtracted. The result is the cost, added to the revenue. Print `GUEST: TYPE-N, NIGHTS nights, COST` (always the word `nights`, even for 1; `NIGHTS` printed as an ordinary number without leading zeros).

## Output

First, the lines printed while processing, in order. Then one line per type that appeared in an `inventory` line, in the order the types first appeared: `TYPE: GIVEN/COUNT` (rooms given out and the current count). Last, the line `revenue: TOTAL`.

With no input at all, the output is just `revenue: 0`.

## Example

Input:

```
inventory single 2
inventory suite 1
rate single 80
rate suite 200

book ann single 3
book bob suite 7
book cy suite 2
book dee single 1
book eve single 5
book fay villa 2
book gus single 0
move x 3
```

Output:

```
ann: single-1, 3 nights, 240
bob: suite-1, 7 nights, 1260
cy: no suite room free
dee: single-2, 1 nights, 80
eve: no single room free
line 11: unknown type villa
line 12: bad line
line 13: bad line
single: 2/2
suite: 1/1
revenue: 1580
```
