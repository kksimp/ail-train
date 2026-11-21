import math
def modulus(b): return b[1] * b[2] * b[2] / 6.0
def stress(b, w, span):
    moment = w * span * span / 8.0
    return moment / modulus(b)
def max_span(b, w): return math.sqrt(8.0 * b[3] * modulus(b) / w)
w = 0.36; span = 900.0
boards = [("pine 18 mm", 250.0, 18.0, 7.0), ("oak 20 mm", 250.0, 20.0, 11.0), ("MDF 18 mm", 250.0, 18.0, 4.0), ("chipboard 15 mm", 250.0, 15.0, 3.0)]
print(f"books at {w:.2f} N/mm over {span:.0f} mm")
for b in boards:
    s = stress(b, w, span)
    verdict = "ok" if s <= b[3] else "too weak"
    print(f"{b[0]:<16} {s:.2f} MPa of {b[3]:.1f} allowed: {verdict}, max span {max_span(b, w):.0f} mm")
