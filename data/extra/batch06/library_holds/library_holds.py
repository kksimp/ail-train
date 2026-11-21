H = {}; S = {}
for e in ["hold Dune Ann", "hold Dune Bob", "return Dune", "hold Emma Cy", "return Emma", "return Dune", "return Dune", "hold Dune Dee", "return Emma"]:
    p = e.split(" "); b = p[1]
    if p[0] == "hold":
        if S.get(b, 0) > 0: S[b] -= 1; print(f"{p[2]} takes {b} from the shelf")
        else: H.setdefault(b, []).append(p[2]); print(f"{p[2]} queues for {b}")
    else:
        q = H.get(b, [])
        if not q: S[b] = S.get(b, 0) + 1; print(f"{b} back on shelf ({S[b]})")
        else: print(f"{b} goes to {q[0]}"); H[b] = q[1:]
for b in sorted(S): print(f"shelf {b}: {S[b]}")
