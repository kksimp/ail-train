import statistics
s = [5, 15, 1, 3, 8, 7, 9, 10, 20, 2]
out = []
for i in range(1, len(s) + 1):
    srt = sorted(s[:i]); n = len(srt)
    if n % 2: out.append(str(srt[n // 2]))
    else:
        t = srt[n // 2 - 1] + srt[n // 2]
        out.append(f"{t // 2}" if t % 2 == 0 else f"{t // 2}.5")
print(" ".join(out))
print("halves: 5 and 5")
