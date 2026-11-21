card = [[3, 18, 33, 49, 62], [11, 22, 40, 54, 70], [7, 29, 0, 46, 66], [14, 16, 38, 58, 75], [1, 25, 44, 52, 68]]
calls = [22, 40, 7, 62, 54, 29, 46, 11, 66, 70, 18, 33]
def lines(mk):
    n = sum(all(card[i][j] in mk for j in range(5)) for i in range(5)) + sum(all(card[j][i] in mk for j in range(5)) for i in range(5))
    n += all(card[i][i] in mk for i in range(5)); n += all(card[i][4 - i] in mk for i in range(5)); return n
mk = {0}
for i, n in enumerate(calls):
    mk.add(n); hit = "marked" if any(n in r for r in card) else "not on card"; l = lines(mk)
    print(f"call {i + 1}: {n} {hit}")
    if l > 0: print(f"bingo after {i + 1} calls ({l} line)"); break
