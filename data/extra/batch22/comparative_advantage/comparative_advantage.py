hours = 600
lands = [("North", 2, 3), ("South", 6, 4)]
for name, c, w in lands:
    oc = float(c) / float(w)
    print(f"{name}: a cloth costs {oc:.2f} wine, a wine costs {1.0 / oc:.2f} cloth")
cloth = 0
wine = 0
for name, c, w in lands:
    cloth += hours // 2 // c
    wine += hours // 2 // w
print(f"even split: {cloth} cloth, {wine} wine")
spec_wine = hours // 4
north_cloth = cloth
left = hours - north_cloth * 2
north_wine = left // 3
print(f"specialised: North {north_cloth} cloth and {north_wine} wine, South {spec_wine} wine")
print(f"same cloth, wine up from {wine} to {spec_wine + north_wine}")
