class Local:
    def __init__(s, name, size, align):
        s.name, s.size, s.align = name, size, align

def round_up(n, a):
    return (n + a - 1) // a * a

def layout(locals_, show):
    off = 0
    parts = []
    for l in locals_:
        off = round_up(off, l.align)
        parts.append(f"{l.name}@{off}")
        off += l.size
    if show:
        print("  " + " ".join(parts))
    return round_up(off, 16)

locals_ = [Local("flag", 1, 1), Local("count", 4, 4), Local("ptr", 8, 8), Local("ch", 2, 2), Local("total", 8, 8), Local("ok", 1, 1), Local("buf", 12, 4), Local("id", 4, 4)]
raw = sum(l.size for l in locals_)
print("declaration order:")
a = layout(locals_, True)
print(f"  frame {a} bytes, padding {a - raw}")
sorted_locals = sorted(locals_, key=lambda l: -l.align)
print("largest alignment first:")
b = layout(sorted_locals, True)
print(f"  frame {b} bytes, padding {b - raw}")
print(f"data bytes {raw}, saved {a - b}")
