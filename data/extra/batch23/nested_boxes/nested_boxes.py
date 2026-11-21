def longest_chain(boxes):
    order = sorted(boxes, key=lambda b: (b[0], -b[1]))
    tails = []
    back = []
    for i, b in enumerate(order):
        lo = 0
        hi = len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if order[tails[mid]][1] < b[1]:
                lo = mid + 1
            else:
                hi = mid
        back.append(tails[lo - 1] if lo > 0 else -1)
        if lo == len(tails):
            tails.append(i)
        else:
            tails[lo] = i
    chain = []
    if len(tails) == 0:
        return chain
    k = tails[-1]
    while k >= 0:
        chain.append(order[k])
        k = back[k]
    chain.reverse()
    return chain

boxes = [[5, 4], [6, 4], [6, 7], [2, 3], [8, 9], [3, 5], [7, 8], [4, 4], [9, 6], [10, 10], [3, 3]]
chain = longest_chain(boxes)
print(f"{len(boxes)} boxes, longest nesting chain has {len(chain)}")
for b in chain:
    print(f"  {b[0]:>2} x {b[1]:>2}")
same = longest_chain([[4, 4], [4, 5], [4, 6]])
print(f"three boxes of width 4 nest {len(same)} deep")
