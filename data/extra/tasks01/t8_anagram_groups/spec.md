# Anagram groups

Read words from standard input, one per line. Trim each line and convert it to lowercase; skip lines that are
empty after trimming. Words are ASCII.

Two words are anagrams when their letters, sorted, are equal. Collect the distinct (after lowercasing) words into
anagram groups. For every group that has at least 2 distinct words, print one line: the group's words in
ascending byte order, separated by single spaces. Print the group lines in ascending byte order of the whole line.

If no group has 2 or more distinct words (including empty input), print `none`.

Example input:
```
Listen
silent
enlist
google
Gogole
cat
tac
act
dog
LISTEN
```
Output:
```
act cat tac
enlist listen silent
gogole google
```
Repeated words (such as `LISTEN` above) count once.
