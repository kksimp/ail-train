ORDER = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s"]

def capacity(sub):
    return {"s": 2, "p": 6, "d": 10}.get(sub[1:], 14)

def configure(z):
    left = z
    out = []
    for sub in ORDER:
        if left == 0:
            break
        n = min(left, capacity(sub))
        out.append((sub, n))
        left -= n
    return out

def unpaired(cfg):
    total = 0
    for sub, e in cfg:
        orbitals = capacity(sub) // 2
        total += e if e <= orbitals else 2 * orbitals - e
    return total

for sym, z in [("H", 1), ("C", 6), ("O", 8), ("Na", 11), ("P", 15), ("Fe", 26), ("Br", 35), ("Kr", 36), ("Sn", 50), ("Nd", 60)]:
    cfg = configure(z)
    text = " ".join(f"{c[0]}{c[1]}" for c in cfg)
    print(f"{sym:<2} ({z:>2}): {text}  unpaired {unpaired(cfg)}")
