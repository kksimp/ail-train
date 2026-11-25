import sys

# nodes: 0 is the sentinel; prv/nxt circular
prv = [0]
nxt = [0]
val = [""]
cur = 0

for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c == "ins" and len(w) == 2:
        prv.append(0)
        nxt.append(0)
        val.append(w[1])
        n = len(val) - 1
        p = prv[cur]
        nxt[p] = n
        prv[n] = p
        nxt[n] = cur
        prv[cur] = n
        print("ok")
    elif c == "del" and len(w) == 1:
        if cur == 0:
            print("nothing")
        else:
            p, n = prv[cur], nxt[cur]
            nxt[p] = n
            prv[n] = p
            print(val[cur])
            cur = n
    elif c == "left" and len(w) == 1:
        if prv[cur] == 0:
            print("edge")
        else:
            cur = prv[cur]
            print("ok")
    elif c == "right" and len(w) == 1:
        if cur == 0:
            print("edge")
        else:
            cur = nxt[cur]
            print("ok")
    elif c == "home" and len(w) == 1:
        cur = nxt[0]
        print("ok")
    elif c == "end" and len(w) == 1:
        cur = 0
        print("ok")
    elif c == "show" and len(w) == 1:
        out = []
        n = nxt[0]
        while n != 0:
            out.append("[" + val[n] + "]" if n == cur else val[n])
            n = nxt[n]
        if cur == 0:
            out.append("|")
        print(" ".join(out))
    elif c == "rshow" and len(w) == 1:
        out = []
        n = prv[0]
        while n != 0:
            out.append(val[n])
            n = prv[n]
        print(" ".join(out) if out else "empty")
    else:
        print("error")
