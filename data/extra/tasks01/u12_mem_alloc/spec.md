# Memory allocator

Simulate a contiguous memory allocator with first-fit or best-fit placement.

Input, first non-blank line: `memory SIZE strategy S` where SIZE >= 1 and S is `first` or `best`. If it does not fit this form,
print `bad header` and stop. Memory is the address range 0..SIZE-1 and starts as one free hole.
Each later non-blank line is a command:
- `alloc NAME N` (N >= 1): place a block of N units in a hole. First-fit takes the lowest-address hole with at least N units; best-fit takes
  the smallest such hole (lowest address on ties). The block goes at the start of the hole; any leftover stays a hole.
  Print `alloc NAME N -> ADDR`. If no hole fits print `alloc NAME N -> fail`. If NAME is already allocated print `alloc NAME N -> exists`.
- `free NAME`: release the block; adjacent holes merge. Print `free NAME -> ok`, or `free NAME -> unknown` if no such block.
- anything else: print `? LINE` with the line trimmed.

After the commands print `layout` and one line per region in address order, `START-END NAME` (END inclusive, `free` for holes),
then `largest free=L` (0 if there are no holes).

Example input:
    memory 100 strategy first
    alloc A 30
    alloc B 50
    free A
    alloc C 40
Output:
    alloc A 30 -> 0
    alloc B 50 -> 30
    free A -> ok
    alloc C 40 -> fail
    layout
    0-29 free
    30-79 B
    80-99 free
    largest free=30
