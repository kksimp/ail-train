# Duration sum

Each non-blank input line (after trimming spaces and tabs) should be one duration written `h:mm:ss`: hours are 1 to 5
ASCII digits, minutes exactly two digits 00-59, seconds exactly two digits 00-59. Blank lines are skipped and not counted.

Print three lines:
    total H:MM:SS
    valid N
    invalid M
`total` is the sum of all valid durations written with hours unpadded (and no limit on their size) and minutes and
seconds padded to two digits. N counts valid lines, M counts non-blank lines that are not valid durations
(those are ignored in the total).

Example input:
    1:30:00
    0:45:30
    12:5:00
    0:00:45

Example output:
    total 2:16:15
    valid 3
    invalid 1

Empty input prints `total 0:00:00`, `valid 0`, `invalid 0`.
