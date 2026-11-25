# De-duplicate lines, keeping the first

Read standard input as lines. The first line is an option line: `exact`, `nocase` or `trim`. Any other first line
(or empty input) makes the program print `bad option` and nothing else.

Process the remaining lines in order. Two lines are duplicates when their keys are equal, where the key is:

    exact    the line itself
    nocase   the line in lower case (ASCII)
    trim     the line with leading and trailing spaces/tabs removed

Print every line (as it appeared originally, unchanged) the first time its key is seen; skip later lines with a
key already seen. Empty lines are ordinary lines (the key of an empty line is empty).

After the lines, print a summary line `kept K of T, dropped D` where T is the number of data lines (excluding the
option line), K the number printed and D = T - K.

Example input:

    nocase
    Apple
    banana
    apple
    BANANA
    Cherry

Example output:

    Apple
    banana
    Cherry
    kept 3 of 5, dropped 2
