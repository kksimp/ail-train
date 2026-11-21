from itertools import permutations
N = ["Depot", "Mill", "Farm", "Inn", "Quay", "Croft"]
D = [[0, 12, 19, 8, 14, 22], [12, 0, 9, 15, 20, 11], [19, 9, 0, 13, 25, 7], [8, 15, 13, 0, 10, 16], [14, 20, 25, 10, 0, 18], [22, 11, 7, 16, 18, 0]]
b = 10 ** 6; bo = []; t = 0
for p in permutations([1, 2, 3, 4, 5]):
    t += 1; s = D[0][p[0]] + sum(D[p[i - 1]][p[i]] for i in range(1, len(p))) + D[p[-1]][0]
    if s < b: b = s; bo = p
print(f"{t} orders tried"); print(f"best: Depot > {' > '.join(N[i] for i in bo)} > Depot = {b} km")
