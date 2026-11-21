eps = {0: [1, 7], 1: [2, 4], 3: [6], 5: [6], 6: [1, 7]}
moves = {"2a": 3, "4b": 5, "7a": 8, "8b": 9, "9b": 10}

def closure(states):
    out = set(states)
    stack = list(states)
    while stack:
        s = stack.pop()
        for t in eps.get(s, []):
            if t not in out:
                out.add(t)
                stack.append(t)
    return out

def step(states, ch):
    out = set()
    for s in states:
        key = f"{s}{ch}"
        if key in moves:
            out.add(moves[key])
    return out

def accepts(word, show):
    cur = closure({0})
    for ch in word:
        cur = closure(step(cur, ch))
        if show:
            print(f"  after {ch}: {sorted(cur)}")
    return 10 in cur

print(f"start: {sorted(closure({0}))}")
accepts("babb", True)
for w in ["abb", "aabb", "babb", "abab", "ab", "bbbabb", ""]:
    verdict = "accept" if accepts(w, False) else "reject"
    print(f"'{w}' {verdict}")
