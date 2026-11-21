M = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]; R = [84, 60, 62, 55, 50, 58, 45, 52, 60, 88, 95, 90]; t = max(R); H = [(r * 8 + t // 2) // t for r in R]
for lv in range(8):
    row = 8 - lv; print(f"{row}|" + " ".join("#" if h >= row else " " for h in H).rstrip())
print(" +" + "-" * 23); print("  " + " ".join(M))
