# matmul

Reads two integer matrices from standard input and prints their product.

Input: the first line is `R1 C1`, followed by R1 lines of C1 integers separated by spaces (matrix A). Then a line `R2 C2`, followed by R2 lines of C2 integers (matrix B). Numbers are whitespace-separated; values fit comfortably in 32 bits and may be negative. Dimensions are at least 1.

Output: if C1 != R2 print `error: cannot multiply RxC by RxC` using the actual dimensions, e.g. `error: cannot multiply 2x3 by 2x2`. Otherwise print the R1 x C2 product, one row per line, entries separated by a single space, each entry right-aligned in a column whose width is the longest entry of the whole product matrix (so columns line up; a negative sign counts toward the width). Then print `trace T` if the product is square (T is the sum of its diagonal), or `shape RxC` otherwise.

If the input is malformed (missing numbers, a non-integer token, or an unreadable dimension line) print `error: bad input` and nothing else. Extra trailing tokens after matrix B are ignored.

Example input:
```
2 2
1 2
3 4
2 2
0 -1
5 6
```
Output:
```
10 11
20  21
trace 31
```
