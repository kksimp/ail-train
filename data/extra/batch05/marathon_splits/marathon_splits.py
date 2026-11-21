import math
def hms(s): return f"{s // 3600}:{s // 60 % 60:02}:{s % 60:02}"
S = [1502, 1488, 1495, 1510, 1476, 1469, 1490, 1455]; t = 0
for i, s in enumerate(S):
    t += s; p = s // 5; print(f"{(i + 1) * 5:>2} km: split {hms(s)}, pace {p // 60}:{p % 60:02}/km, total {hms(t)}")
a = sum(S[:4]); b = sum(S[4:]); print(f"halves {hms(a)} / {hms(b)}: {'negative split' if b < a else 'positive split'}")
print(f"projected finish {hms(int(math.floor(t / 40 * 42.195 + 0.5)))}")
