def van_eck(count):
    seq = [0]
    last = {}
    for n in range(count - 1):
        v = seq[n]
        if v in last:
            seq.append(n - last[v])
        else:
            seq.append(0)
        last[v] = n
    return seq

seq = van_eck(1000)
print(f"first 25: {seq[:25]}")
print(f"zeros in the first 1000 terms: {seq.count(0)}")
print(f"largest of the first 1000: {max(seq)}")
for target in [5, 10, 20, 50]:
    idx = seq.index(target) if target in seq else -1
    print(f"{target} first appears at position {idx}")
