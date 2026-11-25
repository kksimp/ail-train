# sla_breach

Write a program that reads a helpdesk ticket list from standard input and reports which tickets breached their response SLA.

## Input

Line 1 is the current time `NOW`, an integer number of minutes. Every following line is a ticket: `ID,PRIORITY,OPENED,RESOLVED` with exactly four comma-separated fields. `OPENED` is an integer minute. `RESOLVED` is either an integer minute or the single character `-` meaning the ticket is still open. Blank lines are ignored. All lines are well formed. If the input is empty, there are no tickets and `NOW` is irrelevant.

## Rules

- The limit in minutes depends on `PRIORITY`: `P1` is 60, `P2` is 240, anything else is 1440.
- A ticket's elapsed time is `RESOLVED - OPENED`, or `NOW - OPENED` if it is still open.
- A ticket breached if elapsed is strictly greater than its limit. Its overrun is `elapsed - limit`.

## Output

For each breached ticket, in input order, print `ID over by M` where `M` is the overrun. Then print one final line `breaches: K of N` where `K` is the number of breached tickets and `N` the number of tickets.

## Example

Input:
```
500
T1,P1,0,45
T2,P1,100,200
T3,P2,10,-
T4,P3,0,1440
T5,P9,100,-
```

Output:
```
T2 over by 40
T3 over by 250
breaches: 2 of 5
```
