def dm(t):
    n = ord(t) - 65; r = []
    for i in range(n + 1):
        c = chr(65 + i); o = " " * (n - i); r.append(o + c + o if i == 0 else o + c + " " * (2 * i - 1) + c + o)
    return r + r[:-1][::-1]
for t in "CE":
    for r in dm(t): print(f"|{r}|")
    print("")
