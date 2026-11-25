# Sessions by idle timeout

Standard input starts with a header line `timeout N` (N digits only), then event lines `TS USER`: TS is digits only
(seconds), USER is a non-empty word, one space between them. Events may appear in any order. A line that is not a valid
event is skipped and counted; empty lines are ignored.

For each user, sort the user's timestamps ascending. Consecutive timestamps belong to the same session when their gap
is at most N; a larger gap starts a new session. Print one line per session, users in ascending byte order and each
user's sessions in time order:

`USER START END COUNT`

where START and END are the first and last timestamp of the session and COUNT the number of events in it. After all
sessions print `skipped: K`.

If the first non-empty line is not a valid header (or the input is empty), print only `error: bad header`.

Example input:
```
timeout 30
100 bob
10 ann
50 ann
60 ann
200 bob
oops
```
Output:
```
ann 10 10 1
ann 50 60 2
bob 100 100 1
bob 200 200 1
skipped: 1
```
