S = ["York", "Leeds", "Wakefield", "Sheffield", "Derby", "Leicester"]
F = {f"{a}-{b}": c for a, b, c in [("York", "Leeds", 1290), ("York", "Wakefield", 2150), ("York", "Sheffield", 3460), ("York", "Leicester", 7900), ("Leeds", "Sheffield", 1720), ("Leeds", "Derby", 3800), ("Wakefield", "Derby", 2400), ("Sheffield", "Derby", 1530), ("Sheffield", "Leicester", 3100), ("Derby", "Leicester", 1180), ("Leeds", "Wakefield", 690), ("Wakefield", "Sheffield", 1100)]}
n = len(S); B = [0] * n; Fr = [0] * n
for j in range(1, n):
    B[j] = 1000000
    for i in range(j):
        k = f"{S[i]}-{S[j]}"
        if k in F and B[i] + F[k] < B[j]: B[j] = B[i] + F[k]; Fr[j] = i
L = []; a = n - 1
while a > 0: L.append(f"{S[Fr[a]]}-{S[a]}"); a = Fr[a]
t = F["York-Leicester"]; print("tickets: " + ", ".join(reversed(L))); print(f"split cost {B[-1] // 100}.{B[-1] % 100:02} vs through {t // 100}.{t % 100:02}")
