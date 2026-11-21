P = [("Ola", "fuel", 9000), ("Pim", "cabin", 36000), ("Quy", "food", 12600), ("Ola", "ferry", 4800), ("Rex", "food", 3600)]; N = ["Ola", "Pim", "Quy", "Rex"]
s = {p: 0 for p in N}
for p in P: s[p[0]] += p[2]
t = sum(p[2] for p in P); sh = t // 4; print(f"total {t // 100}, share {sh // 100} each")
ow = sorted([[p, sh - s[p]] for p in N if s[p] < sh], key=lambda x: (-x[1], x[0])); gt = sorted([[p, s[p] - sh] for p in N if s[p] > sh], key=lambda x: (-x[1], x[0])); i = j = 0
while i < len(ow) and j < len(gt):
    a = min(ow[i][1], gt[j][1]); print(f"{ow[i][0]} pays {gt[j][0]} {a // 100}.{a % 100:02}")
    ow[i][1] -= a; gt[j][1] -= a
    if ow[i][1] == 0: i += 1
    if gt[j][1] == 0: j += 1
