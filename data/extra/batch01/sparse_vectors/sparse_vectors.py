a = {3: 2, 1000: -4, 77: 5}
b = {i: x for i, x in enumerate([0, 0, 0, 7, 0, 1]) if x}
c = {1000: 4, 5: 3}
show = lambda v: " ".join(f"{i}:{v[i]}" for i in sorted(v))
dot = lambda p, q: sum(x * q.get(i, 0) for i, x in p.items())
print(f"a = {show(a)}")
print(f"b = {show(b)}")
print(f"a.b = {dot(a, b)}, a.c = {dot(a, c)}")
s = dict(a)
for i, x in c.items():
    s[i] = s.get(i, 0) + x
    if s[i] == 0: del s[i]
print(f"a+c = {show(s)} ({len(s)} stored)")
