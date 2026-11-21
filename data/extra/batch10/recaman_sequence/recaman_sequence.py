def recaman(count):
    seq = [0]
    seen = {0}
    for n in range(1, count):
        prev = seq[n - 1]
        back = prev - n
        v = back if back > 0 and back not in seen else prev + n
        seq.append(v)
        seen.add(v)
    return seq

seq = recaman(2000)
print(f"first 20: {seq[:20]}")
first_at = {}
repeats = []
for i, v in enumerate(seq):
    if v in first_at:
        if len(repeats) < 4:
            repeats.append(f"{v} at steps {first_at[v]} and {i}")
    else:
        first_at[v] = i
for r in repeats:
    print(f"repeat: {r}")
missing = 1
while missing in first_at:
    missing += 1
print(f"distinct values in 2000 steps: {len(first_at)}, smallest not yet reached: {missing}")
print(f"largest value so far: {max(seq)}")
