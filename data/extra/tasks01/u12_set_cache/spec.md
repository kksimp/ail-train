# Set-associative cache

Simulate a set-associative cache and report hits and misses.

Input: first non-blank line `cache SETS WAYS BLOCK policy P` with integers SETS, WAYS, BLOCK all >= 1 and P either `lru` or `fifo`;
otherwise print `bad header` and stop. All later lines hold memory addresses (integers >= 0) separated by whitespace, accessed in order.
A token that is not a non-negative integer is skipped and counted.

For an address A: block = A / BLOCK (integer division), set = block % SETS, tag = block / SETS. Each set holds up to WAYS tags.
A hit is an access whose tag is present in its set. On a miss the tag is inserted; if the set is already full, the victim is evicted first:
with `lru` the least recently used tag (a hit refreshes recency), with `fifo` the tag that was inserted earliest (hits do not change order).

Output: one line per access `ADDR set=S hit` or `ADDR set=S miss`; then
    hits=H misses=M ratio=R skipped=K
where R is the hit ratio in percent with two decimals, truncated (hits*10000/total as integer, shown as `X.YY`; `0.00` if there were no
accesses).

Example input:
    cache 2 1 4 policy lru
    0 4 8 0
Output:
    0 set=0 miss
    4 set=1 miss
    8 set=0 miss
    0 set=0 miss
    hits=0 misses=4 ratio=0.00 skipped=0
