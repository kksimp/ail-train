def ceil_div(a, b): return (a + b - 1) // b
trials = [("statin, heart attack", 81, 2000, 52, 2000), ("aspirin, stroke", 46, 1500, 38, 1520), ("antiviral, admission", 61, 600, 25, 610), ("sedative, falls", 12, 800, 29, 790)]
for name, ce, cn, te, tn in trials:
    cer = float(ce) / float(cn)
    eer = float(te) / float(tn)
    num = ce * tn - te * cn
    den = cn * tn
    if num > 0:
        arr = cer - eer
        print(f"{name:<21} {cer * 100.0:.2f}% -> {eer * 100.0:.2f}%: ARR {arr * 100.0:.2f} points, RRR {arr / cer * 100.0:.1f}%, NNT {ceil_div(den, num)}")
    else:
        print(f"{name:<21} {cer * 100.0:.2f}% -> {eer * 100.0:.2f}%: harm, NNH {ceil_div(den, -num)}")
