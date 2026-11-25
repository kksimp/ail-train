# fixed_csv

Convert fixed-width records on standard input to CSV.

Input: the first line lists the field widths, positive integers separated by single spaces (for example `5 8 3`). Every following line is one record: field 1 is the first W1 characters, field 2 the next W2 characters, and so on. A record shorter than the total width gives empty fields for the missing parts (a field cut short keeps the characters it has). Characters beyond the total width are ignored. Empty record lines are skipped.

Each field is trimmed of leading and trailing spaces. Output one CSV line per record: fields joined with `,`. A field that contains a comma or a double quote is wrapped in double quotes, with each inner double quote doubled.

Errors: if the first line is missing, print nothing. If the width line has any token that is not a positive integer, print `error: bad widths` and nothing else.

Example input:
```
5 6 4
Ann  Smith  42
Bo   O"Neil 7
Cy   Lee, J
```
Example output:
```
Ann,Smith,42
Bo,"O""Neil",7
Cy,"Lee, J",
```
