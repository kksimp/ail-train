class Customer:
    def __init__(self, email, name, phone, city, day):
        self.email, self.name, self.phone, self.city, self.day = email, name, phone, city, day

def key_of(email):
    return email.strip().lower()

def pick(old, new):
    return new if new != "" else old

rows = [Customer("Ana@Mail.com", "Ana", "", "Oslo", 3), Customer("ben@shop.io", "Ben K", "555-0101", "", 1), Customer(" ana@mail.com", "Ana Silva", "555-0199", "", 7), Customer("cy@web.net", "Cy", "555-0123", "Lima", 2), Customer("BEN@shop.io ", "", "", "Pune", 5), Customer("ana@mail.com", "", "555-0100", "Bergen", 4)]
sorted_rows = sorted(rows, key=lambda c: c.day)
merged = {}
sources = {}
for c in sorted_rows:
    k = key_of(c.email)
    sources[k] = sources.get(k, 0) + 1
    if k in merged:
        old = merged[k]
        merged[k] = Customer(k, pick(old.name, c.name), pick(old.phone, c.phone), pick(old.city, c.city), c.day)
    else:
        merged[k] = Customer(k, c.name, c.phone, c.city, c.day)
for k, c in merged.items():
    print(f"{k:<13} {c.name:<10} {c.phone:<9} {c.city:<7} from {sources[k]} rows")
print(f"{len(rows)} rows -> {len(merged)} customers")
