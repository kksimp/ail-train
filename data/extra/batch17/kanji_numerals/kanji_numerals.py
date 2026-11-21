def digit_chars():
    return ["〇", "一", "二", "三", "四", "五", "六", "七", "八", "九"]

def small(n):
    d = digit_chars()
    units = ["千", "百", "十", ""]
    divs = [1000, 100, 10, 1]
    out = []
    for i in range(4):
        k = n // divs[i] % 10
        if k == 0:
            continue
        if k == 1 and i < 3:
            out.append(units[i])
        else:
            out.append(d[k] + units[i])
    return "".join(out)

def to_kanji(n):
    if n == 0:
        return "〇"
    out = []
    oku = n // 100000000
    man = n // 10000 % 10000
    rest = n % 10000
    if oku > 0:
        out.append(small(oku) + "億")
    if man > 0:
        out.append(small(man) + "万")
    out.append(small(rest))
    return "".join(out)

def from_kanji(s):
    d = digit_chars()
    total = 0
    group = 0
    digit = 0
    for t in s:
        if t in d:
            digit = d.index(t)
        elif t in ("十", "百", "千"):
            unit = 10 if t == "十" else 100 if t == "百" else 1000
            group += (1 if digit == 0 else digit) * unit
            digit = 0
        else:
            big = 10000 if t == "万" else 100000000
            total += (group + digit) * big
            group = 0
            digit = 0
    return total + group + digit

for n in [7, 10, 15, 111, 2025, 10000, 12345, 300000, 100010001, 987654321]:
    k = to_kanji(n)
    print(f"{n:>10} {k} -> {from_kanji(k)}")
