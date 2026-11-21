P = [("Ada", 2.0, 1850), ("Ben", 1.5, 1920), ("Cyd", 1.5, 1700), ("Dev", 1.0, 1990), ("Eva", 1.0, 1600), ("Fox", 0.5, 1750), ("Gia", 0.0, 1550)]
M = [("Ada", "Ben"), ("Cyd", "Dev"), ("Ada", "Cyd"), ("Ben", "Eva"), ("Dev", "Fox")]
L = [p[0] for p in sorted(P, key=lambda p: (-int(p[1] * 2.0), -p[2]))]; t = 1
while len(L) > 1:
    a = L[0]; k = next((k for k in range(1, len(L)) if (a, L[k]) not in M and (L[k], a) not in M), 1)
    print(f"board {t}: {a} v {L[k]}"); L.pop(k); L.pop(0); t += 1
if len(L) == 1: print(f"bye: {L[0]}")
