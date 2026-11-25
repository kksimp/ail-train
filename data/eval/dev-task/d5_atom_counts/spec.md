# d5_atom_counts

Write a command-line program that reads chemical formulas from standard input and prints how many atoms of each element each formula contains.

## Input

Zero or more lines, each holding one formula. Leading and trailing whitespace on a line is removed first; lines that are then empty are ignored. Formulas contain only letters, digits and round parentheses.

## Formula grammar

- An element symbol is one upper-case ASCII letter, optionally followed by one lower-case ASCII letter (`H`, `O`, `Na`, `Cl`). Any symbol of this shape is accepted; there is no element table. A symbol may be followed by a count.
- A group is `(` formula `)`, optionally followed by a count. Groups may be nested to any depth. Every atom inside a group is counted as many times as the group's count says.
- A count is one to three ASCII digits whose value is at least 1. A missing count means 1. Counts such as `0`, `00` or `1000` (four digits) are invalid.
- A formula is a sequence of element symbols and groups. It must contain at least one atom; a group must not be empty. Unbalanced parentheses, a count that does not follow a symbol or `)` (for example at the start or right after `(`), a lower-case letter that does not follow an upper-case letter, and any other character make the formula invalid.

The same element may appear many times; its counts add up. All totals fit in 64 bits.

## Output

One line per non-blank input line, in input order, with the formula text as trimmed:

- valid: `FORMULA: SYM=COUNT SYM=COUNT ... total=T`, the elements sorted by symbol in ascending byte order (plain string comparison, so `C` comes before `Ca`, and `Ca` before `Cl`), separated by single spaces, and T the sum of all counts.
- invalid: `FORMULA: invalid`

No formulas produce no output.

## Example

Input:

```
H2O
Mg(OH)2
K4(Fe(CN)6)

Al2(SO4)3
(NH4)2CO3
Ca(OH
2H
```

Output:

```
H2O: H=2 O=1 total=3
Mg(OH)2: H=2 Mg=1 O=2 total=5
K4(Fe(CN)6): C=6 Fe=1 K=4 N=6 total=17
Al2(SO4)3: Al=2 O=12 S=3 total=17
(NH4)2CO3: C=1 H=8 N=2 O=3 total=14
Ca(OH: invalid
2H: invalid
```
