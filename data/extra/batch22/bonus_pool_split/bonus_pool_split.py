def money(c):
    return f"{c // 100}.{c % 100:02d}"

mult = [0, 50, 100, 125, 150]
pool = 5000000
staff = [["Ines", 62000, 4, 0], ["Tom", 48000, 3, 0], ["Wu", 75000, 5, 0], ["Pia", 54000, 2, 0], ["Sam", 39000, 3, 0], ["Eve", 58000, 1, 0]]
wt = sum(s[1] * mult[s[2] - 1] for s in staff)
given = 0
for s in staff:
    s[3] = pool * (s[1] * mult[s[2] - 1]) // wt
    given += s[3]
top = 0
for i in range(len(staff)):
    if staff[i][2] > staff[top][2]:
        top = i
left = pool - given
staff[top][3] += left
print(f"{left} cents left over go to {staff[top][0]}")
for p in sorted(staff, key=lambda x: -x[3]):
    bp = p[3] * 100 // p[1]
    print(f"{p[0]:<5} rating {p[2]}: {money(p[3]):>9} ({bp // 100}.{bp % 100:02d}% of salary)")
