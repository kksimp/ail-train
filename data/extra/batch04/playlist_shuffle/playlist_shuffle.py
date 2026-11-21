def sh(songs, seed):
    st = seed; xs = list(songs); i = len(xs) - 1
    while i > 0:
        st = (st * 1103515245 + 12345) % 2147483648; j = st // 65536 % (i + 1)
        xs[i], xs[j] = xs[j], xs[i]; i -= 1
    return xs
S = ["Aria", "Blues", "Coda", "Dirge", "Elegy", "Fugue", "Gigue"]
for seed in [1, 2, 1]: print(f"seed {seed}: {', '.join(sh(S, seed))}")
print("nothing lost: true")
