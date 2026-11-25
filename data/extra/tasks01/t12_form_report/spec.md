# Form field validation report

Reads a submitted form as `key=value` lines and prints a validation report.

Input: one entry per line. Empty lines are skipped (but still counted when numbering lines). Split a line at its first `=`; trim the key and the value. Lines are handled in order:
- a line without `=`: print `line N: malformed`
- a key other than `name`, `age`, `email`, `zip`: print `line N: unknown field KEY`
- otherwise the value is stored for that key (a later line for the same key replaces the earlier value).
`N` is the 1-based line number.

After the input lines print one line per field in the order name, age, email, zip as `FIELD: STATUS`, where STATUS is the first that applies:
- `missing`: the field was never given, or its value is empty
- name: `too long` if more than 20 characters; else `ok`
- age: `not a number` if not made only of digits `0`-`9`; `out of range` if above 120; else `ok`
- email: `invalid` unless it has exactly one `@`, a non-empty part before it, and after it a domain of two or more non-empty parts separated by `.`, with no space anywhere; else `ok`
- zip: `invalid` unless exactly 5 digits; else `ok`

Last line: `RESULT valid` if all four fields are `ok`, otherwise `RESULT invalid (K)` where K is the number of fields that are not `ok`.

Example input:
```
name = Ann
age=abc
mood=happy
email=a@b.co
```
Example output:
```
line 3: unknown field mood
name: ok
age: not a number
email: ok
zip: missing
RESULT invalid (2)
```

Empty input prints the four `missing` lines and `RESULT invalid (4)`.
