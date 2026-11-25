# Record filter queries

Read a small table of records followed by filter queries; for each query print the matching records.

## Input
1. The first line is the header: field names separated by whitespace. The first field identifies a record. If the input is completely empty, print nothing.
2. Then record lines follow, up to the first line that is empty or only whitespace (or the end of input). A record line is its values separated by whitespace (runs of spaces/tabs); a line whose number of values differs from the number of header fields is silently ignored. Records keep their input order.
3. After that first blank line, every remaining line that is not blank is a query (blank lines there are skipped). Queries are numbered from 1.

## Query syntax
A query is words separated by whitespace: `TERM (CONNECTIVE TERM)*` where a TERM is three words `FIELD OP VALUE` and a CONNECTIVE is `and` or `or`. OP is one of `=`, `!=`, `<`, `<=`, `>`, `>=`, `~`. `and` binds tighter than `or` (so `a or b and c` means `a or (b and c)`); there are no parentheses. A VALUE is a single word (it can be anything, including a word like `and`).

If the word count is not of the form 3, 7, 11, ... or any OP position holds a non-operator or any connective position holds something other than `and`/`or`, the query is bad: print `N: error: bad query`. Otherwise, if any FIELD is not a header field, print `N: error: unknown field NAME` for the first such FIELD in the query. (The bad-query check comes first.)

## Comparing
For a term, take the record's value `a` for FIELD and the query's `b`:
- `~` is true when `b` occurs as a substring of `a` (always a text comparison).
- For the other operators, if both `a` and `b` are integers (optional `-`, then one or more digits `0-9`; leading zeros allowed) compare them as integers; otherwise compare as text by character codes (so `B` < `a`; a shorter string that is a prefix of another is smaller). The result of `=`, `!=`, `<`, `<=`, `>`, `>=` is the usual one.

## Output
For each query print `N: COUNT` where COUNT is the number of matching records; if COUNT is greater than 0, follow it with a space and the first-field values of the matching records, in record order, joined with `,`.

## Example
Input:
```
name age city score
alice 34 oslo 90
bob 25 bergen 72
carol 41 oslo 85
dave 19 tromso 60
erin 34 bergen 100

age > 30
city = oslo and score >= 90
city = oslo or city = bergen and age < 30
name ~ a
score < 50
age = 34 and city != oslo
```
Output:
```
1: 3 alice,carol,erin
2: 1 alice
3: 3 alice,bob,carol
4: 3 alice,carol,dave
5: 0
6: 1 erin
```
