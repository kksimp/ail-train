tips = 48763; S = [("Kai", 6), ("Lou", 4), ("Max", 7), ("Nia", 3), ("Oto", 5)]
H = sum(s[1] for s in S); sh = [tips * s[1] // H for s in S]; left = tips - sum(sh)
order = sorted(range(len(S)), key=lambda i: (-(tips * S[i][1] % H), i))
for k in range(left): sh[order[k]] += 1
for i, s in enumerate(S): print(f"{s[0]}: {s[1]} h, {sh[i] // 100}.{sh[i] % 100:02d}")
print(f"total {sum(sh)} of {tips}, {left} leftover cents handed out")
