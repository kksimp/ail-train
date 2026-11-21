sizes = ["XS", "S", "M", "L", "XL"]
orders = [("Amy", "shirt", "S"), ("Raj", "shirt", "L"), ("Tess", "hoodie", "M"), ("Ola", "shirt", "M"), ("Ken", "shirt", "XL"), ("Lin", "hoodie", "S"), ("Max", "shirt", "M"), ("Pam", "hoodie", "L"), ("Ray", "shirt", "L"), ("Sue", "shirt", "XS"), ("Tom", "hoodie", "M"), ("Uli", "shirt", "M"), ("Val", "shirt", "L"), ("Wes", "hoodie", "XL")]
prices = {"shirt": 6000, "hoodie": 11000}
count = {}
for name, item, size in orders:
    count[f"{item} {size}"] = count.get(f"{item} {size}", 0) + 1
spend = spare = 0
for item in ["shirt", "hoodie"]:
    parts = []
    for s in sizes:
        n = count.get(f"{item} {s}", 0)
        if n > 0:
            p = (n + 4) // 5
            spare += p * 5 - n
            spend += p * prices[item]
            parts.append(f"{s} {n} ({p} pk)")
    print(f"{item}: {', '.join(parts)}")
print(f"spare items: {spare}")
print(f"order cost: {spend // 100}.{spend % 100:02d}")
