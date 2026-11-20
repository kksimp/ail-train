people = [("Ana", 52.0, 165.0), ("Raj", 81.5, 178.0), ("Lu", 95.0, 170.0), ("Kim", 70.0, 182.0), ("Ole", 49.0, 172.0)]
def bmi(kg, cm):
    m = cm / 100.0
    return kg / (m * m)
def band(v):
    return "under" if v < 18.5 else "healthy" if v < 25.0 else "over" if v < 30.0 else "obese"
tot = 0.0
for n, kg, cm in people:
    v = bmi(kg, cm); tot += v
    print(f"{n:<4}{kg:>6.1f}kg {cm:>4.0f}cm  bmi {v:>5.1f} {band(v)}")
print(f"mean bmi {tot / len(people):.2f}")
print("healthy: " + ", ".join(n for n, kg, cm in people if band(bmi(kg, cm)) == "healthy"))
