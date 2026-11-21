M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]; S = [1.6, 2.4, 3.3, 4.6, 5.5, 5.9, 5.8, 5.0, 3.9, 2.7, 1.8, 1.3]; D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]; K = []
for i in range(12):
    e = 4800.0 * S[i] * D[i] * 0.82 / 1000.0; K.append(e); print(f"{M[i]} {e:>7.1f} kWh")
t = 0.0
for k in K: t += k
print(f"best {M[K.index(max(K))]}, worst {M[K.index(min(K))]}, year {t:.0f} kWh")
