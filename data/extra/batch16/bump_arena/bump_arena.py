class Arena:
    def __init__(s, cap):
        s.cap, s.top, s.marks, s.padding = cap, 0, [], 0
    def alloc(s, size, align):
        start = (s.top + align - 1) // align * align
        if start + size > s.cap:
            return None, f"no room for {size} bytes at {start}"
        s.padding += start - s.top
        s.top = start + size
        return start, ""

def take(a, name, size, align):
    off, err = a.alloc(size, align)
    if off is not None:
        print(f"{name:<6} {size:>2} bytes align {align} -> offset {off:>2}, top {a.top}")
    else:
        print(f"{name:<6} failed: {err}")

a = Arena(64)
take(a, "header", 6, 1)
take(a, "vec", 16, 8)
a.marks.append(a.top)
print(f"mark at {a.top}")
take(a, "name", 5, 1)
take(a, "tmp", 12, 4)
take(a, "big", 24, 8)
a.top = a.marks.pop()
print(f"reset to {a.top}")
take(a, "big", 24, 8)
take(a, "tail", 10, 2)
take(a, "last", 8, 8)
print(f"bytes used {a.top} of {a.cap}, padding added {a.padding}")
