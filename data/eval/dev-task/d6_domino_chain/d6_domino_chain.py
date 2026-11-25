import sys
import re

for line in sys.stdin.read().splitlines():
    tiles = line.split()
    if not tiles:
        continue
    if not all(re.fullmatch(r"[0-6]-[0-6]", t) for t in tiles):
        print("invalid")
        continue
    nums = [(int(t[0]), int(t[2])) for t in tiles]
    broken = 0
    for i in range(1, len(nums)):
        if nums[i][0] != nums[i - 1][1]:
            broken = i + 1
            break
    if broken:
        print(f"broken at {broken}")
    else:
        print(f"valid {sum(a + b for a, b in nums)}")
