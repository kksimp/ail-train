# Longest repeated word sequence

Words are the whitespace-separated tokens of the whole input, lower-cased (ASCII); punctuation stays attached
to the token. A sequence is L consecutive words. Find the largest L for which some sequence of L words occurs
at two or more different start positions (occurrences may overlap).

Print three lines: `length=L`, `text=WORDS` (the sequence, words joined by single spaces) and `starts=P1,P2,...`
(all 1-based start positions of that sequence in increasing order). If several different sequences share the largest
length, choose the one whose first occurrence starts earliest.

If no word occurs twice (this includes empty input) print only `none`.

Example input:
a b c x a b c y b c

Example output:
length=3
text=a b c
starts=1,5
