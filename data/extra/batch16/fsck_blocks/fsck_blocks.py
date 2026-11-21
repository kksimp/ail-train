inodes = {1: [2, 3, 4], 2: [5, 6, 4], 3: [10, 11], 4: [], 5: [14, 15, 16]}
marked = [0, 1, 2, 3, 5, 6, 10, 12, 13, 14, 15, 16]
reserved = [0, 1]
owner = {}
problems = 0
for ino, blocks in inodes.items():
    for b in blocks:
        if b in owner:
            print(f"block {b:>2}: claimed by inode {owner[b]} and inode {ino} (needs a copy)")
            problems += 1
        else:
            owner[b] = ino
fixed = list(marked)
for b in sorted(owner):
    if b not in marked:
        print(f"block {b:>2}: owned by inode {owner[b]} but marked free, marking used")
        fixed.append(b)
        problems += 1
for b in marked:
    if b not in owner and b not in reserved:
        print(f"block {b:>2}: marked used but owned by no inode, freeing")
        fixed = [x for x in fixed if x != b]
        problems += 1
print(f"{problems} problems; bitmap now {sorted(fixed)}")
