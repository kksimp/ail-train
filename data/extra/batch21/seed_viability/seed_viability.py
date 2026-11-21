keeps = {"parsnip": 1, "onion": 2, "carrot": 3, "pea": 3, "bean": 3, "kale": 4, "lettuce": 5, "tomato": 5, "squash": 6}
packets = [("parsnip", 2025), ("onion", 2023), ("carrot", 2024), ("pea", 2022), ("lettuce", 2021), ("tomato", 2023), ("squash", 2019), ("kale", 2026), ("bean", 2023), ("okra", 2025)]

def verdict(now, packed, k):
    age = now - packed
    if k < 0:
        return "Unknown"
    return "Discard" if age > k else ("Thick" if age == k else "Fine")

groups = {}
for crop, year in packets:
    groups.setdefault(verdict(2026, year, keeps.get(crop, -1)), []).append(f"{crop} ({year})")
for v in ["Fine", "Thick", "Discard", "Unknown"]:
    items = groups.get(v, [])
    if items:
        print(f"{v:<8} {', '.join(items)}")
print(f"packets to replace: {len(groups.get('Discard', []))}")
