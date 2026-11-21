def stuff(bits):
    out = []
    ones = 0
    for c in bits:
        out.append(c)
        if c == '1':
            ones += 1
            if ones == 5:
                out.append('0')
                ones = 0
        else:
            ones = 0
    return "".join(out)

def unstuff(bits):
    out = []
    ones = 0
    skip = False
    for c in bits:
        if skip:
            skip = False
            ones = 0
            continue
        out.append(c)
        if c == '1':
            ones += 1
            if ones == 5:
                skip = True
        else:
            ones = 0
    return "".join(out)

flag = "01111110"
for data in ["0111111101111110", "11111111111", "0101010", "011111011111100"]:
    s = stuff(data)
    added = len(s) - len(data)
    inside = "flag inside!" if flag in s else "no flag inside"
    back = "ok" if unstuff(s) == data else "BAD"
    print(f"{data:<16} -> {s:<19} +{added} bits, {inside}, unstuff {back}")
frame = flag + stuff("0111111101111110") + flag
print(f"frame on the wire: {frame}")
