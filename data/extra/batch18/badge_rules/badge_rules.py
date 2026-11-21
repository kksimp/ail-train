W = [("Noa", [9000, 12000, 8500, 8100, 9900, 4000, 21000, 8800, 9100, 10200, 7000, 11000]), ("Jem", [3000, 0, 2500, 4100, 3900, 6000, 5200, 1800, 2600, 4400, 3000, 2000]), ("Rui", [15000, 14000, 16500, 9000, 12000, 13000, 8000, 9500, 11000, 8200, 7900, 10100])]
def run(d, g):
    b = r = 0
    for x in d:
        r = r + 1 if x >= g else 0; b = max(b, r)
    return b
for who, d in W:
    got = []
    if sum(d) >= 100000: got.append("100k club")
    if all(x > 0 for x in d): got.append("every day")
    if any(x >= 20000 for x in d): got.append("big day")
    if run(d, 8000) >= 5: got.append("streak 5")
    j = ", ".join(got) if got else "none yet"
    print(f"{who}: {sum(d)} steps, best run {run(d, 8000)} -> {j}")
