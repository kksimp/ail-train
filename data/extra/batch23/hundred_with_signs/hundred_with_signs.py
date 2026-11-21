def go(d, total, term, sign, text, out):
    if d == 10:
        if total + sign * term == 100:
            out.append(text)
        return
    go(d + 1, total, term * 10 + d, sign, f"{text}{d}", out)
    go(d + 1, total + sign * term, d, 1, f"{text}+{d}", out)
    go(d + 1, total + sign * term, d, -1, f"{text}-{d}", out)

out = []
go(2, 0, 1, 1, "1", out)
for s in out:
    print(f"{s} = 100")
print(f"{len(out)} ways out of 6561")
