B = {560, 600, 620, 680, 740}; F = [t for t in range(540, 780, 20) if t not in B]
h = lambda m: f"{m // 60:02}:{m % 60:02}"; print("free: " + " ".join(h(m) for m in F))
bs = bl = 0; i = 0
while i < len(F):
    j = i
    while j + 1 < len(F) and F[j + 1] == F[j] + 20: j += 1
    if j - i + 1 > bl: bl = j - i + 1; bs = F[i]
    i = j + 1
print(f"longest free run: {h(bs)}-{h(bs + bl * 20)} ({bl} slots)")
