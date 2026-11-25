# LRU cache commands

The first line of input is the cache capacity, an integer of at least 1. If it is missing or invalid, print `bad capacity` and stop. Every following line is a command (words separated by spaces; blank lines ignored). Keys and values are single words.

Commands:
- `put K V`: if K is cached, replace its value, mark it most recently used and print `updated K`. Otherwise insert it as most recently used and print `stored K`; if the cache is now over capacity, also print `evict X` on the next line, where X is the least recently used key, which is removed.
- `get K`: if K is cached, print its value and mark it most recently used. Otherwise print `miss`.
- `peek K`: like `get` but does not change the usage order and is not counted in the statistics.
- `keys`: print all keys from most to least recently used separated by single spaces, or `(empty)`.
- `stats`: print `hits H misses M evictions E`, counting `get` hits, `get` misses and evictions so far.

Any other line prints `error: bad command`.

Example (capacity 2):
```
2
put a 1
put b 2
get a
put c 3
keys
get b
stats
```
prints
```
stored a
stored b
1
stored c
evict b
c a
miss
hits 1 misses 1 evictions 1
```
