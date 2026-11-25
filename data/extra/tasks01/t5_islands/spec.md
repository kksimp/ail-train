Standard input is a map: lines made of the characters `1` (land) and `0` (water). Any other character counts as water.
Blank lines are ignored. Lines may have different lengths; a missing cell is water.
An island is a maximal group of land cells connected up, down, left or right (not diagonally).

Print two lines:
`islands: K` with the number of islands, and
`largest: M` with the number of cells of the biggest island (0 if there is none).

Example input:
```
11001
10001
00100
00011
```
Output:
```
islands: 3
largest: 3
```
