# queue simulator with service times

The first line is `servers N` with N an integer from 1 to 9; otherwise print `bad header` and stop. Each following line is a customer `arrive T ID S`: arrival time T (integer, 0 or more), customer ID (a word) and service time S (integer, 1 or more). Blank lines are ignored.

Customers are served first come first served, in input order, and all servers are free at time 0. A customer starts at the later of their arrival time and the moment the earliest-free server frees up. If several servers could take the customer (they are free at or before the start time), the one with the lowest number (1 to N) is used; otherwise the server that frees up first, lowest number on ties. The customer then occupies that server for S time units.

For each customer print `ID server K start A end B wait W` where W is start minus arrival.

A line is rejected with `line L: ERR` (L is the 1-based line number, header is line 1) and has no effect: `bad line` (wrong shape, bad numbers, or a non-positive S), or `out of order` if T is earlier than the previous accepted arrival.

At the end print `served C total_wait W max_wait M finish F` where F is the latest end time (0 if nobody was served).

Example:
```
servers 2
arrive 0 ann 5
arrive 1 bob 3
arrive 2 cy 4
```
prints
```
ann server 1 start 0 end 5 wait 0
bob server 2 start 1 end 4 wait 0
cy server 2 start 4 end 8 wait 2
served 3 total_wait 2 max_wait 2 finish 8
```
