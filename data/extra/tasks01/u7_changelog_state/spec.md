# Change log to current state

Standard input is a change log applied in order to an initially empty key/value store. Each non-empty line is one command
(empty lines are ignored but still count for line numbers, which start at 1):
- `set KEY VALUE`: store VALUE (the rest of the line, non-empty, may contain spaces) under KEY.
- `del KEY`: remove KEY; rejected if KEY does not exist.
- `rename OLD NEW`: move the value of OLD to NEW; rejected if OLD does not exist, or NEW exists, or OLD equals NEW.
- `incr KEY N`: add the integer N (optional leading `-`, then digits) to the value of KEY; a missing KEY counts as 0;
  rejected if N is not an integer or the existing value is not an integer.
KEY, OLD and NEW are non-empty words without spaces. Any other line (unknown command, wrong number of arguments) is
rejected. A rejected command changes nothing.

Print `state:` followed by one line `KEY=VALUE` per key in ascending byte order, then `rejected: R` followed by one line
`line L` for each rejected command in input order. Integer results are printed in plain decimal.

Example input:
```
set a 1
set b hello world
incr a 41
rename b c
del zzz
```
Output:
```
state:
a=42
c=hello world
rejected: 1
line 5
```
