def report(n, t, c):
    tp = sum(1 for i in range(len(t)) if c[i] == 1 and t[i] == 1); fp = sum(1 for i in range(len(t)) if c[i] == 1 and t[i] == 0)
    fn = sum(1 for i in range(len(t)) if c[i] == 0 and t[i] == 1); tn = len(t) - tp - fp - fn
    acc = (tp + tn) / len(t); pr = tp / (tp + fp); rc = tp / (tp + fn); f1 = 2.0 * pr * rc / (pr + rc)
    print(f"{n}: TP {tp} FP {fp} TN {tn} FN {fn}")
    print(f"  accuracy {acc:.3f}, precision {pr:.3f}, recall {rc:.3f}, F1 {f1:.3f}")
t = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
report("cautious", t, [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
report("eager", t, [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])
