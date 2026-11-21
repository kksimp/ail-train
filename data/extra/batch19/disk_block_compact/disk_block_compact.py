def expand(t):
    disk = []
    for i, ch in enumerate(t):
        disk += [i // 2 if i % 2 == 0 else -1] * int(ch)
    return disk

def checksum(disk):
    return sum(i * x for i, x in enumerate(disk) if x >= 0)

def by_blocks(disk):
    lo, hi = 0, len(disk) - 1
    while lo < hi:
        if disk[lo] >= 0: lo += 1
        elif disk[hi] < 0: hi -= 1
        else: disk[lo], disk[hi] = disk[hi], disk[lo]

def by_files(disk):
    top = max(disk)
    for fid in range(top, -1, -1):
        start = disk.index(fid)
        size = 0
        while start + size < len(disk) and disk[start + size] == fid:
            size += 1
        run = 0
        for i in range(start):
            run = run + 1 if disk[i] < 0 else 0
            if run == size:
                for k in range(size):
                    disk[i - size + 1 + k] = fid
                    disk[start + k] = -1
                break

def show(disk):
    return "".join("." if x < 0 else str(x) for x in disk)

dense = "1423521131442"
a = expand(dense)
print(f"layout:  {show(a)}")
b = list(a)
by_blocks(a)
print(f"blocks:  {show(a)}")
print(f"part 1: checksum {checksum(a)}")
by_files(b)
print(f"files:   {show(b)}")
print(f"part 2: checksum {checksum(b)}")
