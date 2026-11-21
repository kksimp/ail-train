booked = {"Maths": [False] * 12, "English": [True, True] + [False] * 10, "Science": [False] * 12, "Art": [False, True, False, True, False, False, False, False, False, False, True, True]}
families = [("Patel", ["Maths", "English", "Art"]), ("Okoye", ["English", "Maths"]), ("Smith", ["Art", "Science", "English"]), ("Ruiz", ["Maths", "Science", "Art"]), ("Kowal", ["Science", "Art", "Maths", "English"])]

def first_free(slots, frm):
    for i in range(frm, len(slots)):
        if not slots[i]:
            return i
    return -1

def at(slot):
    m = 16 * 60 + slot * 10
    return f"{m // 60:02d}:{m % 60:02d}"

for name, wants in families:
    nxt = 0
    parts = []
    for t in wants:
        s = first_free(booked[t], nxt)
        if s < 0:
            parts.append(f"{t} full")
            continue
        booked[t][s] = True
        parts.append(f"{t} {at(s)}")
        nxt = s + 1
    print(f"{name:<6} {', '.join(parts)}")
for t, slots in booked.items():
    print(f"{t}: {sum(1 for b in slots if b)} of 12 slots taken")
