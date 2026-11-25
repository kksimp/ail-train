import sys
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    nums = []
    ignored = 0
    for t in sys.stdin.read().split():
        if t.isascii() and t.isdigit() and 1 <= int(t) <= 1000000 and len(nums) < 8:
            nums.append(int(t))
        else:
            ignored += 1
    print("numbers: " + (" ".join(map(str, nums)) if nums else "none"))
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a, b = nums[i], nums[j]
            print(f"gcd({a},{b})={gcd(a, b)} lcm({a},{b})={lcm(a, b)}")
    if len(nums) >= 2:
        g = nums[0]
        l = nums[0]
        for x in nums[1:]:
            g = gcd(g, x)
            l = lcm(l, x)
        print(f"all gcd={g} all lcm={l}")
    print(f"ignored {ignored}")

main()
