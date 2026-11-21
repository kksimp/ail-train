line = [("Depot", 0, 30, True), ("Market", 95, 25, False), ("Bridge", 120, 30, True), ("Park", 80, 20, False), ("College", 100, 40, True), ("Mill", 90, 20, False), ("Terminus", 110, 0, True)]

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

def times(express):
    t = 0
    out = []
    for i, s in enumerate(line):
        t += s[1]
        if express and not s[3]:
            t -= 20
            out.append(-1)
        else:
            out.append(t)
            if i < len(line) - 1:
                t += s[2]
    return out

def show(t):
    return "-" if t < 0 else mmss(t)

slow = times(False)
fast = times(True)
print("stop       all  express")
for i, s in enumerate(line):
    print(f"{s[0]:<9} {show(slow[i]):>5} {show(fast[i]):>8}")
print(f"express saves {mmss(slow[-1] - fast[-1])} end to end")
