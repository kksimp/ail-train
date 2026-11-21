dir_ = {}
inodes = {}
next_ino = 1
ops = [["create", "a"], ["link", "a", "b"], ["open", "a"], ["unlink", "a"], ["unlink", "b"], ["create", "c"], ["close", "b"], ["link", "c", "d"], ["unlink", "c"]]
handles = {}
for op in ops:
    if op[0] == "create":
        ino = next_ino
        next_ino += 1
        inodes[ino] = [1, 0]
        dir_[op[1]] = ino
    elif op[0] == "link":
        ino = dir_[op[1]]
        dir_[op[2]] = ino
        inodes[ino][0] += 1
    elif op[0] == "open":
        ino = dir_[op[1]]
        handles[op[1]] = ino
        inodes[ino][1] += 1
    elif op[0] == "close":
        ino = list(handles.values())[0]
        inodes[ino][1] -= 1
    else:
        ino = dir_[op[1]]
        del dir_[op[1]]
        inodes[ino][0] -= 1
    node = list(inodes[ino])
    note = ""
    if node[0] == 0 and node[1] == 0:
        del inodes[ino]
        note = ", data freed"
    elif node[0] == 0:
        note = ", nameless but open"
    words = " ".join(op)
    print(f"{words:<12} inode {ino}: links {node[0]} opens {node[1]}{note}")
print(f"names left: {' '.join(sorted(dir_))}; inodes in use: {len(inodes)}")
