# Token bucket rate limiter

Decide which requests a per-key token bucket rate limiter allows.

Input: first non-blank line `capacity C rate R` with integers C >= 1 and R >= 0, else print `bad header` and stop.
Each later non-blank line is a request `TIME KEY` or `TIME KEY COST` with integers TIME >= 0 and COST >= 1 (default 1).

Every KEY has its own bucket. A bucket is created at the TIME of the key's first request, holding C tokens. Before each request the
bucket gains R tokens per elapsed time unit since its last request, never exceeding C. The request is allowed when the bucket holds at
least COST tokens, and then COST tokens are removed; otherwise it is denied and the bucket is unchanged (apart from the refill).
A request with COST > C is always denied.
A request whose TIME is lower than the TIME of the previous valid request, or any malformed line, is invalid: print `? ` and the trimmed line
and otherwise ignore it.

Output: for each valid request one line `TIME KEY COST allow left=N` or `TIME KEY COST deny left=N` where N is the bucket's tokens
after processing. Then one summary line per key in order of first appearance `KEY allowed=A denied=D`.

Example input:
    capacity 3 rate 1
    0 a
    0 a 2
    0 a
    2 a
    2 b
Output:
    0 a 1 allow left=2
    0 a 2 allow left=0
    0 a 1 deny left=0
    2 a 1 allow left=1
    2 b 1 allow left=2
    a allowed=3 denied=1
    b allowed=1 denied=0
