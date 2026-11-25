# Event deduplication by key and window

Standard input starts with a header `window W` (W digits only, at least 1). Then event lines `TS KEY PAYLOAD`: TS is
digits only, KEY is a non-empty word, PAYLOAD is the rest of the line (it may contain spaces and may be missing).
Empty lines are ignored. A line is malformed (skipped and counted) if TS is not digits, KEY is missing, or TS is smaller
than the TS of the previous valid event.

An event is a duplicate, and dropped, if an event with the same KEY was kept at a time T with TS - T < W. Otherwise it
is kept (and becomes the reference for later events of that key). A dropped event does not move the reference.

Print every kept event exactly as it appeared in the input, in order. Then print `kept: K dropped: D malformed: M`,
then one line `KEY N` for each key that had at least one dropped event (N = dropped count), keys in ascending byte order.
If the header is missing or invalid print only `error: bad header`.

Example input:
```
window 10
0 disk full
3 disk full again
5 cpu hot
10 disk back
12 cpu hot
```
Output:
```
0 disk full
5 cpu hot
10 disk back
12 cpu hot
kept: 4 dropped: 1 malformed: 0
disk 1
```
