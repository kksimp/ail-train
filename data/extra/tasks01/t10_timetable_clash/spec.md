Timetable clash finder

The program reads course meeting times and student enrolments and reports each student's timetable clashes.

Line kinds (blank lines are ignored):
- `meet COURSE DAY START END`: a weekly meeting. DAY is one of Mon Tue Wed Thu Fri; START and END are integers with
  START < END (periods; a meeting ending at 4 and one starting at 4 do not overlap). A course may have several meetings.
- `enrol STUDENT COURSE`: enrols a student; repeating the same pair has no further effect.
Any other line (wrong field count, unknown DAY, non-integer or out-of-order periods) prints `bad line N`
(1-based line number) as it is read, before everything else.

Then, for each enrolment in input order whose course has no meeting at all, print
`unknown course COURSE for STUDENT` (also when the enrolment comes before the meeting lines).

Then the clash report. Students are processed in byte order of name. For a student, take every pair of distinct enrolled
courses A < B (byte order) that have at least one overlapping pair of meetings on the same day. Print
`STUDENT: A clashes with B on DAY`, where DAY is the earliest weekday (Mon first) with an overlap for that pair.
Pairs are listed ordered by A, then B. Courses with no meetings are ignored here. Finally print `clashes N`, the number of lines printed
in the report.

Example input:
```
meet math Mon 1 3
meet math Wed 2 4
meet art Mon 2 4
meet bio Wed 3 5
meet bio Fri 1 2
enrol sam math
enrol sam art
enrol sam bio
enrol kim art
enrol kim chem
meet x Sun 1 2
```
Output:
```
bad line 12
unknown course chem for kim
sam: art clashes with math on Mon
sam: bio clashes with math on Wed
clashes 2
```
