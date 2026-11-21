T = ["Owls", "Foxes", "Bears"]; R = [[5, 3, 4], [2, 6, 4], [4, 4, 5], [6, 2, 3]]; J = {"Owls": 2, "Foxes": 1, "Bears": 3}; tot = {t: 0 for t in T}
for r, sc in enumerate(R):
    for i, t in enumerate(T): tot[t] += sc[i] * 2 * (2 if J[t] == r + 1 else 1)
    rk = sorted(T, key=lambda t: (-tot[t], t)); ln = []; rank = 0
    for k, t in enumerate(rk):
        if k == 0 or tot[t] != tot[rk[k - 1]]: rank = k + 1
        ln.append(f"{rank}. {t} {tot[t]}")
    print(f"after round {r + 1}: " + "  ".join(ln))
