# histogram

Reads a bucket width and then integers, and prints a text histogram of fixed-width buckets.

Input: the first line is the bucket width W, a positive integer. Every following whitespace-separated token is a value: an integer (optionally with a leading `-`). Tokens may be spread over any number of lines. A token that is not an integer is counted as invalid and otherwise ignored.

Bucket of a value v is floor(v / W) (floor division, so -1 with W=10 is in the bucket [-10, -1]). The bucket covers values from b*W to b*W+W-1.

Output: for every bucket from the lowest non-empty bucket to the highest non-empty bucket (including empty ones in between), one line `[LO..HI] COUNT BAR` where LO=b*W, HI=b*W+W-1, COUNT is the number of values in the bucket, and BAR is COUNT copies of `#`. Print `[LO..HI] 0` (no trailing space, no bar) for an empty bucket. Then print `total T invalid I`.

If the first line is missing, is not a positive integer, print `error: bad width` and nothing else. If there are no valid values print only the `total 0 invalid I` line.

Example (W=10, values 3 12 -1 15 3 x):
```
[-10..-1] 1 #
[0..9] 2 ##
[10..19] 2 ##
total 5 invalid 1
```
