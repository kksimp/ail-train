def home(s):
    h = 0
    for c in s:
        h = (h * 37 + ord(c)) % 10007
    return h % 13

def place(keys, robin):
    slots = [""] * 13
    for key in keys:
        k = key
        pos = home(k)
        dist = 0
        while slots[pos] != "":
            other = slots[pos]
            od = (pos - home(other) + 13) % 13
            if robin and od < dist:
                slots[pos] = k
                k = other
                dist = od
            pos = (pos + 1) % 13
            dist += 1
        slots[pos] = k
    return slots

def dists(slots):
    return [(i - home(slots[i]) + 13) % 13 for i in range(13) if slots[i] != ""]

keys = ["oak", "elm", "ash", "fir", "yew", "box", "bay", "fig", "lime", "pine"]
for k in keys:
    print(f"{k:<5} home {home(k):>2}")
for robin in [False, True]:
    d = dists(place(keys, robin))
    name = "robin hood" if robin else "linear"
    print(f"{name:<10}: probe lengths {d}, longest {max(d)}, total {sum(d)}")
