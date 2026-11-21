R = [("Dune", [5, 4, 5, 5, 4, 5, 3, 5]), ("Ulysses", [5]), ("Emma", [4, 4, 3, 5, 4]), ("Ivanhoe", [2, 3, 3]), ("Beloved", [5, 5, 4, 5, 5, 4])]
A = [x for _, r in R for x in r]; ov = sum(A) / len(A); S = []
for n, r in R: S.append((n, sum(r) / len(r), (5.0 * ov + sum(r)) / (5.0 + len(r)), len(r)))
print(f"overall mean {ov:.3f}")
for s in sorted(S, key=lambda s: -s[2]): print(f"{s[0]:<8} n={s[3]} mean {s[1]:.2f} bayes {s[2]:.3f}")
