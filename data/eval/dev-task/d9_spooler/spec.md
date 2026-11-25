# Printer spooler

Simulate a print spooler with job priorities and a single printer.

## Input (standard input)

One command per line, words separated by spaces (extra spaces and surrounding whitespace are ignored). Lines that are empty or start with `#` are skipped silently but still count for line numbers (line numbers are 1-based). Commands:

- `submit ID PRIORITY PAGES`: queue a job. `ID` is any word. `PRIORITY` is a whole number 1 to 9 (9 is most urgent). `PAGES` is a whole number of at least 1.
- `cancel ID`
- `tick`
- `status`

A number is valid only if it consists of decimal digits only (so `-3`, `+3` and `abc` are not numbers).

## Rules

The printer prints one job at a time and never interrupts it: once a job has started it keeps the printer until it finishes or is cancelled. Jobs waiting in the queue are served by priority, highest number first; jobs of equal priority are served in the order they were submitted.

Every job ID that was ever accepted is remembered, even after the job finished or was cancelled.

`submit` is checked in this order, and the first failing check reports the error: wrong number of words, bad priority, bad pages, duplicate ID (the ID was ever accepted before). A rejected submit changes nothing.

`cancel ID`: if the ID is the job currently printing, it is removed from the printer (its printed pages are lost) and `cancelled ID (printing)` is printed; else if it is waiting in the queue, it is removed and `cancelled ID` is printed; else if the ID was ever accepted (finished or already cancelled) it is an error `job ID not active`; otherwise the error is `unknown job ID`.

`tick` gives the printer 10 pages of capacity. Repeat while capacity remains: if the printer is empty, take the best waiting job (if none is waiting, stop); print `  start ID` (two leading spaces) when a job is taken; the printer prints `min(capacity left, pages left of the job)` pages of it; if the job has no pages left print `  done ID` (two leading spaces), count it as finished and leave the printer empty. A job that is finished exactly when capacity runs out is done in that same tick, and the next job is only started by a later tick. After the loop print `tick: N pages` where N is the number of pages printed during this tick.

`status` prints three lines:

```
printing: ID (K left)        or   printing: none
queued: ID:PRIORITY:PAGES ID:PRIORITY:PAGES ...   or   queued: none
finished F cancelled C
```

The queued jobs are listed in the order they would be served, with their remaining pages (which are the original pages for waiting jobs). F is the number of jobs that completed and C the number of successful cancels so far.

## Errors

An error prints a line `error line N: MESSAGE` (N is the input line number) and the command is otherwise ignored. Messages: `unknown command` (first word is not one of the four commands), `bad arguments` (wrong number of words for the command: `submit` needs 4 words, `cancel` 2, `tick` and `status` 1), `bad priority`, `bad pages`, `duplicate job ID`, `job ID not active`, `unknown job ID`, where ID is the job ID from the command.

## Output

All lines described above in input order. After the last line of input print:

```
summary: finished F cancelled C pending P
```

where P is the number of jobs waiting in the queue plus the job on the printer, if any.

## Example

Input:

```
submit report 3 14
submit memo 5 4
submit photo 3 8
status
tick
status
submit urgent 9 3
tick
tick
status
tick
```

Output:

```
printing: none
queued: memo:5:4 report:3:14 photo:3:8
finished 0 cancelled 0
  start memo
  done memo
  start report
tick: 10 pages
printing: report (8 left)
queued: photo:3:8
finished 1 cancelled 0
  done report
  start urgent
tick: 10 pages
  done urgent
  start photo
  done photo
tick: 9 pages
printing: none
queued: none
finished 4 cancelled 0
tick: 0 pages
summary: finished 4 cancelled 0 pending 0
```
