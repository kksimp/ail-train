# json_csv

Convert lines of flat JSON-like objects on standard input into CSV.

Input: one object per line; empty lines are ignored (but count for line numbers, the first line being line 1). An object is `{`, then zero or more `"key": value` pairs separated by commas, then `}`. Spaces may appear between any two tokens. A key is a double-quoted string that contains no `"` and no backslash. A value is one of: a double-quoted string (no `"` and no backslash inside; it may contain commas, spaces and braces), an integer (optional `-`, then digits), `true`, `false` or `null`. Nothing else is allowed: nested objects or arrays, fractions, escapes, a trailing comma, text after the closing brace. A line that is not a valid object is skipped. If a key repeats within one object, the last value wins.

Output: the columns are all keys of valid objects, in order of first appearance. If at least one object was valid, print a header line with the column names, then one line per valid object, fields joined with `,`. A string value is printed without its quotes; an integer, `true` or `false` is printed as written; `null` and a missing key give an empty field. A printed field containing a comma (or a column name containing one) is wrapped in double quotes.

After the CSV, print `skipped line K` for each skipped line, in order.

Example input:
```
{"id": 1, "name": "Lee, Ann", "ok": true}
{"id": 2, "tag": null}
{"id": 3,}
```
Example output:
```
id,name,ok,tag
1,"Lee, Ann",true,
2,,,
skipped line 3
```
