days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week = [("R", 4), ("S", 9), ("W", 25, 40), ("W", 55, 95), ("F",), ("S", 2), ("R", 28)]
def advice(s):
    k = s[0]
    if k == "R": return "heavy rain, stay in" if s[1] >= 20 else "take an umbrella"
    if k == "S":
        if s[1] >= 8: return "very high UV, hat and shade"
        if s[1] >= 3: return "wear sunscreen"
        return "fine day"
    if k == "W":
        if s[2] >= 80: return "gale, secure the bins"
        return f"breezy at {s[1]} km/h"
    return "fog, drive slowly"
def outdoor(s):
    if s[0] == "S": return True
    if s[0] == "W": return s[1] < 30
    if s[0] == "R": return s[1] < 2
    return False
for i, s in enumerate(week):
    print(f"{days[i]}: {advice(s)}")
print("picnic days: " + " ".join(days[i] for i in range(7) if outdoor(week[i])))
