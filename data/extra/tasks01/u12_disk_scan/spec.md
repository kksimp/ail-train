# Disk scheduling with SCAN

Compute the service order and head movement of the SCAN (elevator) disk scheduling algorithm.

Input: first non-blank line `disk C head H dir D` where C >= 1 is the number of cylinders (numbered 0..C-1), H is the starting
head position (0 <= H < C) and D is `up` or `down`. Otherwise print `bad header` and stop.
All later lines hold cylinder requests, integers separated by whitespace. A token that is not an integer, or an integer outside 0..C-1,
is skipped and counted.

SCAN: the head first moves in direction D serving requests on the way, in order of position, and continues to the physical end of
the disk (cylinder C-1 for `up`, 0 for `down`) only if some requests lie on the other side of the head. It then reverses and serves the
rest. With `up` the first group is requests >= H (ascending), the second is requests < H (descending). With `down` the first group is
requests <= H (descending), the second is requests > H (ascending). A request equal to a position already served is still served
(distance 0). Duplicates stay duplicates.

Output three lines:
    order=R1 R2 ...    (requests in service order; empty after = if none)
    path=H P1 P2 ...   (head positions visited: start, each request, and the disk end when the head went there)
    movement=M skipped=K   (total cylinders travelled, count of skipped tokens)

Example input:
    disk 200 head 50 dir up
    95 180 34 119 11 123 62 64
Output:
    order=62 64 95 119 123 180 34 11
    path=50 62 64 95 119 123 180 199 34 11
    movement=337 skipped=0
