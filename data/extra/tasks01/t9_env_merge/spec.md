# env_merge

Merge two environment-file blocks read from standard input.

Input: lines. The first line that is exactly `---` ends the base block; every line after it (including any later `---`) belongs to the override block. With no `---` line, everything is the base block.

Within a block:
- empty lines and lines starting with `#` are ignored;
- an entry is `KEY=VALUE`, optionally preceded by `export ` (the word and one space). Split at the first `=`. KEY (trimmed) must be a letter or `_` followed by letters, digits or `_`. VALUE is trimmed and kept exactly as written (quotes are not removed). `KEY=` sets an empty value;
- in the override block only, a line `-KEY` (a valid key after a `-`) deletes that key if present;
- any other line is malformed and counted.

Apply the base entries in order, then the override block in order, to an ordered map: setting an existing key changes its value and keeps its position, setting a new key appends it, deleting removes it (setting it again later appends it).

Output: one `KEY=VALUE` line per key in map order. If any line was malformed, finish with `# skipped N`.

Example input:
```
HOST=localhost
PORT=80
export DEBUG=1
---
PORT=8080
-DEBUG
NAME="demo app"
bad line
```
Example output:
```
HOST=localhost
PORT=8080
NAME="demo app"
# skipped 1
```
