surveys = [("mill pond", 40, 35, 7), ("reed bed", 120, 100, 30), ("stream", 25, 30, 2), ("meadow", 60, 50, 0)]
def lincoln(s):
    return s[1] * s[2] // s[3]
def chapman(s):
    return (s[1] + 1) * (s[2] + 1) // (s[3] + 1) - 1
for s in surveys:
    if s[3] == 0:
        print(f"{s[0]:<10} no marked animals caught again: population too large to estimate")
        continue
    share = float(s[3]) / float(s[2]) * 100.0
    print(f"{s[0]:<10} {share:>5.1f}% marked in second catch: Lincoln {lincoln(s):>4}, Chapman {chapman(s):>4}")
sized = [s for s in surveys if s[3] > 0]
biggest = max(sized, key=chapman)
print(f"largest population: {biggest[0]}")
