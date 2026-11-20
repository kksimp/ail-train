for n in [0, 7, 10, 255, 4096, 65535]:
    print(f"{n:>6} | {n:>5x} | {n:016b} | {oct(n)[2:]:>6}")
print(f"{1234567:,}")
print(f"{255:x} {48879:x}")
for text in ["ff", "7F", "zz", "1000"]:
    try:
        v = int(text, 16)
    except ValueError:
        print(f"{text}: not hex")
        continue
    print(f"{text} = {v}")
print(f"{48879:x}")
