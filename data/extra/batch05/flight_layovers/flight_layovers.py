F = [("BHX", "AMS", "07:10", "09:20"), ("AMS", "OSL", "09:50", "11:45"), ("AMS", "OSL", "10:20", "12:15"), ("BHX", "CPH", "08:00", "10:55"), ("CPH", "OSL", "11:30", "12:40"), ("CPH", "OSL", "11:20", "12:30"), ("BHX", "OSL", "13:00", "16:10"), ("AMS", "OSL", "12:05", "14:00")]
def m(t): h, mi = t.split(":"); return int(h) * 60 + int(mi)
T = []
for a in F:
    if a[0] != "BHX": continue
    if a[1] == "OSL": T.append((m(a[3]), f"direct {a[2]}-{a[3]}")); continue
    for b in F:
        if b[0] == a[1] and b[1] == "OSL":
            g = m(b[2]) - m(a[3])
            if g >= 45: T.append((m(b[3]), f"via {a[1]} {a[2]}-{a[3]}, {b[2]}-{b[3]} (wait {g} min)"))
for t in sorted(T): print(t[1])
