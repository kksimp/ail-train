def bits(v, width):
    return "".join(str((v >> (width - 1 - i)) & 1) for i in range(width))
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
cases = [[1, 2, 3, 3], [2, 2, 2, 3, 3], [1, 2, 2, 3], [2, 3, 3, 3, 3, 4, 4], [3, 3, 3, 3, 3, 3, 3, 3]]
for lens in cases:
    top = max(lens)
    used = sum(1 << (top - l) for l in lens)
    room = 1 << top
    if used > room:
        print(f"lengths {fl(lens)}: sum = {used}/{room} > 1, no prefix code exists")
        continue
    sl = sorted(lens)
    code = 0
    prev = sl[0]
    words = []
    for i, l in enumerate(sl):
        if i > 0:
            code = (code + 1) << (l - prev)
        words.append(bits(code, l))
        prev = l
    pf = all(not (a != b and b.startswith(a)) for a in words for b in words)
    note = "complete" if used == room else "spare room"
    print(f"lengths {fl(lens)}: sum = {used}/{room} ({note}), code {' '.join(words)}, prefix-free {'true' if pf else 'false'}")
