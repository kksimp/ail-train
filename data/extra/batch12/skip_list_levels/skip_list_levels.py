def search(lanes, want):
    steps = 0
    cur = -1
    lvl = len(lanes) - 1
    while lvl >= 0:
        lane = lanes[lvl]
        i = 0
        if cur >= 0:
            i = lane.index(cur) if cur in lane else 0
            i += 1
        while i < len(lane) and lane[i] <= want:
            cur = lane[i]
            steps += 1
            i += 1
        lvl -= 1
    found = 1 if cur == want else 0
    return [found, steps]

keys = [3, 8, 12, 17, 21, 26, 30, 34, 41, 47, 52, 58, 63, 69, 75, 80]
seed = 99
levels = []
for k in keys:
    lv = 1
    seed = (seed * 1103515245 + 12345) % 2147483648
    bits = seed >> 16
    while (bits & 1) == 1 and lv < 4:
        lv += 1
        bits >>= 1
    levels.append(lv)
lanes = []
for l in range(4):
    lanes.append([keys[i] for i in range(len(keys)) if levels[i] > l])
l = 3
while l >= 0:
    print(f"lane {l}: {lanes[l]}")
    l -= 1
for want in [47, 8, 80, 50]:
    r = search(lanes, want)
    verdict = "found" if r[0] == 1 else "absent"
    print(f"find {want}: {verdict} after {r[1]} hops (a plain list scan takes up to {len(keys)})")
