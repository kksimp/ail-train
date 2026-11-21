F = [(12000, 0.0), (12540, 38.2), (13110, 41.0), (13600, 35.5), (14230, 44.9)]; k = 0; l = 0.0
for i in range(1, len(F)):
    g = F[i][0] - F[i - 1][0]; u = F[i][1]; print(f"leg {i}: {g} km, {u:.1f} l, {u * 100 / g:.2f} l/100km"); k += g; l += u
print(f"total {k} km, average {l * 100 / k:.2f} l/100km")
