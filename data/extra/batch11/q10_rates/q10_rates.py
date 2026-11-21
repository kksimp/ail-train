def q10(r1, t1, r2, t2):
    return (r2 / r1) ** (10.0 / (t2 - t1))
trials = [("frog heart, beats/min", 15.0, 22.0, 25.0, 41.0), ("seed respiration, uL/h", 10.0, 3.2, 20.0, 7.0), ("enzyme, umol/min", 20.0, 1.5, 35.0, 4.4)]
for name, t1, r1, t2, r2 in trials:
    q = q10(r1, t1, r2, t2)
    preds = []
    for t in [5.0, 30.0]:
        rate = r1 * q ** ((t - t1) / 10.0)
        preds.append(f"{t} C: {rate:.1f}")
    joined = ", ".join(preds)
    print(f"{name}: Q10 {q:.2f}; {joined}")
