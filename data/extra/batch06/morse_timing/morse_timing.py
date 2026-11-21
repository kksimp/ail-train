L = "abcdefghijklmnopqrstuvwxyz"; C = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
def un(t):
    tot = 0
    for wi, w in enumerate(t.split(" ")):
        if wi: tot += 7
        for li, c in enumerate(w):
            if li: tot += 3
            for si, s in enumerate(C[L.index(c)]):
                if si: tot += 1
                tot += 1 if s == "." else 3
    return tot
for t in ["sos", "paris", "hello world", "e", "t"]: print(f"{t}: " + " / ".join(" ".join(C[L.index(c)] for c in w) for w in t.split(" ")) + f" = {un(t)} units")
