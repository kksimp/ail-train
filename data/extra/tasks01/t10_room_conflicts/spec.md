Room booking conflicts

The program reads booking requests from standard input, one per line, and decides them in order.
A request line has four fields separated by single spaces: `room start end name`.
`start` and `end` are non-negative integers (slot numbers), and a valid request has start < end.
A booking occupies the half-open range [start, end), so a booking ending at 5 and one starting at 5 do not conflict.

For each non-blank line, in order:
- Malformed (not exactly 4 fields, a non-integer slot, or start >= end): print `BAD line N` (N is the 1-based line number).
- Otherwise, if it overlaps an already accepted booking in the same room, print
  `REJECT name room start-end conflicts with other`, where `other` is the name of the earliest accepted conflicting booking.
- Otherwise accept it and print `OK name room start-end`.
Blank lines are skipped but still count toward line numbers.

After all lines print one summary line: `accepted A rejected R bad B`.

Example input:
```
A 1 4 ann
A 4 6 bob
A 3 5 cy
B 3 5 dee
A 7 7 eve
```
Output:
```
OK ann A 1-4
OK bob A 4-6
REJECT cy A 3-5 conflicts with ann
OK dee B 3-5
BAD line 5
accepted 3 rejected 1 bad 1
```
Empty input prints `accepted 0 rejected 0 bad 0`.
