# thousands

Reformats integers with thousands separators, or removes the separators again.

Input: each line is a command `add SEP NUMBER` or `strip SEP NUMBER` where SEP is a single character other than a digit, `-` or space, and NUMBER is a token. Fields are separated by spaces. Empty lines are skipped silently.

- `add`: NUMBER must be an optionally negative decimal integer (`-?[0-9]+`, at most 18 digits; leading zeros are dropped, `-0` and `000` become `0`). Print it with SEP inserted between every group of three digits counted from the right, e.g. `add , 1234567` prints `1,234,567` and `add . -1000` prints `-1.000`.
- `strip`: NUMBER must be a correctly grouped number: an optional `-`, then 1 to 3 digits (the first group, which does not start with `0` unless it is exactly `0` alone with no further groups), then zero or more groups of exactly SEP followed by 3 digits. Print the plain digits (with the sign). Anything else is invalid, for example `1,23,456` or `12,3456`.

Errors, printed instead of a result: `line K: bad command` if the line does not have exactly 3 fields, the command is unknown, or SEP is not exactly one allowed character; `line K: bad number` if NUMBER does not fit the rules of its command. K is the 1-based physical line number.

Finally print `done N errors M`.

Example input:
```
add , 1234567
add . -1000
strip , 1,234,567
strip , 1,23,456
mul , 5
```
Output:
```
1,234,567
-1.000
1234567
line 4: bad number
line 5: bad command
done 3 errors 2
```
