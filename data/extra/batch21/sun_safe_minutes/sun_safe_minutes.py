uv = [2, 4, 6, 7, 8, 7, 5, 3, 1]

def burn_minute(uv, start, threshold):
    dose = 0
    for m in range(start, len(uv) * 60):
        dose += uv[m // 60]
        if dose >= threshold:
            return m + 1
    return -1

def at(m):
    return f"{9 + m // 60:02d}:{m % 60:02d}"

start = 2 * 60
for name, dose in [("I", 70), ("II", 100), ("III", 200), ("IV", 300), ("V", 450)]:
    bare = burn_minute(uv, start, dose)
    cream = burn_minute(uv, start, dose * 5)
    a = "safe all day" if bare < 0 else f"burns {at(bare)}"
    b = "safe all day" if cream < 0 else f"burns {at(cream)}"
    print(f"type {name:<3}: {a}; thin sunscreen (x5): {b}")
print(f"dose from 11:00 to 18:00: {sum(uv[2:]) * 60} UV-minutes")
