log = """$ cd /
$ ls
dir docs
dir games
1200 boot.cfg
$ cd docs
$ ls
dir old
2300 plan.txt
800 todo_notes.txt
$ cd old
$ ls
4100 draft.txt
$ cd ..
$ cd ..
$ cd games
$ ls
9800 chess.bin
3100 go.bin"""
trail = []; sizes = {}
for line in log.splitlines():
    w = line.split(" ")
    if line == "$ cd /":
        trail = ["root"]
    elif line == "$ cd ..":
        trail.pop()
    elif w[0] == "$" and w[1] == "cd":
        trail.append(w[2])
    elif w[0] != "$" and w[0] != "dir":
        n = int(w[0])
        for i in range(1, len(trail) + 1):
            key = "/".join(trail[:i])
            sizes[key] = sizes.get(key, 0) + n
for k, v in sizes.items():
    print(f"{k:<16} {v:>6}")
print(f"part 1: folders of at most 5000 sum to {sum(v for v in sizes.values() if v <= 5000)}")
need = 15000 - (30000 - sizes["root"])
print(f"part 2: need {need} more free, delete a folder of {min(v for v in sizes.values() if v >= need)}")
