def best(book, side):
    at = -1
    for i in range(len(book)):
        o = book[i]
        if o[1] == side and o[3] > 0:
            better = at < 0 or (side == "sell" and o[2] < book[at][2]) or (side == "buy" and o[2] > book[at][2])
            if better:
                at = i
    return at

book = []
incoming = [[1, "sell", 102, 50], [2, "sell", 101, 30], [3, "buy", 99, 40], [4, "buy", 102, 60], [5, "sell", 98, 70], [6, "sell", 101, 25], [7, "buy", 103, 45]]
volume = 0
for o0 in incoming:
    o = list(o0)
    other = "sell" if o[1] == "buy" else "buy"
    while o[3] > 0:
        at = best(book, other)
        if at < 0:
            break
        p = book[at][2]
        crosses = p <= o[2] if o[1] == "buy" else p >= o[2]
        if not crosses:
            break
        fill = min(o[3], book[at][3])
        print(f"trade {fill} at {p}: order {o[0]} with resting order {book[at][0]}")
        book[at][3] -= fill
        o[3] -= fill
        volume += fill
    if o[3] > 0:
        book.append(o)
    book = [r for r in book if r[3] > 0]
for side in ["buy", "sell"]:
    rest = [f"{r[3]}@{r[2]}" for r in book if r[1] == side]
    shown = "empty" if len(rest) == 0 else " ".join(rest)
    print(f"{side} side: {shown}")
print(f"traded volume {volume}")
