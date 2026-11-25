# mustache: a tiny template engine

Write a program that reads variable definitions and a template from standard input and prints the rendered template.

## Input

- Definition part: the lines before the first line that is exactly `---`. If there is no `---` line, the whole input is the definition part and there is no template.
- Template part: all lines after that `---` line (it may be empty).

If the input ends with a newline, that final newline does not start another line. Empty lines elsewhere are real lines. Lines are numbered from 1 (see below).

## Definitions

Each definition line is processed in order:

- A line that is empty or only spaces is ignored.
- Otherwise split the line at its FIRST `=`. The text before it, with surrounding spaces removed, is the name; the text after it, taken exactly as written (no trimming), is the value (it may be empty or contain more `=`).
- A name is valid when it is non-empty and made only of ASCII letters, digits and `_`. If the line has no `=` or the name is not valid, print `error: definition N: malformed` where N is the line's number in the whole input (the first input line is line 1), and ignore the line.
- A later definition of a name replaces an earlier one.

These error lines are printed first, in order, before any template output.

## Template lines

Template lines are numbered T = 1, 2, ... starting with the first line after `---`. Process them in order, keeping a stack of open blocks.

Control lines. After removing spaces and tabs from both ends, a line is a control line if it is exactly `{{else}}` or `{{/if}}`, or if it starts with `{{#if ` or `{{#unless ` and ends with `}}`; in the last two cases the variable name is the text between the opening tag and the final `}}`, trimmed of spaces (it is always a valid name). A variable is TRUE when it is defined and its value is not empty. Control lines print nothing themselves:

- `{{#if NAME}}` opens a block whose condition is "NAME is true"; `{{#unless NAME}}` opens one whose condition is "NAME is not true".
- `{{else}}` flips the innermost open block to its other branch. If no block is open, print `error: line T: unexpected else`. If the innermost block already had its `{{else}}`, print `error: line T: duplicate else`. Neither changes the stack.
- `{{/if}}` closes the innermost block (it closes `#unless` blocks too). If no block is open, print `error: line T: unexpected /if`.

A line is ACTIVE when every open block is currently in a branch that is on: a block is on in its first branch when its condition holds (and its second, after `{{else}}`, when the condition does not hold), and a block opened while an enclosing block was off is off in both branches. Control lines are processed (they open, flip and close blocks, and can print the errors above) whether or not they are active. Every other line that is not active is skipped entirely and produces nothing, not even errors.

Ordinary lines (not control lines) that are active are rendered as follows. Scan left to right for `{{`. The tag extends to the next `}}` after it (so in `{{{a}}}` the tag text is `{a`). If there is a `{{` with no `}}` after it, the line fails with `unclosed tag`. The tag text is trimmed of spaces; if it contains `|`, split at the first `|` into a name and a default, each trimmed. The name must be valid (as defined above), otherwise the line fails with `bad tag`. The tag is replaced by:

1. the variable's value, if the variable is defined and its value is not empty;
2. else the default, if the tag has one (even if it is empty);
3. else the empty string, if the variable is defined (with an empty value);
4. else the line fails with `undefined NAME`.

Replacement text is never scanned again, and text outside tags is copied unchanged (including all spaces). Tags are handled left to right and the first failure is the one reported. When a line fails, print `error: line T: MESSAGE` instead of the line, and continue with the next line.

## End

After the last template line, if any block is still open, print `error: unclosed block` once.

## Output

Everything above is printed to standard output in the order produced.

## Example

Input:

```
name=World
n=3
---
Hello, {{name}}!
{{#if n}}
n is {{ n }}, mode {{mode|plain}}
{{else}}
n is empty
{{/if}}
{{#unless missing}}
done {{oops}}
```

Output:

```
Hello, World!
n is 3, mode plain
error: line 8: undefined oops
error: unclosed block
```
