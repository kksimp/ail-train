V = [1180, 1240, 1310, 1290, 1405, 1460, 1440, 1555, 1610, 1590, 1700, 1760]; n = float(len(V)); X = [i + 1.0 for i in range(len(V))]; Y = [float(v) for v in V]
mx = sum(X) / n; my = sum(Y) / n; sxy = sxx = syy = 0.0
for i in range(len(V)): dx = X[i] - mx; dy = Y[i] - my; sxy += dx * dy; sxx += dx * dx; syy += dy * dy
sl = sxy / sxx; ic = my - sl * mx; print(f"visits = {sl:.3f} * month + {ic:.3f}, r^2 {sxy * sxy / (sxx * syy):.4f}")
for m in range(13, 16): print(f"month {m}: about {sl * m + ic:.0f}")
