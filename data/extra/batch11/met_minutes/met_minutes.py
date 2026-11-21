import math
acts = [("yoga", 2.5), ("brisk walk", 4.3), ("swimming", 6.0), ("cycling", 8.0), ("running", 9.8)]
def per_minute(a, kg):
    return a[1] * 3.5 * kg / 200.0
for kg in [60.0, 80.0]:
    print(f"at {kg} kg:")
    for a in acts:
        half_hour = per_minute(a, kg) * 30.0
        need = int(math.ceil(300.0 / per_minute(a, kg)))
        print(f"  {a[0]:<10} {half_hour:>6.2f} kcal in 30 min, {need:>3} min for 300 kcal")
total = 0.0
for name, minutes in [("cycling", 45), ("yoga", 60), ("running", 30), ("swimming", 40)]:
    act = next((x for x in acts if x[0] == name), acts[0])
    total += per_minute(act, 75.0) * float(minutes)
print(f"a week for a 75 kg person: {total:.2f} kcal")
