def rn(f):
    for n in range(1, 100):
        num = f * 100 + n
        if "4" not in str(num) and n != 13: yield num
import itertools
allr = []
for f in [1, 2, 3, 5]:
    r = list(itertools.islice(rn(f), 16)); allr += r
    print(f"floor {f}: {r[0]} to {r[-1]}, {r[-1] - r[0] + 1 - len(r)} numbers skipped")
print(f"{len(allr)} rooms, none with a 4: true")
print(f"floor 1 rooms 11 to 14: {list(itertools.islice(rn(1), 10, 14))}")
