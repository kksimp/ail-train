# Audit trail diff per user

Standard input holds two snapshots of user records. The line `@before` starts the first snapshot and the line `@after`
starts the second; each section may appear at most once, in any order, and every record line belongs to the most recent
marker. A record line is `USER FIELD VALUE`: USER and FIELD are non-empty words, VALUE is the rest of the line
(non-empty, may contain spaces). If the same USER and FIELD repeat inside a section, the last one wins.
A record line before any marker, a line with fewer than three parts, a repeated marker, or an unknown `@` line is
malformed (skipped and counted). Empty lines are ignored.

A user exists in a snapshot if it has at least one record there. Compare the snapshots; users are processed in ascending
byte order and only changed users are printed:
- user only in `@after`: `USER: added`; user only in `@before`: `USER: removed`.
- user in both: for fields in ascending byte order, `USER: FIELD OLD -> NEW` if the value changed, `USER: +FIELD NEW` if
  the field is new, `USER: -FIELD OLD` if the field disappeared.

Finally print `unchanged: U` (users in both snapshots with no differences) and `malformed: M`.

Example input:
```
@before
ann role user
ann mail a@x.org
bob role admin
@after
ann role admin
ann team ops
cy role user
```
Output:
```
ann: -mail a@x.org
ann: role user -> admin
ann: +team ops
bob: removed
cy: added
unchanged: 0
malformed: 0
```
