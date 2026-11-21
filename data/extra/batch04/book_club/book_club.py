R = [("Una", "Dune", 5), ("Vic", "Dune", 4), ("Wes", "Dune", 3), ("Una", "Emma", 2), ("Wes", "Emma", 4), ("Vic", "Kim", 5), ("Una", "Kim", 4), ("Wes", "Kim", 5), ("Vic", "Ulysses", 1)]
M = ["Una", "Vic", "Wes"]; B = []
for r in R:
    if r[1] not in B: B.append(r[1])
for b in B:
    rs = [r[2] for r in R if r[1] == b]; a = sum(rs) * 100 // len(rs)
    print(f"{b:<8} {a // 100}.{a % 100:02d} from {len(rs)}")
avg = lambda m: sum(r[2] for r in R if r[0] == m) * 100 // len([r for r in R if r[0] == m])
print(f"most generous: {max(M, key=avg)}")
print("rated by all: " + ", ".join(b for b in B if len([r for r in R if r[1] == b]) == len(M)))
