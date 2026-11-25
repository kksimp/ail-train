# Uptime from heartbeats

Standard input: a header line `interval I` (I digits only, at least 1), then lines of two kinds:
`beat TS` (a heartbeat at second TS) and `end TS` (the end of observation). TS is digits only. Empty lines are ignored.
A line is malformed (skipped and counted) if it is neither kind, or if:
- a `beat` TS is not strictly greater than the previous valid beat's TS, or a beat appears after a valid `end`;
- an `end` appears before any valid beat, a second `end` appears, or its TS is smaller than the last beat's TS.

A service is expected to beat every I seconds. For consecutive beats a < b with b - a > I there is a downtime period
from a + I to b. If an `end` E was given and E - last_beat > I there is also a period from last_beat + I to E.

Print `beats: N`. If N is 0 nothing else except `malformed: M`. Otherwise print one line `down S E` per period in time
order, then `downtime: D` (total length of all periods), `observed: O` (E, or the last beat if there is no `end`, minus the
first beat), `uptime: P%` where P = (O - D) * 100 / O rounded down (100 if O is 0), then `malformed: M`.
If the header is missing or invalid print only `error: bad header`.

Example input:
```
interval 10
beat 0
beat 10
beat 45
end 60
```
Output:
```
beats: 3
down 20 45
down 55 60
downtime: 30
observed: 60
uptime: 50%
malformed: 0
```
