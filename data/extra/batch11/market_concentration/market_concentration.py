def hhi(shares):
    return sum(s * s for s in shares)
def label(h):
    return "unconcentrated" if h < 1500 else ("moderately concentrated" if h <= 2500 else "highly concentrated")
markets = {"coffee shops": [12, 10, 9, 8, 8, 7, 6, 40], "phone networks": [35, 30, 20, 15], "search": [88, 6, 4, 2], "bakeries": [5, 5, 4, 4, 3, 3, 76]}
for name, shares in markets.items():
    h = hhi(shares)
    print(f"{name:<15} HHI {h:>5}: {label(h)}")
phones = markets["phone networks"]
merged = [phones[0] + phones[2], phones[1], phones[3]]
after = hhi(merged)
print(f"merging networks 1 and 3: HHI {hhi(phones)} -> {after} (+{2 * phones[0] * phones[2]})")
