print("dec      bin hex ones")
t = 0
for n in range(21):
    t += bin(n).count("1"); print(f"{n:>3} {n:>8b} {n:>3x} {bin(n).count('1'):>4}")
print(f"one bits in 0..20: {t}")
