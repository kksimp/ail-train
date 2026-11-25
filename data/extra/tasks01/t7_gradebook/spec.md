Read grade records from standard input, one per line: `name,score,score,...` with at least one score. Blank lines are
ignored. The name (trimmed) must be non-empty and every score (trimmed) an integer from 0 to 100; otherwise print
`line N: invalid` (N is the 1-based line number, blank lines counted) and skip the line.

For a valid record with n scores: if n >= 4 the single lowest score is dropped (one copy only). The average in tenths
is round-half-up of sum/n times 10, computed as (sum * 20 + n) / (2 * n) with integer division, where sum and n are
taken after any drop. Letter grade from that value in tenths: >= 900 A, >= 800 B, >= 700 C, >= 600 D, otherwise F.

After all lines print the valid students sorted by average descending, ties by name ascending (byte order; equal names
keep input order), each as `NAME: avg=X.Y grade=L` (for example 875 tenths is `87.5`). Then print one line
`grades: A=a B=b C=c D=d F=f` with the counts. The invalid-line messages are printed first, as the lines are read.

Example input:
    ann,90,80,70
    bob,100,95,95,50
Output:
    bob: avg=96.7 grade=A
    ann: avg=80.0 grade=B
    grades: A=1 B=1 C=0 D=0 F=0

Empty input prints only `grades: A=0 B=0 C=0 D=0 F=0`.
