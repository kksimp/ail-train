# Login failure lockouts

Standard input starts with a header `policy F W L` (three numbers, digits only, each at least 1): F failures within W
seconds lock the account for L seconds. Then come events `TS USER RESULT` with TS digits only, USER a non-empty word and
RESULT either `ok` or `fail`. Empty lines are ignored. An event line is malformed (skipped and counted) if it does not
have exactly these three fields, or if its TS is smaller than the TS of the previous valid event.

Process valid events in order, per user:
- If the user is locked (the event's TS is smaller than the lock end), print `TS USER denied`; nothing else changes.
- Otherwise `ok` prints `TS USER ok` and forgets the user's earlier failures.
- Otherwise `fail` records a failure at TS. Failures that are W seconds or older (TS - failure_time >= W) are dropped
  first. If the user now has F recorded failures, the user is locked until TS + L, the failures are forgotten and
  `TS USER locked` is printed; otherwise `TS USER fail` is printed.

Finally print `lockouts: N` (how many `locked` lines) and `malformed: M`.
If the header is missing or invalid print only `error: bad header`.

Example input:
```
policy 2 10 30
1 amy fail
5 amy fail
6 amy ok
40 amy fail
```
Output:
```
1 amy fail
5 amy locked
6 amy denied
40 amy fail
lockouts: 1
malformed: 0
```
