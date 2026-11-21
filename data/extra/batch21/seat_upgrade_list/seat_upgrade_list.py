tier_rank = {"Gold": 0, "Silver": 1, "Bronze": 2, "Basic": 3}
fare_rank = {"Y": 0, "B": 1, "M": 2}
lst = [("Ng", "Silver", "M", 610), ("Okafor", "Gold", "Y", 655), ("Price", "Basic", "Y", 540), ("Quinn", "Gold", "M", 600), ("Ruiz", "Silver", "Y", 630), ("Shah", "Bronze", "B", 560), ("Tran", "Silver", "Y", 615), ("Ueda", "Basic", "K", 500)]
seats = 3
order = sorted(lst, key=lambda w: (tier_rank[w[1]], fare_rank.get(w[2], 3), w[3]))
for i, w in enumerate(order):
    label = "UPGRADED" if i < seats else f"waitlist {i - seats + 1}"
    print(f"{i + 1}. {w[0]:<7} {w[1]:<7} fare {w[2]}: {label}")
golds = sum(1 for w in order[:seats] if w[1] == "Gold")
print(f"{golds} of {seats} seats went to Gold members")
