# parking lot

The first line is `capacity N` with N an integer from 1 to 99; otherwise print `bad header` and stop. Spots are numbered 1 to N. Each following line is a command (words separated by spaces; blank lines ignored). Times are whole minutes (integers, 0 or more).

Commands:
- `park T PLATE`: the car takes the lowest-numbered free spot. Prints `PLATE spot K`. If the lot is full prints `PLATE rejected: full`.
- `leave T PLATE`: the car leaves, freeing its spot. The fee is 2 per started hour of parking (duration = T minus the arrival time; 1 to 60 minutes is one hour, 61 to 120 is two, ...), with a minimum of one hour (a duration of 0 also costs 2). Prints `PLATE left spot K fee F`.
- `status`: prints `free F of N`, then one line `K PLATE` per occupied spot in spot order.

Errors print `error: MESSAGE` and change nothing: `bad command` (unknown command, wrong word count, or T not a non-negative integer), `already parked PLATE`, `not parked PLATE`, `time went backwards` (for `leave`, if T is earlier than the arrival time).

Check order for `park`: bad command, already parked, then full. For `leave`: bad command, not parked, time went backwards.

At the end of input print `revenue R` (the sum of all fees) and `occupied O`.

Example:
```
capacity 2
park 0 AAA
park 10 BBB
park 20 CCC
leave 130 AAA
status
```
prints
```
AAA spot 1
BBB spot 2
CCC rejected: full
AAA left spot 1 fee 6
free 1 of 2
2 BBB
revenue 6
occupied 1
```
