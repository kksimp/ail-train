def joined(a, b):
    p = 10
    while p <= b:
        p *= 10
    return a * p + b

def fits(target, nums, i, acc, join):
    if acc > target: return False
    if i == len(nums): return acc == target
    if fits(target, nums, i + 1, acc + nums[i], join) or fits(target, nums, i + 1, acc * nums[i], join):
        return True
    return join and fits(target, nums, i + 1, joined(acc, nums[i]), join)

lines = ["150: 10 15", "47: 3 4 35", "1210: 12 10", "96: 2 6 8 2", "3312: 3 3 12", "640: 8 8 10", "7290: 6 8 6 15", "58: 5 8 1", "2410: 2 4 10"]
p1 = p2 = 0
for l in lines:
    k, v = l.split(": ")
    target = int(k); nums = [int(w) for w in v.split(" ")]
    a = fits(target, nums, 1, nums[0], False)
    b = fits(target, nums, 1, nums[0], True)
    mark = "add" if a else ("cat" if b else "---")
    print(f"{mark} {l}")
    if a: p1 += target
    if b: p2 += target
print(f"part 1: {p1}")
print(f"part 2: {p2}")
