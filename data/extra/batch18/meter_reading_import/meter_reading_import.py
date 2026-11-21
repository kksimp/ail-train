months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
raw = ["10412", "10790", "1O980", "11105", "11002", "12950", " 11388 "]
prev = 10200; used = []; sk = 0
for i, t in enumerate(raw):
    s = t.strip()
    if not s.isdigit(): print(f"{months[i]}: skipped, '{t}' is not a reading"); sk += 1; continue
    v = int(s)
    if v < prev: print(f"{months[i]}: skipped, {v} is lower than {prev}"); sk += 1; continue
    if v - prev > 900: print(f"{months[i]}: skipped, jump of {v - prev} kWh looks wrong"); sk += 1; continue
    used.append(v - prev); print(f"{months[i]}: {v}, used {v - prev} kWh"); prev = v
print(f"{sum(used)} kWh over {len(used)} readings, {sk} skipped")
