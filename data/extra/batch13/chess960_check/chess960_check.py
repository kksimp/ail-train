def problem(rank):
    cs = list(rank)
    for piece in ['K', 'Q', 'R', 'B', 'N']:
        want = 1 if piece in "KQ" else 2
        if cs.count(piece) != want or len(cs) != 8:
            return "wrong pieces"
    bishops = [i for i, c in enumerate(cs) if c == 'B']
    rooks = [i for i, c in enumerate(cs) if c == 'R']
    king = cs.index('K')
    if bishops[0] % 2 == bishops[1] % 2:
        return "bishops on one colour"
    if king < rooks[0] or king > rooks[1]:
        return "king not between rooks"
    return ""

def build(prefix, left, found):
    if len(prefix) == 8:
        if problem(prefix) == "":
            found.append(prefix)
        return
    for p in ['B', 'K', 'N', 'Q', 'R']:
        if left[p] > 0:
            left[p] -= 1
            build(prefix + p, left, found)
            left[p] += 1

for rank in ["RNBQKBNR", "BBRNKNQR", "KRNBBNRQ", "RNBQKBNN", "QNRBKRNB", "RKNQBBNR", "RNBKQNBR"]:
    why = problem(rank)
    verdict = "legal" if why == "" else why
    print(f"{rank}: {verdict}")
left = {'B': 2, 'K': 1, 'N': 2, 'Q': 1, 'R': 2}
found = []
build("", left, found)
print(f"legal starting ranks: {len(found)}")
print(f"first: {found[0]}, last: {found[-1]}")
