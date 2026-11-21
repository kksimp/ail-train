def signature(report):
    frames = [f.split(":")[0] for f in report.split(";")]
    return f"{frames[0]} < {frames[1]}"

reports = ["parse@json.py:12;load@config.py:40;main@app.py:5", "parse@json.py:14;load@config.py:40;main@app.py:5", "send@net.py:88;flush@queue.py:20;worker@app.py:30", "parse@json.py:12;load@config.py:41;reload@app.py:60", "div@math.py:3;ratio@stats.py:9;report@app.py:70", "send@net.py:90;flush@queue.py:20;worker@app.py:30", "send@net.py:88;retry@queue.py:25;worker@app.py:30"]
counts = {}
tops = {}
seen = set()
for r in reports:
    sig = signature(r)
    counts[sig] = counts.get(sig, 0) + 1
    top = r.split(";")[0]
    key = f"{sig}|{top}"
    if key not in seen:
        seen.add(key)
        tops[sig] = tops.get(sig, 0) + 1
order = sorted(counts.keys(), key=lambda k: -counts[k])
for sig in order:
    print(f"{counts[sig]}x {sig:<28} {tops[sig]} distinct top lines")
print(f"{len(reports)} crashes, {len(counts)} signatures")
print(f"fix first: {order[0]}")
