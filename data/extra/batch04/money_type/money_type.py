I = [("bread", 245), ("cheese", 615), ("apples", 320), ("tea", 399)]
def s(c): return ("-" if c < 0 else "") + f"{abs(c) // 100}.{abs(c) % 100:02d}"
t = 0
for n, c in I: t += c; print(f"{n:<7} {s(c)}")
print(f"total   {s(t)}")
print(f"change  {s(2000 - t)}")
print(f"short   {s(1000 - t)}")
print(f"dearest {max(I, key=lambda i: i[1])[0]}")
