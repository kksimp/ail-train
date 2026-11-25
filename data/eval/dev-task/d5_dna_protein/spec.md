# d5_dna_protein

Write a command-line program that translates DNA reads into protein sequences using a codon table supplied in the input.

## Input

The input has two parts separated by a line that is exactly `---` after removing leading and trailing whitespace. All lines are trimmed of leading and trailing whitespace before use.

1. Table part: lines of the form `XYZ=A`: exactly three characters from `A`, `C`, `G`, `T`, then `=`, then one character that is an upper-case ASCII letter or `*` (`*` means stop). Such a line maps that codon to that character. If a codon appears twice, the later line wins. Any table line not of this form (including blank lines) is ignored. The table need not be complete.
2. Read part: every line after the first `---` line. Blank lines are ignored; every other line is one read, numbered K = 1, 2, 3, ... counting only the non-blank read lines.

If there is no `---` line at all, print exactly `error: missing separator` and nothing else. Later `---` lines (if any) are ordinary read lines (and so invalid reads).

## Rules

For each read:

1. If it contains any character other than `A`, `C`, `G`, `T` it is invalid.
2. Otherwise find the leftmost occurrence of `ATG`. If there is none the read has no start.
3. Otherwise translate from that position: take successive non-overlapping three-letter codons, looking each up in the table. Stop at the first of these:
   - the codon maps to `*`: the end is `stop` (the stop is not part of the protein);
   - the codon is not in the table: the end is `unknown:CODON` (that codon text);
   - fewer than three letters remain: the end is `open` (this also applies when the read ends exactly after a full codon without a stop).
   Every other codon contributes its one-letter amino acid to the protein, in order. Note that `ATG` itself is looked up like any other codon (so with no `ATG` entry the end is `unknown:ATG` and the protein is empty).

## Output

One line per read:

- invalid: `K invalid`
- no start: `K no start`
- otherwise: `K protein=P len=L end=E` where P is the protein string (possibly empty), L its length, E the end described above.

## Example

Input:

```
ATG=M
TTT=F
GGC=G
AAA=K
TAA=*
---
CCATGTTTGGCAAATAAGG
ATGTTTGGCA

ACGTCC
ATGTTTCCCAAA
ATGXAT
```

Output:

```
1 protein=MFGK len=4 end=stop
2 protein=MFG len=3 end=open
3 no start
4 protein=MF len=2 end=unknown:CCC
5 invalid
```
