def clean(text):
    out = []
    for w in text.lower().split(" "):
        w2 = "".join(c for c in w if c.isalpha())
        if w2 != "":
            out.append(w2)
    return out

def ttr(ws):
    return len(set(ws)) / len(ws)

def mattr(ws, size):
    if len(ws) < size:
        return ttr(ws)
    total = 0.0
    count = 0
    for i in range(len(ws) - size + 1):
        total += ttr(ws[i:i + size])
        count += 1
    return total / count

texts = [("nursery", "the cat sat on the mat and the cat saw the rat and the rat ran from the cat"), ("weather", "grey clouds gathered over distant hills while cold wind pushed rain across empty fields toward town"), ("speech", "we will build and we will grow and we will win because we will never stop trying")]
for name, body in texts:
    ws = clean(body)
    print(f"{name:<8} {len(ws):>2} words, ttr {ttr(ws):.3f}, moving ttr {mattr(ws, 8):.3f}")
short = clean("the cat sat on the mat")
print(f"first six nursery words alone: ttr {ttr(short):.3f}")
