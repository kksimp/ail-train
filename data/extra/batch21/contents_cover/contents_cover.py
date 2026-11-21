items = [("sofa", 120000), ("television", 80000), ("beds", 150000), ("clothes", 300000), ("kitchen goods", 220000), ("laptop", 90000), ("bikes", 140000)]
value = sum(v for _, v in items)
print(f"contents worth {value // 100}")

def payout(claim, insured, value, excess):
    scaled = claim if insured >= value else claim * insured // value
    return max(scaled - excess, 0)

policies = [("Hale", 1100000, 10000), ("Iqbal", 800000, 25000), ("Jones", 550000, 10000)]
claims = [45000, 300000, 8000]
for h, ins, ex in policies:
    under = 0 if ins >= value else (value - ins) * 100 // value
    print(f"{h}: insured {ins // 100}, {under}% under-insured")
    for c in claims:
        got = payout(c, ins, value, ex)
        print(f"  claim {c // 100:>5} -> paid {got // 100}.{got % 100:02d}")
