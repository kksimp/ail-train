def ver(s):
    p = s.split(".")
    return int(p[0]) * 10000 + int(p[1]) * 100 + int(p[2])

def in_range(v, rng):
    for part in rng.split(" "):
        if part.startswith(">="):
            if v < ver(part[2:]):
                return False
        elif part.startswith("<"):
            if v >= ver(part[1:]):
                return False
    return True

manifest = {"serde": ">=1.0.0 <2.0.0", "tokio": ">=1.20.0 <1.30.0", "rand": ">=0.8.0 <0.9.0", "clap": ">=4.0.0 <5.0.0", "regex": ">=1.5.0 <2.0.0"}
lock = {"serde": "1.0.188", "tokio": "1.32.0", "rand": "0.8.5", "regex": "1.4.9", "once": "1.18.0"}
problems = 0
for name, rng in manifest.items():
    if name in lock:
        pinned = lock[name]
        ok = in_range(ver(pinned), rng)
        if not ok:
            problems += 1
        verdict = "ok" if ok else "OUTSIDE range"
        print(f"{name:<6} {pinned:<8} {rng:<17} {verdict}")
    else:
        problems += 1
        print(f"{name:<6} {rng} has no locked version")
for name, pinned in lock.items():
    if name not in manifest:
        problems += 1
        print(f"{name:<6} {pinned} is locked but no longer wanted")
print(f"{problems} problems; run the resolver again")
