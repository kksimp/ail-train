def bar(n, top):
    return "#" * ((n * 20 + top // 2) // top)

bands = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]
men = [612, 640, 701, 688, 652, 598, 470, 301, 98]
women = [585, 611, 690, 694, 671, 623, 512, 382, 196]
top = max(max(men), max(women))
for i in reversed(range(len(bands))):
    left = bar(men[i], top).rjust(20, ' ')
    right = bar(women[i], top)
    ratio = men[i] * 100 // women[i]
    print(f"{left} {bands[i]:^7} {right} ({ratio})")
total = sum(men) + sum(women)
seen = 0
median = ""
for i in range(len(bands)):
    seen += men[i] + women[i]
    if median == "" and seen * 2 >= total:
        median = bands[i]
print(f"{total} thousand people, median age band {median}, overall {sum(men) * 100 // sum(women)} men per 100 women")
