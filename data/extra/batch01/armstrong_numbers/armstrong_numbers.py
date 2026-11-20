def arm(n):
    s = str(n)
    return sum(int(c) ** len(s) for c in s) == n
found = [n for n in range(1, 100000) if arm(n)]
print(", ".join(map(str, found)))
groups = {}
for n in found:
    groups.setdefault(len(str(n)), []).append(n)
for k, v in groups.items():
    print(f"{k} digits: {len(v)}")
print("true")
print("false")
