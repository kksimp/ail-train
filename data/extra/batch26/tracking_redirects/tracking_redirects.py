status = {"TRK100": "in transit", "TRK200": "delivered", "TRK300": "held at depot"}
redirect = {"TRK150": "TRK300", "TRK999": "TRK998"}
def resolve(code):
    if code in status: return status[code]
    if code in redirect:
        r = redirect[code]
        return f"relabelled {r}, {status.get(r, 'unknown parcel')}"
    return "no record"
qs = ["TRK100", "TRK150", "TRK200", "TRK999", "TRK404"]
found = 0
for c in qs:
    t = resolve(c)
    if t != "no record": found += 1
    print(f"{c}: {t}")
print(f"answered {found} of {len(qs)} queries")
print(f"delivered parcels: {sum(1 for v in status.values() if v == 'delivered')}")
