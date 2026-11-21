rows = ["Ada, 36, ada@example.org", "Bo, 15, bo@example.org", "Cy, x9, cy@example.org", "Di, 41", "Ed, 29, ed.example.org", "Fay, 52, fay@example.org"]
users = []; pb = 0; rb = 0
for r in rows:
    f = r.split(",")
    if len(f) != 3: print(f"skip '{r}': expected 3 fields, got {len(f)}"); pb += 1; continue
    a = f[1].strip()
    if not a.isdigit(): print(f"skip '{r}': age '{a}' is not a number"); pb += 1; continue
    a = int(a); e = f[2].strip()
    if a < 16: print(f"skip '{r}': age {a} is under 16"); rb += 1; continue
    if "@" not in e: print(f"skip '{r}': email '{e}' has no @"); rb += 1; continue
    users.append(f[0].strip())
print("imported [" + ", ".join(f'"{u}"' for u in users) + "]")
print(f"{pb} unreadable, {rb} broke a rule")
