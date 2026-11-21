work, rest, rounds = 20, 10, 3
rnd = 1; working = True; left = work; sec = 0
print("round 1: work 20s")
while rnd <= rounds:
    sec += 1; left -= 1
    if left > 0: continue
    if working:
        working = False; left = rest; print(f"{sec:>3}s round {rnd}: rest {rest}s"); continue
    rnd += 1
    if rnd > rounds: print(f"{sec:>3}s finished"); break
    working = True; left = work; print(f"{sec:>3}s round {rnd}: work {work}s")
print(f"total {sec // 60}m {sec % 60}s")
