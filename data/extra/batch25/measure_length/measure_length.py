def verdict(cpl):
    if cpl < 45:
        return "too narrow"
    if cpl > 75:
        return "too wide"
    return "comfortable"

layouts = [("phone", 320, 16), ("tablet", 600, 16), ("article", 680, 18), ("desktop", 960, 16), ("sidebar", 280, 14), ("wide hero", 1200, 20), ("print column", 450, 10)]
ok = 0
for name, width, size in layouts:
    cpl = width * 2 // size
    v = verdict(cpl)
    if v == "comfortable":
        ok += 1
    ideal = width / 33.0
    print(f"{name:<12} {width:>4}px at {size}px: {cpl:>3} chars, {v:<11} (66 chars at {ideal:.1f}px)")
print(f"{ok} of {len(layouts)} layouts read comfortably; 66 chars at 16px needs {66 * 16 // 2}px")
