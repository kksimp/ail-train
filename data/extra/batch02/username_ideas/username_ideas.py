def cands(full):
    p = full.lower().split()
    if not p: return []
    f, l = p[0], p[-1]
    return [f, f"{f}.{l}", f"{f[0]}{l}", "".join(x[0] for x in p)] + [f"{f}{n}" for n in range(2, 5)]
taken = {"anna", "anna.lee", "alee", "bob", "bob.smith", "bsmith", "bjs", "bob2"}
for name in ["Anna Lee", "Bob James Smith", "Cleo", "Anna Lee", "  "]:
    u = next((c for c in cands(name) if c not in taken), None)
    if u:
        taken.add(u); print(f"{name}: {u}")
    else:
        print(f"'{name}': no username")
print(f"taken now: {len(taken)}")
