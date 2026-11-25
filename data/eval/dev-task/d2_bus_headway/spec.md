# bus_headway

Write a command-line program that reads bus arrival times from standard input and prints a headway report for each route. The headway is the time gap between consecutive arrivals.

## Input

Zero or more lines. A blank line (empty or only spaces/tabs) is ignored but still counts for numbering. Any other line is an arrival record when it consists of exactly two whitespace-separated words `ROUTE HH:MM`: ROUTE is any word, and the time has exactly two digit characters (`0`-`9`) for the hour, a colon, and exactly two digit characters for the minutes, with hour 00-23 and minutes 00-59. Lines are numbered from 1. Arrivals are not necessarily in time order, and the same time may appear more than once.

## Rules

- A non-blank line that is not a valid arrival record is reported as `line K: bad` (K is its line number) on standard output immediately while reading, so all such messages come before the route reports.
- Group the valid arrivals by route. Routes are reported in the order in which each route first appears among the valid records.
- For each route sort its arrival times (in minutes since midnight) in ascending order. The gaps are the differences between consecutive sorted times (a duplicate time gives a gap of 0).
- With N arrivals there are N-1 gaps. If N is less than 2 the route has no headway.
- `min` is the smallest gap, `max` the largest gap. `avg` is the sum of gaps divided by the number of gaps, rounded half up with integer arithmetic: `(sum * 2 + count) / (2 * count)` with integer division rounding down.
- `longest` is the interval of the largest gap, written `START-END` with both times as `HH:MM`. If several gaps tie for the largest, use the earliest one.

## Output

First the `line K: bad` messages (if any), then one line per route:

    ROUTE n=N min=A max=B avg=C longest=HH:MM-HH:MM

or, when the route has fewer than two arrivals:

    ROUTE n=N no headway

Nothing else is printed (empty input prints nothing).

## Example

Input:

    12 08:00
    12 08:10
    7 07:30
    12 08:25
    oops
    7 07:30
    12 8:40
    12 08:55
    9 23:59
    7 07:45

    12 09:15

Output:

    line 5: bad
    line 7: bad
    12 n=5 min=10 max=30 avg=19 longest=08:25-08:55
    7 n=3 min=0 max=15 avg=8 longest=07:30-07:45
    9 n=1 no headway
