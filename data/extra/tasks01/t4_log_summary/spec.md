# Log summary

Each non-blank input line (after trimming spaces from both ends) should look like `DATE TIME LEVEL MESSAGE`, with
single spaces between the first three fields: DATE is `dddd-dd-dd`, TIME is `dd:dd:dd` (d is an ASCII digit), LEVEL is
exactly one of `ERROR`, `WARN`, `INFO`, `DEBUG`, and MESSAGE is the rest of the line (it may contain spaces and may be
missing). Every other non-blank line is malformed. Blank lines are skipped.

Print, in this order:
    ERROR n
    WARN n
    INFO n
    DEBUG n
    malformed n
    span FIRST .. LAST      (only if at least one valid line)
    first error: MESSAGE    (only if at least one ERROR line)
FIRST and LAST are the `DATE TIME` of the first and the last valid line in input order. MESSAGE is that of the first
ERROR line in input order, or `(no message)` if it has none.

Example input:
    2024-05-01 10:00:00 INFO started
    2024-05-01 10:00:05 ERROR disk full on /dev/sda
    garbage
    2024-05-01 10:01:00 WARN slow response
    2024-05-01 10:02:00 ERROR timeout

Example output:
    ERROR 2
    WARN 1
    INFO 1
    DEBUG 0
    malformed 1
    span 2024-05-01 10:00:00 .. 2024-05-01 10:02:00
    first error: disk full on /dev/sda

Empty input prints the four counts as 0 and `malformed 0` only.
