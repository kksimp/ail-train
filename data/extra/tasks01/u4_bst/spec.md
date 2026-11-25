# Binary search tree commands

Read commands from standard input, one per line, and operate on a binary search tree of distinct integers, initially empty.
Words are separated by spaces; blank lines are ignored.

Commands and output (one output line per command):
- `insert N`: add N; prints `ok`, or `dup` if N is already present (tree unchanged).
- `delete N`: remove N; prints `ok`, or `missing` if absent. A node with two children is replaced by the smallest value of its right subtree (which is then removed from there); a node with at most one child is replaced by that child.
- `contains N`: prints `yes` or `no`.
- `inorder`: prints all values in ascending order separated by single spaces, or `empty` if the tree is empty.
- `height`: prints the number of nodes on the longest root-to-leaf path (0 for the empty tree).
- `min`: prints the smallest value, or `empty`.

Any other line (unknown command, missing or non-integer N, extra words) prints `error` and changes nothing.
Negative N is allowed.

Example input:
    insert 5
    insert 3
    insert 8
    insert 3
    inorder
    delete 5
    inorder
    height
Output:
    ok
    ok
    ok
    dup
    3 5 8
    ok
    3 8
    2
