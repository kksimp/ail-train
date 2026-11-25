# Multi-key record sort

The first input line is a sort specification: comma-separated keys, each `FIELD:DIR`, where FIELD is one of
`name`, `dept`, `salary` and DIR is `asc` or `desc`, e.g. `dept:asc,salary:desc`. If the line is missing or any key is
invalid (unknown field, unknown direction, no colon), print `bad spec` and stop.

Every following line is a record `name,dept,salary` (no spaces trimmed except a trailing `\r`). A record is
malformed if it does not have exactly 3 comma-separated fields, if name or dept is empty, or if salary is not an
integer (optional `-` then digits). Malformed lines are skipped and reported as `skip N` (N = 1-based input line
number, the spec line being line 1), printed before the sorted records, in input order. Blank lines are skipped
silently.

Then print the valid records as `name,dept,salary`, sorted by the keys in order of the spec. `name` and `dept`
compare as strings (byte order), `salary` as an integer. The sort is stable: records equal on every key keep their
input order.

Example input:
```
dept:asc,salary:desc
bob,ops,50
ann,dev,70
cy,dev,90
oops
dan,ops,50
```
Output:
```
skip 5
cy,dev,90
ann,dev,70
bob,ops,50
dan,ops,50
```
