forms = [("Ama", [4, 5, None, 3, 5]), ("Ben", [None, 2, 2, None, 1]), ("Caz", []), ("Dev", [5, 5, 4, 4, 5])]
def df(xs):
    if not xs: return "empty form"
    return f"first answer {xs[0]}" if xs[0] is not None else "first question skipped"
sk = 0
for w, a in forms:
    g = [x for x in a if x is not None]; sk += len(a) - len(g)
    if not g:
        print(f"{w}: no answers ({df(a)})"); continue
    m = float(sum(g)) / float(len(g))
    print(f"{w}: mean {m:.2f} from {len(g)} answers, {df(a)}")
print(f"{sk} questions skipped in total")
