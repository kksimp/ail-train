# recipe_cost

Write `recipe_cost`, a command-line program. It reads a kitchen's ingredient prices and recipes from standard input and prints what each recipe costs.

## Input

One command per line, fields separated by one or more spaces. Lines that are empty or contain only spaces are skipped silently (they still count when numbering lines: the first input line is line 1). Names (`ITEM`, `NAME`) are any text without spaces. Every number is made only of digits (1 to 6 digits, leading zeros allowed, no sign).

- `price ITEM CENTS PER`: `PER` units of `ITEM` cost `CENTS` cents (for example `price flour 250 1000` means 1000 grams cost 250 cents). `CENTS` may be 0; `PER` must be at least 1. A later `price` line for the same item replaces the earlier one, even for recipes that came before it: costing happens after all input has been read, using the final prices.
- `recipe NAME SERVINGS`: starts a new recipe that makes `SERVINGS` servings (at least 1). Two recipes may share a name; they are separate recipes.
- `use ITEM QTY`: the most recently started recipe uses `QTY` units of `ITEM` (at least 1). The same item may be used several times in one recipe; each `use` line is costed on its own.

Any other line, or a line of a known command with the wrong number of fields or an invalid number, is a bad line. A `use` line before any `recipe` line is not bad but has no recipe to belong to.

## Messages while reading

These are printed first, in input order, as the lines are read:

- bad line: `line K: bad line`
- valid `use` with no recipe started yet: `line K: no recipe`

where `K` is the line number. Such lines change nothing.

## Rules

For each `use` of an item that has a price: cost is `ceil(QTY * CENTS / PER)` cents (round up to a whole cent, per `use` line). The recipe total is the sum of those costs. The cost per serving is `ceil(total / SERVINGS)` cents. A recipe with no `use` lines has total 0.

If a recipe uses any item that has no price, it cannot be costed.

## Output

After the messages above, one line per recipe in input order:

- costed: `NAME: total T, per serving P`
- not costed: `NAME: missing A, B` listing the unpriced items, each once, in the order they first appear in that recipe, separated by `, `.

Cents are written as dollars with exactly two decimals: `T` and `P` print as `D.CC` (for example 5 cents is `0.05`, 1234 cents is `12.34`).

Finally, if at least one recipe was costed, print `most expensive per serving: NAME` for the costed recipe with the highest per-serving cost (the first one in input order wins ties). If no recipe was costed, print nothing more.

## Example

Input:

```
price flour 250 1000
price egg 30 1
price milk 120 1000
recipe pancakes 4
use flour 300
use egg 2
use milk 450
use butter 20
recipe crepes 6
use flour 250
use milk 500
use milk 3
recipe tea 1
price butter 900 500
oops
use salt 5
```

Output:

```
line 15: bad line
pancakes: total 2.25, per serving 0.57
crepes: total 1.24, per serving 0.21
tea: missing salt
most expensive per serving: pancakes
```

(`pancakes` is costed because `butter` is priced later in the input: flour 75 + egg 60 + milk 54 + butter 36 = 225 cents. `crepes`: 63 + 60 + 1 = 124 cents.)
