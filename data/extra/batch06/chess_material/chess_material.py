V = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9}
for b in ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", "r3k2r/ppp2ppp/8/3q4/8/8/PPP2PPP/R2QK2R", "8/5k2/8/8/2B5/8/4PK2/8", "4k3/8/8/8/8/8/8/3QK3"]:
    w = sum(V.get(c.lower(), 0) for c in b if c.isupper()); k = sum(V.get(c, 0) for c in b if c.islower()); d = w - k
    print(f"white {w}, black {k}: {'white +' + str(d) if d > 0 else 'black +' + str(-d) if d < 0 else 'level'}")
