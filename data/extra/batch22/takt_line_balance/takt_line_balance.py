jobs = [("A", 45, []), ("B", 30, ["A"]), ("C", 25, ["A"]), ("D", 40, ["B"]), ("E", 20, ["B", "C"]), ("F", 35, ["C"]), ("G", 30, ["D", "E"]), ("H", 15, ["F", "G"])]
takt = 28800 // 480
done = set()
stations = 0
while len(done) < len(jobs):
    stations += 1
    left = takt
    names = []
    while True:
        pick = -1
        for i, (name, secs, preds) in enumerate(jobs):
            ready = all(p in done for p in preds)
            if name not in done and ready and secs <= left:
                if pick == -1 or secs > jobs[pick][1]:
                    pick = i
        if pick == -1:
            break
        done.add(jobs[pick][0])
        names.append(jobs[pick][0])
        left -= jobs[pick][1]
    print(f"station {stations}: {' '.join(names)}, idle {left} s")
work = sum(j[1] for j in jobs)
least = (work + takt - 1) // takt
eff = work * 1000 // (stations * takt)
print(f"takt {takt} s, work {work} s: {stations} stations (at least {least}), efficiency {eff // 10}.{eff % 10}%")
