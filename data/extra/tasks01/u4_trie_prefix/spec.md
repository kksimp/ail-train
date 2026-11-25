# Trie prefix counts

Read commands from standard input, one per line, and maintain a multiset of lowercase words (a trie), initially empty.
Words are separated by spaces; blank lines are ignored. A word is one or more letters `a`-`z`.

Commands and output (one output line per command):
- `add WORD`: insert one occurrence of WORD. Prints `ok`.
- `del WORD`: remove one occurrence of WORD; prints `ok`, or `missing` if it is not present.
- `has WORD`: prints how many occurrences of exactly WORD are stored.
- `count PREFIX`: prints how many stored occurrences start with PREFIX (a word is a prefix of itself).
- `longest PREFIX`: prints the longest common prefix shared by all stored words that start with PREFIX, or `none` if no stored word starts with PREFIX.

Any other line (unknown command, missing word, a word with characters outside `a`-`z`, extra words) prints `error` and changes nothing.

Example input:
    add car
    add cart
    add cat
    count ca
    count car
    longest ca
    del cat
    longest ca
Output:
    ok
    ok
    ok
    3
    2
    ca
    ok
    car
