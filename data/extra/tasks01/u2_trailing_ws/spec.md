# Trailing-whitespace report

Report the lines of standard input that end in spaces or tabs.

For each such line (numbered from 1) print `N: C KIND`, where C is the number of trailing space and tab
characters and KIND is `spaces` if they are all spaces, `tabs` if they are all tabs, and `mixed` otherwise.
If the whole line consists only of whitespace (and is not empty) append ` (blank)` to the output line.
After the list print `flagged=F of T lines`, where F is the number of reported lines and T the number of lines
in the input. If no line is reported print only `clean`.

Edge cases: empty input has no lines and prints `clean`. Other whitespace characters (such as form feed)
are not considered.

Example input (a tab is written as <T>, a space as _):
ok
x__
y_<T>
<T><T>

Example output:
2: 2 spaces
3: 2 mixed
4: 2 tabs (blank)
flagged=3 of 4 lines
