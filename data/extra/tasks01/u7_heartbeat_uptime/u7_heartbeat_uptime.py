import sys


def digits(s):
    return s.isascii() and s.isdigit()


def main():
    lines = [l for l in sys.stdin.read().splitlines() if l != ""]
    h = lines[0].split(" ") if lines else []
    if len(h) != 2 or h[0] != "interval" or not digits(h[1]) or int(h[1]) < 1:
        print("error: bad header")
        return
    gap = int(h[1])
    beats = []
    end = None
    bad = 0
    for line in lines[1:]:
        f = line.split(" ")
        if len(f) != 2 or f[0] not in ("beat", "end") or not digits(f[1]):
            bad += 1
            continue
        t = int(f[1])
        if f[0] == "beat":
            if end is not None or (beats and t <= beats[-1]):
                bad += 1
                continue
            beats.append(t)
        else:
            if end is not None or not beats or t < beats[-1]:
                bad += 1
                continue
            end = t
    print(f"beats: {len(beats)}")
    if beats:
        periods = []
        for a, b in zip(beats, beats[1:]):
            if b - a > gap:
                periods.append((a + gap, b))
        if end is not None and end - beats[-1] > gap:
            periods.append((beats[-1] + gap, end))
        down = 0
        for s, e in periods:
            print(f"down {s} {e}")
            down += e - s
        last = end if end is not None else beats[-1]
        obs = last - beats[0]
        pct = 100 if obs == 0 else (obs - down) * 100 // obs
        print(f"downtime: {down}")
        print(f"observed: {obs}")
        print(f"uptime: {pct}%")
    print(f"malformed: {bad}")


main()
