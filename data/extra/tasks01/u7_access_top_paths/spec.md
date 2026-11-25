# Access log summary

Read a web access log from standard input. Each non-empty line has exactly five fields separated by single spaces:
`IP METHOD PATH STATUS BYTES`. All five must be non-empty, STATUS must be digits only with a value from 100 to 599, and
BYTES must be digits only. Any other non-empty line is malformed. Empty lines are ignored.

Print, in this order:
1. `top paths:` followed by up to three lines `COUNT PATH`, the most requested paths, count descending, ties by path ascending (byte order).
2. `status:` followed by five lines `1xx N`, `2xx N`, `3xx N`, `4xx N`, `5xx N` (N may be 0).
3. `malformed: K`

Example input:
```
1.1.1.1 GET /a 200 10
1.1.1.2 GET /b 404 5
1.1.1.3 GET /a 200 7
bad line
```
Output:
```
top paths:
2 /a
1 /b
status:
1xx 0
2xx 2
3xx 0
4xx 1
5xx 0
malformed: 1
```
Empty input prints `top paths:`, the five status lines with 0, and `malformed: 0`.
