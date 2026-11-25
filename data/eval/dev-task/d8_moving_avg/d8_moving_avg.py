import sys

lines = sys.stdin.read().splitlines()
first = lines[0].strip() if lines else ""
try:
    k = int(first)
except ValueError:
    k = 0
if k < 1 or not (first.lstrip("-").isascii() and first.lstrip("-").isdigit()):
    print("bad window")
    sys.exit(0)
vals = []
for line in lines[1:]:
    vals.extend(line.split())
if not all(v.isascii() and v.isdigit() for v in vals):
    print("bad value")
    sys.exit(0)
nums = [int(v) for v in vals]
if len(nums) < k:
    print("none")
else:
    print(" ".join(str(sum(nums[i:i + k]) // k) for i in range(len(nums) - k + 1)))
