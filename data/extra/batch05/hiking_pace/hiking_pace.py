import math
def rd(x): return int(math.floor(abs(x) + 0.5)) * (1 if x >= 0 else -1)
L = [("car park to bridge", 3.2, 120), ("bridge to ridge", 4.5, 540), ("ridge to summit", 2.1, 310), ("summit to tarn", 3.8, 0), ("tarn to car park", 5.4, 60)]
t = 8 * 60 + 15; k = 0.0; u = 0
for n, km, up in L:
    m = rd(km / 5.0 * 60.0 + up / 600.0 * 60.0); t += m; k += km; u += up
    print(f"{n:<20} {km:>4.1f} km {up:>4} m  {m:>3} min, at {t // 60:02}:{t % 60:02}")
print(f"total {k:.1f} km, {u} m climb, finish {t // 60:02}:{t % 60:02}")
