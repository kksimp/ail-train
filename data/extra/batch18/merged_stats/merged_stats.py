week = [(1240, 88, 310), (980, 75, 420), (1515, 102, 260)]
s = sum(w[0] for w in week); v = sum(w[1] for w in week); b = max(w[2] for w in week)
print(f"ShopDay(sales: {s}, visits: {v}, best: {b})")
print(f"average sale {s // v} per visit")
spans = [(3, 11, 7), (-2, 8, 7), (5, 14, 6)]
print(f"{sum(x[2] for x in spans)} days from {min(x[0] for x in spans)} to {max(x[1] for x in spans)} degrees")
print("no data: 0 days")
