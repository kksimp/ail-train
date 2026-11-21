def marker(s, k):
    for i in range(k, len(s) + 1):
        if len(set(s[i - k:i])) == k:
            return i
    return -1

bursts = ["qpqzrqpwtyxvnmbbcda", "aabbccddeeffgghhijklmnop", "xyxyzzwvutsrqponmlk", "hellohelloabcdefghij", "zzzzzzzzzzzz"]
found = 0
for b in bursts:
    p1 = marker(b, 4); p2 = marker(b, 9)
    if p2 > 0:
        found += 1
    print(f"{b:<26} part 1: {p1:>3}  part 2: {p2:>3}")
print(f"{found} of {len(bursts)} bursts carry a full message marker")
