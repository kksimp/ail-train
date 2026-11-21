def dep(first, every, gf, gt):
    t = first
    while t < 1440:
        if t < gf or t >= gt: yield t
        t += every
c = lambda m: f"{m // 60:02}:{m % 60:02}"
d = list(dep(370, 20, 600, 660))
print(f"first trains: {' '.join(c(t) for t in d[:5])}")
print(f"after 09:45: {' '.join(c(t) for t in [t for t in d if t >= 585][:3])}")
print(f"trains before noon: {sum(1 for t in d if t < 720)}")
print(f"{len(d)} trains a day, last at {c(d[-1])}")
