def ff(s, sub):
    d = s.split("@")[1]; l = sub.lower()
    if d == "bank.example": return "finance"
    if "invoice" in l or "receipt" in l: return "finance"
    if d == "school.example": return "family"
    if "sale" in l or "offer" in l: return "promotions"
    return "inbox"
c = {}
for s, sub in [("alerts@bank.example", "Your statement"), ("shop@store.example", "Big SALE this weekend"), ("office@school.example", "Trip letter"), ("ann@friends.example", "Lunch?"), ("billing@host.example", "Invoice 2291"), ("deals@store.example", "A special offer"), ("head@school.example", "Receipt for dinner money")]:
    f = ff(s, sub); c[f] = c.get(f, 0) + 1; print(f"{sub:<26} -> {f}")
for f in sorted(c): print(f"{f}: {c[f]}")
