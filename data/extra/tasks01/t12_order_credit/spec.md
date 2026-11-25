# Order rule checks with credit limits

Reads commands that manage customer credit and applies the order rules.

Input: one command per line, words separated by spaces. Empty lines are skipped (but still counted when numbering lines). Amounts are positive whole numbers.
- `limit NAME AMOUNT`: sets the credit limit of customer NAME (creating the customer with 0 used if new; an existing customer keeps what it has used).
- `order NAME AMOUNT`: the order is accepted when used + AMOUNT does not exceed the limit; accepted orders increase `used`.
- `pay NAME AMOUNT`: decreases `used`; it is rejected if AMOUNT is more than `used`.
- `report`: lists every customer.

Output lines, one or more per command:
- `limit`: `LIMIT NAME AMOUNT`
- accepted order: `ACCEPT NAME AMOUNT balance USED/LIMIT` (the new used amount)
- order over the limit: `REJECT NAME AMOUNT: over limit by X` where X is how far used + AMOUNT exceeds the limit
- `pay` accepted: `PAID NAME AMOUNT balance USED/LIMIT`; too large: `REJECT NAME AMOUNT: overpayment`
- `order` or `pay` for a customer with no limit yet: `REJECT NAME: unknown customer`
- `report`: one line `NAME USED/LIMIT` per customer sorted by name, or `no customers` if there are none
- an amount that is not a positive integer: `ERROR line N: bad amount`; an unknown command word or wrong number of words: `ERROR line N: bad command` (N is the 1-based input line number; `report` takes no arguments)

Example input:
```
limit ann 500
order ann 300
order ann 250
pay ann 100
report
```
Example output:
```
LIMIT ann 500
ACCEPT ann 300 balance 300/500
REJECT ann 250: over limit by 50
PAID ann 100 balance 200/500
ann 200/500
```

Empty input prints nothing.
