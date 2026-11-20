def area(s):
    k = s[0]
    if k == "circle":
        return 3 * s[1] * s[1]
    if k == "rect":
        return s[1] * s[2]
    if k == "line":
        return 0
    return area(s[1]) + s[2]

def label(s):
    k = s[0]
    if k == "circle":
        return "circle"
    if k == "rect":
        return "square" if s[1] == s[2] else "rectangle"
    if k == "line":
        return f"line of {s[1]}"
    if s[1][0] == "line":
        return "framed line"
    return "framed " + label(s[1])

shapes = [("circle", 2), ("rect", 3, 3), ("rect", 2, 5), ("line", 7),
          ("framed", ("rect", 4, 4), 2), ("framed", ("line", 1), 1)]
total = 0
for s in shapes:
    print(f"{label(s)}: {area(s)}")
    total += area(s)
print(f"total {total}")
print(sum(1 for s in shapes if label(s) == "square"))
