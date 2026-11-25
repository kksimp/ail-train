# upgrade_queue

Write a command-line program that manages a flight's upgrade queue. It reads commands from standard input, one per line, and prints the outcome of every upgrade run.

## Input

Each line is a command made of whitespace-separated words. Blank lines (empty or only spaces/tabs) are ignored but count for line numbering (lines are numbered from 1). Commands, with exact upper-case spelling:

- `SEATS N` sets the number of premium seats currently available to N (replacing the previous value; initially 0).
- `PAX NAME STATUS FARE MILES` registers a passenger. NAME is any word. STATUS is one of `PLAT`, `GOLD`, `SILVER`, `BASIC`. FARE is one of `Y`, `B`, `M`, `K`. MILES is a whole number.
- `REQ NAME` puts a registered passenger into the upgrade queue. Each accepted request gets the next request number, starting at 1 (numbers are shared by all passengers, in input order).
- `RUN` assigns seats (see below).

A number (N or MILES) is valid when it has 1 to 7 characters, all digits `0`-`9` (leading zeros allowed).

## Errors

A command that cannot be applied prints `line K: MESSAGE` (K is the line number) and changes nothing. Checks are made in this order, and the first failing check gives the message:

1. First word is not one of the four commands: `unknown command`.
2. Wrong number of words for the command (SEATS 2 words, PAX 5, REQ 2, RUN 1): `wrong number of arguments`.
3. PAX only: STATUS not valid: `bad status`; then FARE not valid: `bad fare`; then MILES not a valid number: `bad number`; then NAME already registered: `duplicate passenger NAME`.
4. SEATS only: N not a valid number: `bad number`.
5. REQ only: NAME not registered: `unknown passenger NAME`; then NAME already requested (whether or not it has been upgraded): `already requested NAME`.

## Rules for RUN

The waiting passengers are those who have requested an upgrade and have not been upgraded yet. Order them by:
1. status, best first: PLAT, GOLD, SILVER, BASIC;
2. then fare class, best first: Y, B, M, K;
3. then MILES, larger first;
4. then request number, smaller first.

If there are S seats, the first S passengers in this order are upgraded (they leave the queue for good) and the rest stay waiting. Afterwards the available seats are reduced by the number upgraded.

A RUN prints a header `run R: seats S waiting W` (R counts RUNs from 1, S is the seats available before the assignment, W the number of waiting passengers), then one line per waiting passenger in the order above: `U NAME` for an upgraded passenger, or `W P NAME` for a passenger still waiting, where P is the position among the still-waiting passengers, starting at 1.

## Output

All messages and RUN output are printed in input order. At the end print `summary: U upgraded, W waiting`, where U is the number of passengers upgraded over the whole input and W the number still waiting (requested but not upgraded). Empty input prints just `summary: 0 upgraded, 0 waiting`.

## Example

Input:

    SEATS 2
    PAX ann GOLD M 52000
    PAX bob BASIC Y 900
    PAX cy SILVER Y 15000
    PAX dee PLAT K 100
    PAX eve GOLD M 61000
    REQ ann
    REQ bob
    REQ cy
    REQ dee
    REQ eve
    RUN
    SEATS 1
    REQ bob
    RUN
    RUN

Output:

    run 1: seats 2 waiting 5
    U dee
    U eve
    W 1 ann
    W 2 cy
    W 3 bob
    line 14: already requested bob
    run 2: seats 1 waiting 3
    U ann
    W 1 cy
    W 2 bob
    run 3: seats 0 waiting 2
    W 1 cy
    W 2 bob
    summary: 3 upgraded, 2 waiting
