def bucket(o):
    if 1 <= o <= 30: return 1
    if 31 <= o <= 60: return 2
    if 61 <= o <= 90: return 3
    if o <= 0: return 0
    return 4
today = 200
names = ["current", "1-30", "31-60", "61-90", "over 90"]
allowance = [1, 3, 10, 25, 50]
invoices = [("Abel", 125000, 210), ("Brook", 48050, 188), ("Cole", 230000, 150), ("Abel", 61500, 131), ("Dunn", 15999, 95), ("Brook", 72000, 175), ("Eve", 38800, 60)]
totals = [0] * 5
for c, cents, due in invoices:
    totals[bucket(today - due)] += cents
reserve = 0
for i in range(5):
    r = totals[i] * allowance[i] // 100
    reserve += r
    print(f"{names[i]:<8} {totals[i] // 100:>6}.{totals[i] % 100:02}  allowance {r // 100:>5}.{r % 100:02}")
a = sum(totals)
print(f"total {a // 100}.{a % 100:02}, allowance {reserve // 100}.{reserve % 100:02}")
