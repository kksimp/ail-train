# Error burst detection

Standard input starts with a header line `window W threshold K` (W and K digits only, both at least 1). Every other
non-empty line is a log line `TS LEVEL MESSAGE...`: TS is digits only, LEVEL is a word, MESSAGE is the rest (may be
empty or contain spaces). A log line is malformed if it has no LEVEL, if TS is not digits, or if TS is smaller than
the TS of the previous valid log line. Malformed lines are skipped and counted. Empty lines are ignored.

Only lines whose LEVEL is exactly `ERROR` count as errors. Scan the errors in order. Take the first error not yet
used by a burst, with timestamp t, and count the errors (from this one onward) whose timestamp is at most t + W - 1.
If that count is at least K, report a burst and mark all those errors as used; otherwise move on to the next error.

Print one line per burst `burst START END COUNT` (START = t, END = timestamp of the last error in the burst, COUNT =
number of errors in it), then `bursts: B` and `malformed: M`.
If the header is missing or invalid print only `error: bad header`.

Example input:
```
window 10 threshold 3
1 ERROR a
2 INFO ok
4 ERROR b
9 ERROR c
12 ERROR d
30 ERROR e
```
Output:
```
burst 1 9 3
bursts: 1
malformed: 0
```
