def flag_sort(t):
    low = mid = 0; high = len(t) - 1; sw = 0
    while mid <= high:
        if t[mid] == "R":
            t[low], t[mid] = t[mid], t[low]; low += 1; mid += 1; sw += 1
        elif t[mid] == "W":
            mid += 1
        else:
            t[mid], t[high] = t[high], t[mid]; high -= 1; sw += 1
    return sw
tiles = list("BWRBRWWRBR")
print("before: " + "".join(tiles))
exp = sorted(tiles, key="RWB".index)
n = flag_sort(tiles)
print(f"after:  {''.join(tiles)} ({n} swaps)")
print(f"matches sort: {str(tiles == exp).lower()}")
print(0)
