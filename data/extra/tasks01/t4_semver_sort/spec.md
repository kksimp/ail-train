# Semantic version sort

Each non-blank input line (trim spaces) is a version `MAJOR.MINOR.PATCH` or `MAJOR.MINOR.PATCH-PRE`. MAJOR, MINOR and
PATCH are runs of 1 to 9 ASCII digits (leading zeros allowed, compared as numbers). PRE is one or more identifiers
separated by `.`; each identifier is a non-empty run of ASCII letters and digits. Anything else on a line makes it invalid.

Precedence (ascending): compare MAJOR, then MINOR, then PATCH as numbers. If those are equal, a version with a PRE sorts
before the same version without one. Two PREs compare identifier by identifier: an all-digit identifier is compared as a
number and sorts before any identifier containing a letter; two identifiers with letters compare as plain byte strings;
if all shared identifiers are equal, the PRE with fewer identifiers sorts first. Versions that compare equal keep their
input order.

Print the valid versions exactly as written (trimmed), one per line, in ascending order. Then print one line
`invalid: TEXT` for each invalid line, in input order. Blank lines are skipped.

Example input:
    1.10.0
    1.2.0
    1.2.0-rc.1
    1.2.0-alpha
    x.1.2

Example output:
    1.2.0-alpha
    1.2.0-rc.1
    1.2.0
    1.10.0
    invalid: x.1.2

Empty input prints nothing.
