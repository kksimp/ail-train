rows = [("alpha", 1234567, 0.5), ("beta", 42, 12.347), ("gamma", 0, 100.0)]
print(f"{'name':<8}|{'count':>9}|{'ratio':>7}|{'hex':>6}")
for name, count, ratio in rows:
    print(f"{name:<8}|{count:>9,}|{ratio:>7.2f}|{count:>6x}")
n = 37
print(f"[{n:5}] [{n:<5}] [{n:^5}] [{n:05}] [{n:+}]")
print(f"[{n:b}] [{n:x}] [{n:08b}]")
s = "ail"
print(f"[{s:>6}] [{s:*^9}] [{s:-<6}] [{s:0>6}]")
x = 3.14159
print(f"[{x:.0f}] [{x:.2f}] [{x:8.3f}] [{x:<8.1f}]")
print(f"{1000000:,} {999:,} {-1234:,}")
print(f"order-{7:04}")
