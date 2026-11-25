# gcd_lcm_table

Reads a list of positive integers and prints a table of gcd and lcm for every pair.

Input: whitespace-separated tokens over any number of lines. Tokens that are positive decimal integers (digits only, value 1 to 1000000) are the numbers, in order; any other token is skipped and counted as ignored. At most 8 numbers are used; further valid numbers are not used but are counted as ignored too.

Output, in this order:
1. `numbers: A B C ...` listing the used numbers separated by single spaces (`numbers: none` if there are none).
2. For each pair i<j of used numbers in order (i ascending, then j ascending): `gcd(A,B)=G lcm(A,B)=L`.
3. If there are at least 2 numbers: `all gcd=G all lcm=L`, the gcd and lcm of every used number.
4. `ignored K`.

Example input: `12 18 x 5`
```
numbers: 12 18 5
gcd(12,18)=6 lcm(12,18)=36
gcd(12,5)=1 lcm(12,5)=60
gcd(18,5)=1 lcm(18,5)=90
all gcd=1 all lcm=180
ignored 1
```
The lcm of all numbers may exceed 10^12 but fits in 64 bits for these limits.
