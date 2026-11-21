cols = ["name", "joined", "level"]
rows = [["Iris", "2021", "gold"], ["Omar", "2023", "silver"]]
print(";".join(cols))
for r in rows: print(";".join(r))
print("(2 rows)")
print("| " + " | ".join(cols) + " |")
print("| " + " | ".join("---" for c in cols) + " |")
for r in rows: print("| " + " | ".join(r) + " |")
print("_2 members_")
print("".join(c.upper().ljust(8) for c in cols).rstrip())
for r in rows: print("".join(c.ljust(8) for c in r).rstrip())
print("(2 rows)")
