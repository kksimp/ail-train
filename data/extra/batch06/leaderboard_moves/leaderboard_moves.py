L = ["Kim", "Lou", "Max", "Ned", "Oz", "Pia"]; N = ["Lou", "Kim", "Pia", "Qi", "Max", "Ned"]
for i, p in enumerate(N):
    if p in L: m = L.index(p) - i; print(f"{i + 1}. {p:<4} {'up ' + str(m) if m > 0 else 'down ' + str(-m) if m < 0 else 'same'}")
    else: print(f"{i + 1}. {p:<4} new")
print(f"dropped out: {', '.join(p for p in L if p not in N)}")
