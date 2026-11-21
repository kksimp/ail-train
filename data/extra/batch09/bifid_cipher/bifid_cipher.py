def encrypt(sq, msg):
    rows = []
    cols = []
    for c in msg:
        at = sq.index('I' if c == 'J' else c)
        rows.append(at // 5)
        cols.append(at % 5)
    stream = rows + cols
    return "".join(sq[stream[2 * k] * 5 + stream[2 * k + 1]] for k in range(len(msg)))

def decrypt(sq, code):
    stream = []
    for c in code:
        at = sq.index(c)
        stream.append(at // 5)
        stream.append(at % 5)
    n = len(code)
    return "".join(sq[stream[k] * 5 + stream[n + k]] for k in range(n))

square = "BGWKZQPNDSIOAXEFCLUMTHYVR"
for r in range(5):
    print(square[r * 5:r * 5 + 5])
for msg in ["FLEEATONCE", "DEFENDTHEHILL", "BIFID"]:
    code = encrypt(square, msg)
    print(f"{msg:<13} -> {code:<13} -> {decrypt(square, code)}")
