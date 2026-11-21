def pl(n, u): return f"1 {u}" if n == 1 else f"{n} {u}s"
def ds(s):
    if s == 0: return "now"
    parts = []
    for name, size in [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]:
        n, s = divmod(s, size)
        if n: parts.append(pl(n, name))
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]
for s in [0, 1, 59, 60, 62, 3600, 3661, 7501, 86400, 90061, 1000000]: print(f"{s:>7}: {ds(s)}")
