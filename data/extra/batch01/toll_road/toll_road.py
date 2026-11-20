cars = [1, 4, 2]; trucks = [2, 5]
ct = sum(200 if p >= 3 else 400 for p in cars)
tt = sum(500 * a for a in trucks)
print(f"cars: {ct}")
print(f"trucks: {tt}")
for k, v in [("car", ct), ("truck", tt)]:
    print(f"{k}: {v // 100}.{v % 100:02d}")
