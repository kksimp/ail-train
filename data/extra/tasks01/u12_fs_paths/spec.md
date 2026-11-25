# In-memory file system

Run shell-like commands on an in-memory directory tree. It starts with only the root directory `/`, and the current directory is `/`.

Input: one command per line; blank lines are ignored; surrounding whitespace is trimmed; words are separated by whitespace.
Paths start with `/` (absolute) or are relative to the current directory. They are resolved lexically: empty and `.` parts are
dropped and `..` removes the previous part (at the root it stays at the root). The result is then looked up in the tree.

Commands:
- `mkdir PATH`: create a directory. Parent must be an existing directory, else print `mkdir: no such directory`. If PATH already exists (file or directory), print `mkdir: exists`.
- `touch PATH`: create an empty file. Parent missing: `touch: no such directory`. If PATH is an existing directory: `touch: is a directory`. An existing file is fine (no output).
- `cd PATH`: change directory. If PATH is not an existing directory print `cd: no such directory`.
- `pwd`: print the current directory path (`/` or `/a/b`, no trailing slash).
- `ls` or `ls PATH`: list the directory (default: current). Print its entries sorted by name (byte order), separated by single spaces, directories with a trailing `/`; an empty directory prints `(empty)`. If PATH is a file print its base name. If missing print `ls: no such file or directory`.
A command with the wrong word count for its name, or an unknown command, prints `? ` followed by the trimmed line. `mkdir`, `touch`, `cd` need exactly one path.
Successful `mkdir`, `touch`, `cd` print nothing.

Example input:
    mkdir a
    mkdir a/b
    touch a/f.txt
    cd a
    pwd
    ls
    ls ..
    cd ../zzz
Output:
    /a
    b/ f.txt
    a/
    cd: no such directory
