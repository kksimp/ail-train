import math
def boil_minutes(grams, egg_c, water_c, yolk_c):
    ratio = 0.76 * (egg_c - water_c) / (yolk_c - water_c)
    return 0.451 * grams ** (2.0 / 3.0) * math.log(ratio)
def clock(minutes):
    whole = int(minutes)
    secs = int((minutes - float(whole)) * 60.0)
    return f"{whole}:{secs:02}"
for name, grams in [("small", 48.0), ("medium", 58.0), ("large", 68.0)]:
    soft = boil_minutes(grams, 4.0, 100.0, 63.0)
    firm = boil_minutes(grams, 4.0, 100.0, 70.0)
    warm = boil_minutes(grams, 21.0, 100.0, 63.0)
    print(f"{name:<6} {grams} g: soft {clock(soft)}, firm {clock(firm)}, soft from room temperature {clock(warm)}")
high = boil_minutes(58.0, 4.0, 90.0, 63.0)
print(f"medium soft egg where water boils at 90 C: {clock(high)}")
