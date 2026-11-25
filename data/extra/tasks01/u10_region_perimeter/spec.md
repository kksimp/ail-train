# region_perimeter

Reads a grid of letters and reports every connected region with its area and perimeter.

Input: non-empty lines, each a row of the same width, made of letters. Empty lines are ignored. Two cells are in the same region if they hold the same letter and are neighbours up, down, left or right (not diagonally).

Output: one line per region, `LETTER AREA PERIMETER`, ordered by the region's first cell in reading order (top row first, then left to right). AREA is the number of cells. PERIMETER is the number of unit cell edges of the region that touch either the grid border or a cell of a different region (a region with a hole counts the hole's edges too).
After the region lines print `regions N` with the number of regions. Empty input prints `regions 0`.

Example input:
```
AAB
ABB
```
Output:
```
A 3 8
B 3 8
regions 2
```
