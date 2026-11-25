# distance_map

Computes, for every cell of a map, the walking distance to the nearest source.

Input: non-empty lines forming a grid of equal width (empty lines ignored). `S` is a source, `#` is a wall, any other character is open floor. Moves go one cell up, down, left or right through non-wall cells; each move costs 1.

Output: the grid as rows of cells separated by single spaces. A source prints `0`, an open cell its distance to the nearest source as a decimal number, a wall `#`, and an open cell that no source can reach `-`. After the grid print `reachable R unreachable U farthest F`, where R counts open cells (not sources, not walls) with a distance, U counts the unreachable open cells, and F is the largest distance (0 if none). If the grid has no `S`, print `no sources` and nothing else. Empty input also prints `no sources`.

Example input:
```
S..#
.#..
...S
```
Output:
```
0 1 2 #
1 # 2 1
2 2 1 0
reachable 8 unreachable 0 farthest 2
```
