# kv_group

Read `key=value` lines from standard input and print them grouped and sorted.

Input: one entry per line. A line is split at its first `=`; the key (before) and the value (after) are each trimmed of surrounding spaces. Empty lines and lines starting with `#` are ignored. Any other line without `=`, or whose trimmed key is empty, is malformed and counted.

A key is split at its first `.` into a group and a sub-key (`db.host` is group `db`, sub-key `host`). A key without `.` has group `default` and the whole key as sub-key. If the same full key appears again, the later value replaces the earlier one.

Output: groups in ascending byte order. For each group print `[GROUP]`, then one line `SUBKEY = VALUE` per entry in ascending byte order of sub-key. Groups are separated by one empty line. If any line was malformed, finish with an empty line and `skipped: N`. If there are no entries and nothing was malformed, print nothing.

Example input:
```
db.port = 5432
name=demo
db.host=localhost
oops
db.port=5433
```
Example output:
```
[db]
host = localhost
port = 5433

[default]
name = demo

skipped: 1
```
