def compare(older, newer, with_new):
    out = []
    for p in sorted(set(older) | set(newer)):
        a = older.get(p)
        b = newer.get(p)
        if a is None and with_new:
            out.append(f"new file:  {p}")
        elif a is not None and b is None:
            out.append(f"deleted:   {p}")
        elif a is not None and b is not None and a != b:
            out.append(f"modified:  {p}")
    return out

def section(title, items):
    if not items:
        return
    print(f"{title}:")
    for it in items:
        print(f"    {it}")

head = {"README": 11, "main.c": 20, "util.c": 30, "old.txt": 40}
index = {"README": 11, "main.c": 21, "util.c": 30, "notes.md": 50}
work = {"README": 12, "main.c": 21, "notes.md": 50, "scratch.log": 60, "todo.txt": 70}
staged = compare(head, index, True)
unstaged = compare(index, work, False)
untracked = [p for p in sorted(work) if p not in index]
section("changes to be committed", staged)
section("changes not staged", unstaged)
section("untracked files", untracked)
print(f"{len(staged)} staged, {len(unstaged)} unstaged, {len(untracked)} untracked")
