# Tokenizer

Read standard input and split every line into tokens. Spaces and tabs between tokens are skipped. For each token print
`LINE:COL KIND TEXT` where LINE is the 1-based line number, COL the 1-based character column where the token starts, and
TEXT the exact source text of the token.

Token kinds:
- `KEYWORD`: one of `if`, `else`, `while`, `return`;
- `IDENT`: a letter or `_` followed by letters, digits or `_` (and not a keyword);
- `FLOAT`: digits, a `.`, then at least one digit (`3.14`); `INT`: other digit runs;
- `STRING`: from a `"` to the next `"` on the same line, quotes included, no escapes;
- `OP`: two-character `==`, `!=`, `<=`, `>=`, `->`, else a single one of `+ - * / % < > = !`;
- `PUNCT`: one of `( ) { } , ; :`;
- `ERROR`: any other character (TEXT is that character), or an unterminated string (TEXT is the rest of the line
  starting at the opening quote; scanning of that line then stops).
Longest match wins (`<=` is one OP, `3.` is INT `3` followed by ERROR `.`).

Example input:
    if x1 >= 3.5 {
      return "hi"
    }

Example output:
    1:1 KEYWORD if
    1:4 IDENT x1
    1:7 OP >=
    1:10 FLOAT 3.5
    1:14 PUNCT {
    2:3 KEYWORD return
    2:10 STRING "hi"
    3:1 PUNCT }

Empty input prints nothing.
