def ordinal(n):
    if 11 <= n % 100 <= 13:
        suffix = "th"
    elif n % 10 == 1:
        suffix = "st"
    elif n % 10 == 2:
        suffix = "nd"
    elif n % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{n}{suffix}"

def regnal(date, monarchs):
    current = -1
    for i, m in enumerate(monarchs):
        if m[1] <= date:
            current = i
    if current < 0:
        return None
    name, acc = monarchs[current]
    year = date // 10000 - acc // 10000
    if date % 10000 >= acc % 10000:
        year += 1
    return f"the {ordinal(year)} year of {name}"

monarchs = [("Queen Mab", 16030324), ("King Oberon", 16250327), ("Queen Titania", 16490130), ("King Puck", 16600529)]
docs = [16030401, 16040323, 16040324, 16241231, 16250327, 16480101, 16500130, 16611111, 15991225]
for d in docs:
    shown = f"{d // 10000}-{d // 100 % 100:02}-{d % 100:02}"
    r = regnal(d, monarchs)
    if r is not None:
        print(f"{shown}: {r}")
    else:
        print(f"{shown}: before the first recorded accession")
