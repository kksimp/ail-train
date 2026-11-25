# text buffer with undo and redo

Read commands from standard input, one per line, and edit a text buffer that starts empty. Blank lines are ignored.

Commands:
- `append TEXT`: TEXT is everything after the first space (it must not be empty, and may contain spaces); add it to the end of the buffer.
- `delete N`: remove the last N characters (N is an integer of at least 1). If N is larger than the buffer length, the whole buffer is removed.
- `undo`: restore the buffer from before the most recent edit that was not undone.
- `redo`: re-apply the most recently undone edit.
- `show`: print the buffer between square brackets, e.g. `[hello]`.

Every `append` and `delete` is an edit. A new edit discards everything that could be redone. `undo` and `redo` are not edits.

Errors print `error: MESSAGE` and change nothing: `nothing to undo`, `nothing to redo`, `bad command` (unknown command, `append` with no text, `delete` with a missing or invalid N, or extra words on `undo`, `redo`, `show`).

At the end of input print `edits: E` where E is the number of undoable edits currently applied (the undo history length).

Example:
```
append hello
append  world
show
undo
show
redo
delete 3
show
```
prints (the second append adds a leading space, since TEXT starts after the first space only)
```
[hello world]
[hello]
[hello wo]
edits: 3
```
