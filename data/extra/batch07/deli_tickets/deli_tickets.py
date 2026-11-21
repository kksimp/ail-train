iss = 95; Q = []
for e in ["take", "take", "serve", "take", "take", "take", "serve", "serve", "take", "serve", "serve", "serve", "serve"]:
    if e == "take": iss = 1 if iss == 99 else iss + 1; Q.append(iss); print(f"ticket {iss} taken, {len(Q)} waiting")
    elif not Q: print("no one waiting")
    else: s = Q.pop(0); print(f"now serving {s}, {len(Q)} waiting")
