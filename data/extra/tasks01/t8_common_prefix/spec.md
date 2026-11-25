# Longest common prefix per group

Standard input holds groups of words. Each non-blank line is one word (trim surrounding spaces); one or more blank
lines separate groups. Several blank lines in a row count as one separator, and leading or trailing blank lines are
ignored.

For each group, numbered from 1, print `group N: "P"` where P is the longest common prefix of all words in the group
(compared character by character, case-sensitive). If P is empty, print `group N: ""`. A group with a single word
has that whole word as its prefix. After the groups, print `longest: N` where N is the length of the longest prefix
found, or `longest: 0` if there are no groups.

Example input:
```
flower
flow
flight

dog
racecar

solo
```
Output:
```
group 1: "fl"
group 2: ""
group 3: "solo"
longest: 4
```
Empty input prints just `longest: 0`.
