# Config validation

Read a config file from standard input and validate it. Each line is trimmed first. Blank lines and lines starting
with `#` are skipped (but still count for line numbers, which start at 1). Every other line is `key = value`, split at
the first `=`, with key and value trimmed.

Known keys and their valid values:
- `host`: non-empty, contains no spaces (it can contain anything else);
- `port`: digits only, value 1 to 65535;
- `workers`: digits only, value 1 to 64;
- `debug`: exactly `true` or `false`;
- `mode`: exactly `dev`, `test` or `prod`.

Check each line in order and report at most one problem per line (the first that applies):
- no `=` on the line: `line N: missing '='`
- empty key: `line N: empty key`
- key not known: `line N: unknown key 'KEY'`
- key already set by an earlier valid line: `line N: duplicate key 'KEY'`
- value not valid for the key: `line N: bad value for 'KEY': 'VALUE'`
A key counts as set only when its value was valid. After all lines, `host` and `port` are required: for each of them
(in that order) that was never set print `missing required key 'KEY'`. Finally print `ok` if nothing was reported,
otherwise `errors: N` where N is the number of problems printed.

Example input:
    # server
    host = example.org
    port = 70000
    debug = yes
    colour = red

Example output:
    line 3: bad value for 'port': '70000'
    line 4: bad value for 'debug': 'yes'
    line 5: unknown key 'colour'
    missing required key 'port'
    errors: 4

Empty input reports both required keys and `errors: 2`.
