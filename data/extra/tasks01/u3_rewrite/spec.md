# rewrite: a string rewriting system

Line 1 of stdin is N, the maximum number of steps (digits only, 0 to 40). Line 2 is the start string (it may be
empty; spaces are ordinary characters). Every later line is a rule `LHS=>RHS`, split at the first `=>` (LHS must be
non-empty; RHS may be empty and may contain `=>`; nothing is trimmed). Empty lines after line 2 are skipped but
count for line numbers. If line 1 is missing or not valid, or there is no line 2, print only `bad input`.
A rule line without `=>` or with an empty LHS makes the program print only `bad rule line K` (K is the 1-based
line number of the first such line).

One step: take the first rule, in input order, whose LHS occurs in the current string, and replace the leftmost
occurrence of its LHS by its RHS (once). Print `0: [START]`, then after each step `K: [STRING]` (K = step number).
Stop when no rule applies or when N steps have been done. If a step would make the string longer than 60
characters, print `too long at step K` instead of that step's line and stop. The last line otherwise is
`halted after K steps` if no rule applies to the final string (K = steps done), else `step limit N reached`.

Example: N=5, start `ab`, rules `ab=>ba` and `ba=>ab` prints
```
0: [ab]
1: [ba]
2: [ab]
3: [ba]
4: [ab]
5: [ba]
step limit 5 reached
```
