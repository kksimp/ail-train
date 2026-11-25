# Daily inventory with reorder

Simulate a shop that sells one product each day and reorders stock when it runs low.

## Input (standard input)

- Line 1 (header): four whitespace-separated tokens `START REORDER QTY LEAD`: starting stock, reorder point, order quantity, order lead time in days. Every token must consist of decimal digits only, `QTY >= 1` and `LEAD >= 1`. If the input is empty or the header is invalid, print only `bad header` and stop.
- Every following line is one day's demand. Surrounding spaces on a line are ignored. Lines that are empty (or only spaces) are skipped silently and do not count as a day.
- A line whose trimmed text is not a whole number written as an optional `-` followed by digits, or is a negative number, is bad: print `line L: bad demand` (L is the 1-based line number in the input, header is line 1) and skip it; it does not count as a day.

## Rules

Days are numbered 1, 2, 3, ... counting only valid demand lines. Keep the current stock and a list of pending orders (arrival day, quantity). For each day `d` with demand `D`, in this order:

1. Every pending order arriving on day `d` is delivered: add its quantity to the stock and print `  received Q` (two leading spaces) for each, in the order the orders were placed. Delivered orders are no longer pending.
2. Sell `min(D, stock)` units; the rest of the demand (`D - sold`) is lost. Subtract the sold units from the stock. Print `day d: demand D sold S lost L stock E` where `E` is the stock after selling.
3. Let the position be the stock plus the quantities of all orders still pending. If position `<= REORDER`, place a new order of `QTY` units arriving on day `d + LEAD` and print `  ordered QTY arriving day X` (two leading spaces). Several orders may be pending at once.

## Output

The lines described above, in input order, followed by two summary lines:

```
total sold X lost Y orders Z
final stock S
```

where X and Y are the totals of units sold and lost, Z is the number of orders placed, and S is the stock after the last day (orders still pending are not delivered). With no valid days the totals are 0 and the final stock is `START`.

## Example

Input:

```
5 3 10 3
4
4
4
4
4
4
```

Output:

```
day 1: demand 4 sold 4 lost 0 stock 1
  ordered 10 arriving day 4
day 2: demand 4 sold 1 lost 3 stock 0
day 3: demand 4 sold 0 lost 4 stock 0
  received 10
day 4: demand 4 sold 4 lost 0 stock 6
day 5: demand 4 sold 4 lost 0 stock 2
  ordered 10 arriving day 8
day 6: demand 4 sold 2 lost 2 stock 0
total sold 15 lost 9 orders 2
final stock 0
```
