# Line numbering with blank-line rules

Standard input is a text file. Number its lines as follows.
- Leading blank lines are dropped. A blank line is one that is empty or holds only spaces and tabs.
- A non-blank line is printed as its number right-aligned in 4 columns, two spaces, and the original line text
  (kept exactly, including trailing spaces). Numbers count only the non-blank lines, starting at 1.
- A run of one or more blank lines between non-blank lines is printed as a single empty line, which gets no number.
- Trailing blank lines are dropped.
After the lines print `-- N numbered lines`, where N is the number of numbered lines (also when N is 0).

Example input:
alpha


beta
gamma


Example output:
   1  alpha

   2  beta
   3  gamma
-- 3 numbered lines
