R = [1204, 1213, 1221, 1232, 1240, 1262, 1271, 1279, 1290, 1298]; U = [R[i] - R[i - 1] for i in range(1, len(R))]; a = sum(U) / len(U); b = 0
for i, u in enumerate(U):
    lo = min(u, 12); c = lo * 180 + (u - lo) * 260; b += c; print(f"month {i + 1}: {u} m3, {c // 100}.{c % 100:02}{' leak?' if u > a * 1.5 else ''}")
print(f"average {a:.2f} m3, total {b // 100}.{b % 100:02}")
