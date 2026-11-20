pc = lambda n: bin(n).count("1")
print("".join(str(pc(n)) for n in range(16)))
for k in range(1, 5):
    print(f"{k} bits: " + " ".join(str(n) for n in [n for n in range(256) if pc(n) == k][:6]))
print(f"bits set in 0..1023: {sum(pc(n) for n in range(1024))}")
print(63)
