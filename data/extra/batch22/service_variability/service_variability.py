def queue_len(lam, mean, var):
    r = lam * mean
    return (lam * lam * var + r * r) / (2.0 * (1.0 - r))

lam = 0.8
print("arrivals 0.8 a minute, service 1 minute on average")
for name, var in [("fixed", 0.0), ("two-phase", 0.5), ("exponential", 1.0), ("very uneven", 4.0)]:
    lq = queue_len(lam, 1.0, var)
    wq = lq / lam
    total = lq + lam
    print(f"{name:<12} variance {var:.1f}: waiting {lq:.3f}, wait {wq:.3f} min, in system {total:.3f}")
for load in [5, 7, 9]:
    l = float(load) / 10.0
    a = queue_len(l, 1.0, 0.0)
    b = queue_len(l, 1.0, 1.0)
    print(f"load 0.{load}: fixed {a:.3f} against exponential {b:.3f}")
