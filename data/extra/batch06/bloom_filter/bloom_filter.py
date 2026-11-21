def hs(s, sd):
    h = sd
    for c in s: h = (h * 31 + ord(c)) % 1000003
    return h % 64
A = ["apple", "pear", "plum", "fig", "kiwi", "lime", "date", "grape"]; B = [False] * 64
for w in A:
    for sd in [7, 13, 101]: B[hs(w, sd)] = True
print(f"{sum(B)} of 64 bits set"); fp = 0
for w in ["apple", "fig", "melon", "cherry", "lemon", "peach", "grape", "mango", "berry", "olive"]:
    m = all(B[hs(w, sd)] for sd in [7, 13, 101]); t = w in A
    if m and not t: fp += 1
    print(f"{w}: {'maybe' if m else 'no'}{' (false positive)' if m and not t else ''}")
print(f"{fp} false positives")
