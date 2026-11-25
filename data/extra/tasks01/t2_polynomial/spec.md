# polynomial

Reads an integer polynomial and a list of points, prints its derivative and evaluates both at each point.

Input: the first line lists the coefficients from the highest degree down to the constant term, separated by spaces (1 to 7 integers, each from -100 to 100; the first one may be 0). Every following non-empty line holds one integer x from -100 to 100.

Output: first `p(x) = TEXT` and `p'(x) = TEXT` where TEXT is the polynomial in the usual written form: terms from the highest degree with a non-zero coefficient down, joined by ` + ` or ` - ` (a negative first term starts with `-`), coefficient 1 omitted except for the constant term, `x` for degree 1, `x^k` for degree k >= 2; a polynomial with all coefficients zero prints `0`. Example: coefficients `2 -3 0 5` print `2x^3 - 3x^2 + 5`. Then for each x line, in order: `x=X p=V dp=W`, the value of the polynomial and of its derivative at X.

Errors: if the first line is missing or has a token that is not an integer in range, or more than 7 coefficients, print `error: bad coefficients` and nothing else. A later non-empty line that is not an integer in range prints `line K: bad point` (K is its 1-based physical line number) and is otherwise skipped.

Example input:
```
1 0 -2
3
-1
```
Output:
```
p(x) = x^2 - 2
p'(x) = 2x
x=3 p=7 dp=6
x=-1 p=-1 dp=-2
```
