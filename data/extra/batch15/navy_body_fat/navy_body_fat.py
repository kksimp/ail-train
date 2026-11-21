import math
def body_fat(p):
    h = p[2] / 2.54; n = p[3] / 2.54; w = p[4] / 2.54; hip = p[5] / 2.54
    if p[1]:
        return 86.01 * math.log10(w - n) - 70.041 * math.log10(h) + 36.76
    return 163.205 * math.log10(w + hip - n) - 97.684 * math.log10(h) - 78.387
people = [("Arun", True, 178.0, 39.0, 86.0, 0.0, 78.0), ("Ben", True, 185.0, 41.5, 101.0, 0.0, 96.0), ("Chloe", False, 165.0, 32.0, 71.0, 97.0, 61.0), ("Dana", False, 170.0, 34.0, 84.0, 106.0, 77.0)]
for p in people:
    bf = body_fat(p)
    fat = p[6] * bf / 100.0
    lean = p[6] - fat
    print(f"{p[0]:<6} {bf:>5.1f}% body fat: {fat:>5.1f} kg fat, {lean:>5.1f} kg lean")
