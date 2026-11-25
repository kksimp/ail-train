# running_stats

Reads lines from standard input, one integer per line, and prints running statistics after each valid integer.

Input: each line is an optionally negative decimal integer (`-?[0-9]+`, at most 9 digits) with optional surrounding spaces or tabs. An empty line (or one containing only spaces) is skipped silently.

Output: for each valid integer, one line `K: sum=S min=A max=B mean=M` where K is the 1-based count of valid integers so far, S the running sum, A and B the running minimum and maximum, and M the running mean S/K with exactly two decimals, truncated toward zero (not rounded). A negative mean prints a leading `-` (for example -7/3 gives `-2.33`; a mean that truncates to zero prints `0.00`, never `-0.00`).

A line that is not empty and not a valid integer prints `bad line N` where N is the 1-based physical line number, and does not change the statistics.

At the end, if no valid integer was seen print `no data`; otherwise print `done K`.

Example input:
```
5
-8
x1
4
```
Output:
```
1: sum=5 min=5 max=5 mean=5.00
2: sum=-3 min=-8 max=5 mean=-1.50
bad line 3
3: sum=1 min=-8 max=5 mean=0.33
done 3
```
