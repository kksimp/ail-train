import math

def lmtd(d1, d2):
    if d1 <= 0.0 or d2 <= 0.0:
        raise ValueError("temperature cross: the cold side would leave hotter than the hot side")
    if abs(d1 - d2) < 0.001:
        return d1
    return (d1 - d2) / math.log(d1 / d2)

u = 300.0
duties = [("oil cooler", 150.0, 90.0, 20.0, 60.0, 2.0), ("tight approach", 120.0, 70.0, 30.0, 95.0, 1.5)]
for name, hot_in, hot_out, cold_in, cold_out, flow in duties:
    q = flow * 2100.0 * (hot_in - hot_out)
    print(f"{name}: duty {q / 1000.0:.1f} kW")
    try:
        v = lmtd(hot_in - cold_out, hot_out - cold_in)
        print(f"  counterflow LMTD {v:.2f} K, area {q / (u * v):.2f} m2")
    except ValueError as err:
        print(f"  counterflow: {err}")
    try:
        v = lmtd(hot_in - cold_in, hot_out - cold_out)
        print(f"  parallel LMTD {v:.2f} K, area {q / (u * v):.2f} m2")
    except ValueError as err:
        print(f"  parallel: {err}")
