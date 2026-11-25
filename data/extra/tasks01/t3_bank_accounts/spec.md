# bank accounts

Read commands from standard input, one per line (words separated by spaces; blank lines ignored). Accounts start nonexistent; balances are integers.

Commands:
- `open NAME`: create an account with balance 0, prints `opened NAME`.
- `deposit NAME AMT`: add AMT, prints `NAME: BALANCE`.
- `withdraw NAME AMT`: subtract AMT, prints `NAME: BALANCE`.
- `transfer FROM TO AMT`: move AMT, prints `FROM->TO AMT`.
- `balance NAME`: prints `NAME: BALANCE`.
- `report`: prints one line `NAME BALANCE` per account in ascending name order (byte order), then `total T` (sum of all balances).

AMT must be an integer of at least 1, otherwise the error is `bad amount`.

Errors print `error: MESSAGE` on stdout and change nothing. Checks run in this order, the first failure wins:
1. wrong word count for the command, or an unknown command: `bad command`
2. (open) `exists NAME` if it is already open
3. `bad amount`
4. `no such account NAME` (for transfer: FROM is checked, then TO)
5. (transfer) `same account` if FROM equals TO
6. (withdraw, transfer) `insufficient funds` if the balance is below AMT

Example:
```
open a
open b
deposit a 50
transfer a b 70
transfer a b 20
report
```
prints
```
opened a
opened b
a: 50
error: insufficient funds
a->b 20
a 30
b 20
total 50
```
