# named set operations

Read commands from standard input, one per line (words separated by spaces; blank lines ignored). The program keeps named sets of words. A set prints as `{` + its elements in ascending byte order separated by single spaces + `}`, so the empty set is `{}`.

Commands:
- `set NAME E...`: define NAME (replacing any old set) with the given elements, duplicates collapsed; zero elements are allowed. Prints `NAME = SET`.
- `union R A B`, `inter R A B`, `diff R A B`: store in R the union, intersection or difference (elements of A not in B) of sets A and B. R may be A or B. Prints `R = SET`.
- `show NAME`: prints `SET`.
- `size NAME`: prints the element count.
- `subset A B`: prints `yes` if every element of A is in B (the empty set is a subset of anything), else `no`.
- `del NAME`: removes the set, prints `deleted NAME`.
- `names`: prints the defined names ascending separated by single spaces, or `(none)`.

Errors print `error: MESSAGE` and change nothing: `bad command` (unknown command or wrong word count; `set` and `names` aside, counts are fixed), `unknown set X` where X is the first operand name (in the order written, result name excluded) that is not defined.

Example:
```
set a x y z
set b y z w
inter c a b
diff d a b
subset c a
names
```
prints
```
a = {x y z}
b = {w y z}
c = {y z}
d = {x}
yes
a b c d
```
