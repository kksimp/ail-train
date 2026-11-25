# biblio

Convert bibliography entries on standard input into citation strings.

Input: one entry per line, four fields separated by `|`: `AUTHORS | TITLE | YEAR | VENUE`. Each field is trimmed of surrounding spaces. AUTHORS is one or more authors separated by `;`, each written `Last, First Middle...` (a surname, a comma, then one or more given names separated by spaces). Empty lines are ignored (but count for line numbers; the first line is line 1).

An entry is bad if it does not have exactly four fields, if any author lacks a comma or has an empty surname or no given name, if the title or venue is empty, or if YEAR is not exactly four digits.

Citation format: `AUTHORLIST (YEAR). TITLE. VENUE.` Each author is `Last, F. M.`: the surname, a comma, then the first letter of each given name, upper-cased, each followed by a period, separated by spaces. The author list is: one author alone; two authors joined by ` & `; three or more joined by `, ` with `& ` before the last (`A, B, & C`).

Output: the citations of the good entries sorted in ascending byte order, one per line, then one line `error: line K: bad entry` for each bad entry in input order.

Example input:
```
Knuth, Donald Ervin | The Art of Programming | 1968 | Addison-Wesley
Lovelace, Ada; Babbage, Charles | Notes | 1843 | Taylor
broken line
```
Example output:
```
Knuth, D. E. (1968). The Art of Programming. Addison-Wesley.
Lovelace, A. & Babbage, C. (1843). Notes. Taylor.
error: line 3: bad entry
```
