# outline

Convert an indented outline on standard input into a numbered list.

Input: one item per line, indented with spaces only. Each nesting level is exactly 2 spaces. Lines that are empty or only spaces are ignored but still count for line numbers (the first line is line 1). The text of an item is the line with surrounding spaces removed.

Rules for a non-blank line with `S` leading spaces:
- If `S` is odd, or the level `S / 2` is more than one deeper than the previous accepted item (the first accepted item must be at level 0), the line is rejected: print `error: line K: bad indent` (K is its line number) and carry on; a rejected line does not change the numbering.
- Otherwise the line is accepted. Its number is the path of counters from level 0 down to its level, joined by `.`. A counter counts accepted items at that level since the parent item began. Print `NUMBER TEXT`.

Example input:
```
Fruit
  Apple
  Pear
    Conference
Veg
   odd
      jump
  Leek
```
Example output:
```
1 Fruit
1.1 Apple
1.2 Pear
1.2.1 Conference
2 Veg
error: line 6: bad indent
error: line 7: bad indent
2.1 Leek
```
