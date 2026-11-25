# Vending machine with coins

Standard input: one command per line. The machine starts with no stock, no coins and no credit. Commands:
- `stock NAME PRICE QTY`: sets the price (cents, > 0) of NAME and adds QTY (>= 1) to its quantity. Prints nothing.
- `coin C`: C must be 5, 10, 25 or 100. The coin goes into the machine's coin bank and adds C to the credit; print `credit=N`. Any other coin prints `rejected C` and changes nothing.
- `select NAME`: if NAME was never stocked print `unknown NAME`; if its quantity is 0 print `sold out NAME`; if credit < price print `need K more` (K cents short).
  Otherwise change = credit - price is paid out from the bank taking the largest coins first (100, 25, 10, 5), each as often as the bank holds that coin and as the remaining change allows.
  If the change cannot be paid exactly this way, print `no change` and nothing else happens. Otherwise the quantity drops by 1, the credit becomes 0, the paid coins leave the bank, and print `vend NAME change=X`,
  where X lists the coins paid out, largest first, joined by `+` (e.g. `25+10+10`), or `none` for no change.
- `refund`: pays the credit back from the bank the same way; print `refund X` (X as above, `none` if the credit was 0), credit becomes 0. If it cannot be paid exactly print `no change` and keep the credit.
Any other line (unknown command, missing or non-numeric arguments, wrong argument count, blank line) prints `bad command`.
At the end print `credit=N`, then one line `stock NAME QTY` for every stocked name in alphabetical order.

Example:
    input:  stock cola 65 2
            coin 25
            coin 25
            coin 25
            coin 10
            coin 5
            select cola
            select cola
    output: credit=25
            credit=50
            credit=75
            credit=85
            credit=90
            vend cola change=25
            need 65 more
            credit=0
            stock cola 1
