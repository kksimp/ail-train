def indian(n):
    s = str(n)
    if len(s) <= 3:
        return s
    head = s[:len(s) - 3]
    tail = s[len(s) - 3:]
    groups = []
    end = len(head)
    while end > 0:
        start = max(end - 2, 0)
        groups.insert(0, head[start:end])
        end = start
    groups.append(tail)
    return ",".join(groups)

def spoken(n):
    parts = []
    crore = n // 10000000
    lakh = n // 100000 % 100
    thousand = n // 1000 % 100
    rest = n % 1000
    if crore > 0:
        parts.append(f"{crore} crore")
    if lakh > 0:
        parts.append(f"{lakh} lakh")
    if thousand > 0:
        parts.append(f"{thousand} thousand")
    if rest > 0 or not parts:
        parts.append(f"{rest}")
    return " ".join(parts)

for n in [999, 1000, 54321, 100000, 1234567, 98765432, 1500000000]:
    print(f"{n:>13,}  {indian(n):>14}  {spoken(n)}")
