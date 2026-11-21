from functools import reduce
def xor_all(xs):
    return reduce(lambda a, x: a ^ x, xs, 0)

def hex2(n):
    return f"{n:02x}"

disks = [[0x41, 0x6e, 0x20, 0x45], [0x62, 0x79, 0x74, 0x65], [0x7f, 0x00, 0x13, 0xc4], [0x99, 0x2a, 0x5e, 0x01]]
stripes = len(disks[0])
parity = [xor_all([d[s] for d in disks]) for s in range(stripes)]
for i, d in enumerate(disks):
    print(f"disk {i}:   {' '.join(hex2(b) for b in d)}")
print(f"parity:   {' '.join(hex2(b) for b in parity)}")
lost = 2
print(f"disk {lost} fails")
rebuilt = []
for s in range(stripes):
    others = [parity[s]]
    for i in range(len(disks)):
        if i != lost:
            others.append(disks[i][s])
    rebuilt.append(xor_all(others))
print(f"rebuilt:  {' '.join(hex2(b) for b in rebuilt)}")
print(f"matches original: {str(rebuilt == disks[lost]).lower()}")
