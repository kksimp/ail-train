# English auction

Run a single-item ascending (English) auction from a list of bids.

## Input (standard input)

- Line 1: two non-negative integers separated by spaces: `RESERVE INCREMENT`.
- Every following line is a bid: `NAME AMOUNT`, fields separated by spaces (extra spaces around fields are allowed). `NAME` is a word without spaces; `AMOUNT` should be a positive integer.
- Lines that are empty or contain only spaces are skipped silently.
- If there is no input at all, print only `no auction`.

## Rules

Bids are processed in order. A bid line that does not have exactly two fields, or whose amount is not a whole number written with an optional leading `-` and digits, or whose amount is 0 or negative, is malformed: print `line L: malformed` where `L` is the 1-based line number in the input (the header is line 1, skipped lines count), and ignore it.

For a well-formed bid, let the required amount be `RESERVE` if there is no accepted bid yet, otherwise the current highest amount plus `INCREMENT`. The bid is accepted if its amount is at least the required amount AND its bidder is not the current highest bidder. Otherwise it is rejected. An accepted bid becomes the new highest bid.

## Output

For every well-formed bid print `NAME AMOUNT accepted` or `NAME AMOUNT rejected` (amount printed as a plain integer). Malformed lines print the message above, in input order.

At the end print `winner NAME at AMOUNT` for the highest accepted bid, or `no sale` if no bid was accepted.

## Example

Input:

```
50 5
ann 40
bob 50
cy 52
cy 60
ann 60
dee 65
bob 64
ann 100
```

Output:

```
ann 40 rejected
bob 50 accepted
cy 52 rejected
cy 60 accepted
ann 60 rejected
dee 65 accepted
bob 64 rejected
ann 100 accepted
winner ann at 100
```
