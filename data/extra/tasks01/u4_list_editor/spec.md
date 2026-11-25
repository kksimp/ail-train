# Doubly linked list editor

Read commands from standard input, one per line, and edit a sequence of words with a cursor. The sequence starts empty. The cursor sits between items or at the end: it points at the item that would be removed by `del`, or at the end position if it is past the last item. It starts at the end.
Words are separated by spaces; blank lines are ignored. An item is a single word without spaces.

Commands and output (one output line per command):
- `ins W`: insert item W immediately before the cursor position; the cursor still points at the same item (or the end). Prints `ok`.
- `del`: remove the item at the cursor; the cursor then points at the following item (or the end). Prints the removed item, or `nothing` if the cursor is at the end.
- `left`: move the cursor one item toward the front. Prints `ok`, or `edge` if it is already at the front.
- `right`: move the cursor one item toward the end. Prints `ok`, or `edge` if it is already at the end.
- `home`: move the cursor to the front. Prints `ok`.
- `end`: move the cursor to the end. Prints `ok`.
- `show`: print all items from front to back separated by single spaces, with the item under the cursor wrapped in brackets like `[x]`; if the cursor is at the end print `|` as a final word. An empty list prints `|`.
- `rshow`: print all items from back to front separated by single spaces, with no cursor mark; prints `empty` for an empty list.

Any other line (unknown command, missing word, extra words) prints `error` and changes nothing.

Example input:
    ins a
    ins b
    left
    show
    ins c
    show
    del
    show
    rshow
Output:
    ok
    ok
    ok
    a [b]
    ok
    a c [b]
    b
    a c |
    c a
