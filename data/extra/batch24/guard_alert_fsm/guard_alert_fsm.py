def react(w, noise):
    kind, left = w
    if kind == "calm": return ("suspicious", 3) if noise >= 2 else ("calm", 0)
    if kind == "suspicious":
        if noise >= 2: return ("alert", 4)
        if left <= 1: return ("calm", 0)
        return ("suspicious", left - 1)
    if kind == "alert":
        if noise >= 1: return ("alert", 4)
        if left <= 1: return ("searching", 5)
        return ("alert", left - 1)
    if noise >= 1: return ("alert", 4)
    if left <= 1: return ("calm", 0)
    return ("searching", left - 1)
noise = [0, 1, 2, 0, 0, 0, 2, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
w = ("calm", 0)
seconds = {}
for t, n in enumerate(noise):
    before = w[0]
    w = react(w, n)
    after = w[0]
    seconds[after] = seconds.get(after, 0) + 1
    if after != before:
        print(f"second {t:>2}: noise {n}, {before} -> {after}")
for name, s in seconds.items():
    print(f"{name}: {s} s")
