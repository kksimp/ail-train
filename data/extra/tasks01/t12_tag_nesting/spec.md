# Tag nesting check

Reads lines of HTML-like markup and reports whether the tags are properly nested.

Input: any number of lines. Empty lines are skipped (but still counted when numbering lines). Text outside tags is ignored. A tag is `<` up to the next `>`:
- `<name>` opens a tag,
- `</name>` closes the most recently opened tag,
- `<name/>` is self-closing and changes nothing.
A name is one or more lowercase letters or digits. Tags are numbered 1, 2, 3, ... within their line, in order of appearance (self-closing ones count too).

For each non-empty line, check the tags from left to right and stop at the first problem. Print `N: RESULT` where `N` is the 1-based line number and RESULT is the first applicable of:
- `unterminated tag`: a `<` has no `>` after it.
- `bad tag K`: tag number K has an invalid name (empty, or other characters).
- `unexpected close X at tag K`: a close tag `X` appears with nothing open.
- `mismatch at tag K: expected Y got X`: a close tag `X` while `Y` is the innermost open tag.
- `unclosed Y`: after the last tag, tags remain open; `Y` is the innermost one.
- `OK`: everything matched (also when there are no tags).

Example input:
```
<a><b>hi</b></a>
<a><b></a>
<br/><p>
```
Example output:
```
1: OK
2: mismatch at tag 3: expected b got a
3: unclosed p
```

Empty input prints nothing.
