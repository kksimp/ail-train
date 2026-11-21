def hc(c): return sum({"A": 4, "K": 3, "Q": 2, "J": 1}.get(x, 0) for x in c)
for h in ["AKJ4.Q83.K962.75", "Q7.AJ10953.A4.K82", "8642.973.J85.Q64", "AKQ.KQJ.AQ7.KJ104", "KQ98754..A93.J82"]:
    S = h.split("."); hi = sum(hc(s) for s in S); L = [len(s.replace("10", "T")) for s in S]; sh = sum(3 if n == 0 else 2 if n == 1 else 1 if n == 2 else 0 for n in L); t = hi + sh
    print(f"{h}: {hi} hcp + {sh} shape = {t}, {'-'.join(map(str, L))}, {'2 clubs' if hi >= 22 else 'one of a suit' if t >= 12 else 'pass'}")
