# Pattern matcher with character classes

Each input line holds a pattern and a text; for each line report whether the whole text matches the pattern.

## Input
Lines are numbered from 1. A line is the pattern, then one space, then the text: the pattern is everything before the **first** space (it may be empty), and the text is everything after that space (it may be empty and may contain further spaces). A line with no space at all is a bad line. Every line produces output (empty lines are bad lines). All characters are ASCII.

## Pattern syntax
A pattern is a sequence of items, each optionally followed by one quantifier:
- A literal character matches itself. Every character that is not special is literal, including `^`, `]`, `-`, `+` and `\` outside a class. There are no escapes.
- `.` matches any single character.
- `[...]` is a character class matching one character. The class body is the characters after `[` (and after an optional leading `^`) up to the first `]` after that. A leading `^` negates the class (any character not listed). Inside the body, scanning left to right at position `k` with `L` the body length: if `k + 2 < L` and the character at `k + 1` is `-`, then `body[k]-body[k+2]` is an inclusive range of character codes and scanning continues at `k + 3`; otherwise `body[k]` is a single character and scanning continues at `k + 1`. So `-` is a plain character when it is first, last, or otherwise not between two characters (`[a-]`, `[-a]`), and `.`, `*`, `?`, `[`, `^` (not first) are plain characters inside a class.
- Quantifiers: `*` (zero or more repetitions of the preceding item) and `?` (zero or one).

The text must match the **entire** pattern (anchored at both ends).

A pattern is **bad** if: a `[` has no closing `]`; a class body is empty (`[]`, `[^]`); a range has its first character code greater than its last (`[z-a]`); or a quantifier (`*` or `?`) appears with no item before it (at the start) or directly after another quantifier (`a**`, `a*?`). Bad patterns are reported even if the text is empty or irrelevant.

## Output
For line N print `N: bad line`, `N: bad pattern`, `N: match` or `N: no match` (a line with no space is reported as bad line before the pattern is examined).

## Example
Input:
```
abc abc
a.c axc
a.c ac
[a-c]x bx
[a-c]x dx
[^0-9]* hello
[^0-9]* he1lo
colou?r colour
[0-9]*.[0-9] 12.5
.* anything at all
```
Output:
```
1: match
2: match
3: no match
4: match
5: no match
6: match
7: no match
8: match
9: match
10: match
```
