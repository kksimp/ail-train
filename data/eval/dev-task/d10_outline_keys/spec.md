# Outline to dotted keys

Read an indentation-based outline (a tiny YAML-like subset) from standard input and print every value with its full dotted key path.

## Input
Lines (the input contains no tab characters). Lines are numbered from 1. A line that is empty or only spaces is skipped (it still counts for numbering).

For any other line:
- `sp` is the number of leading spaces; the rest of the line, with trailing spaces removed, is the text `t`.
- The key is the part of `t` before its first `:` with surrounding spaces removed; the value is the part after that first `:` with surrounding spaces removed (it may contain further colons and may be empty).
- The line is **bad** if `t` has no `:`, or `t` starts with `:` (empty key), or `sp` is odd, or `sp / 2` is greater than the current path length (see below).

## Rules
Keep a path (a list of keys), initially empty. The depth of a good line is `sp / 2`.
For a good line: cut the path down to its first `depth` keys, then append the line's key.
If the value is empty, the key stays on the path as a parent for the lines that follow.
If the value is not empty, print `PATH=VALUE` where PATH is all keys on the path joined with `.`, and then remove the key just added (a line with a value never becomes a parent).
A bad line prints `bad line N` (N is its line number) and changes nothing.

## Output
One line per printed value or bad line, in input order. No output at all for empty input.

## Example
Input:
```
server:
  host: example.org
  port: 8080
  tls:
    enabled: yes
    cert: /etc/a.pem
name: demo
```
Output:
```
server.host=example.org
server.port=8080
server.tls.enabled=yes
server.tls.cert=/etc/a.pem
name=demo
```
