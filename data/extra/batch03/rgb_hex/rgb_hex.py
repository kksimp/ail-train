def fh(c):
    if len(c) != 7 or c[0] != "#": return None
    try: return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))
    except ValueError: return None
th = lambda c: "#" + "".join(f"{x:02x}" for x in c)
for code in ["#ff8800", "#1E90FF", "#000000", "#12345", "#zz0000"]:
    c = fh(code)
    print(f"{code} -> {c} -> {th(c)}" if c else f"{code} is not a colour")
a, b = fh("#ff0000"), fh("#0000ff")
print(f"red + blue = {th(tuple((x + y) // 2 for x, y in zip(a, b)))}")
