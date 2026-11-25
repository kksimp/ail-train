# URL query strings

Each non-blank input line is a relative URL of the form `PATH?QUERY#FRAGMENT`, where `?QUERY` and `#FRAGMENT` are each
optional; trim spaces from both ends of the line first. Cut the fragment off (everything from the first `#`), then split
the rest at the first `?` into PATH and QUERY (no `?` means no query).

For each URL print `path=PATH` (PATH as written), then one line `  KEY=VALUE` per parameter, in order, indented by two
spaces. QUERY is split at `&`; empty pieces are skipped; each piece is split at its first `=` into KEY and VALUE (no `=`
means an empty VALUE). KEY and VALUE are decoded: `+` becomes a space and `%XY` with two hex digits (either case) whose
value is below 128 becomes that ASCII character. Any other `%` (bad or too short, or value 128 and above) is kept
literally. Decoded text is not decoded again.
Blank lines (empty or only spaces) are skipped.

Example input:
    /search?q=hello+world&page=2&flag#top
    /plain
    /a/b?x=%41%2b%zz&&y==1

Example output:
    path=/search
      q=hello world
      page=2
      flag=
    path=/plain
    path=/a/b
      x=A+%zz
      y==1

Empty input prints nothing.
