import math
C = {"London": (51.5074, -0.1278), "Paris": (48.8566, 2.3522), "Berlin": (52.52, 13.405), "Rome": (41.9028, 12.4964), "Madrid": (40.4168, -3.7038)}
def rd(d): return d * 3.141592653589793 / 180.0
def hv(a, b):
    s1 = math.sin(rd(b[0] - a[0]) / 2.0); s2 = math.sin(rd(b[1] - a[1]) / 2.0); h = s1 * s1 + math.cos(rd(a[0])) * math.cos(rd(b[0])) * s2 * s2
    return 2.0 * 6371.0 * math.atan2(math.sqrt(h), math.sqrt(1.0 - h))
R = ["London", "Paris", "Madrid", "Rome", "Berlin", "London"]; t = 0.0
for i in range(1, len(R)): d = hv(C[R[i - 1]], C[R[i]]); t += d; print(f"{R[i - 1]} -> {R[i]}: {d:.0f} km")
print(f"route total: {t:.0f} km")
