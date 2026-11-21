D = [("pad thai", {"peanut", "egg", "soy"}, True), ("risotto", {"dairy"}, True), ("bean chilli", set(), True), ("fish pie", {"fish", "dairy", "gluten"}, True), ("fruit salad", set(), False), ("cheesecake", {"dairy", "gluten", "egg"}, False)]
for w, a in [("Ike", {"peanut"}), ("Jo", {"dairy", "gluten"}), ("Kai", {"egg", "soy", "dairy"}), ("Lu", set())]:
    s = [d for d in D if not (d[1] & a)]; m = sum(1 for d in s if d[2])
    print(f"{w}: {', '.join(d[0] for d in s)}")
    if m < 2: print(f"  only {m} main for {w}")
