import math

def secs(t):
    total = 0
    for p in t.split(":"):
        total = total * 60 + int(p)
    return total

def clock(s):
    return f"{s // 60}:{str(s % 60).rjust(2, '0')}"

def factor(age):
    ages = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    table = [1.0, 0.9921, 0.9668, 0.9406, 0.9143, 0.8880, 0.8617, 0.8354, 0.8091, 0.7795]
    if age <= 30:
        return 1.0
    for i in range(len(ages) - 1):
        if age <= ages[i + 1]:
            t = (age - ages[i]) / 5.0
            return table[i] + (table[i + 1] - table[i]) * t
    return table[-1]

open_standard = 1571.0
runners = [("Abe", 28, "41:20"), ("Bina", 44, "44:05"), ("Carl", 57, "46:30"), ("Dora", 63, "52:10"), ("Emil", 71, "58:45"), ("Fern", 36, "37:15")]
for name, age, time in runners:
    f = factor(age)
    actual = float(secs(time))
    grade = open_standard / f / actual * 100.0
    if grade >= 90.0:
        level = "world class"
    elif grade >= 80.0:
        level = "national"
    elif grade >= 70.0:
        level = "regional"
    elif grade >= 60.0:
        level = "local"
    else:
        level = "recreational"
    graded = int(math.floor(actual * f + 0.5))
    print(f"{name:<5} {age} {time}  factor {f:.4f}  grade {grade:>5.1f}%  {level:<12} graded {clock(graded)}")
