def insert(kids, x):
    node = 0
    for b in range(4, -1, -1):
        bit = (x >> b) & 1
        if kids[node][bit] < 0:
            kids.append([-1, -1])
            kids[node][bit] = len(kids) - 1
        node = kids[node][bit]

def best(kids, x):
    node = 0
    y = 0
    for b in range(4, -1, -1):
        bit = (x >> b) & 1
        want = 1 - bit
        if kids[node][want] >= 0:
            node = kids[node][want]
            y |= want << b
        else:
            node = kids[node][bit]
            y |= bit << b
    return y

nums = [3, 10, 5, 25, 2, 8, 17, 30]
kids = [[-1, -1]]
for x in nums:
    insert(kids, x)
print(f"{len(nums)} numbers, {len(kids)} trie nodes")
top = 0
for x in nums:
    y = best(kids, x)
    top = max(top, x ^ y)
    print(f"{x:>2} ({x:05b}) pairs best with {y:>2} ({y:05b}): xor {x ^ y}")
brute = max(a ^ c for a in nums for c in nums)
print(f"largest xor {top}, all pairs give {brute}")
