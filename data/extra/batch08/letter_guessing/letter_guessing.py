def shown(w, f): return " ".join(c if c in f else "_" for c in w)
def play(w, gs):
    f = set(); m = 0
    for g in gs:
        hit = g in w
        if hit: f.add(g)
        else: m += 1
        b = shown(w, f); print(f"{g}: {b} ({'hit' if hit else f'miss {m}'})")
        if "_" not in b: print(f"solved with {m} misses"); return
        if m == 6: print(f"out of guesses, the word was {w}"); return
play("PLANET", list("EASTRLNP")); play("RHYTHM", list("EAIOUST"))
