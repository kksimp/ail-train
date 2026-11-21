def year(st, quota):
    growth = st[1] * st[0] * (1.0 - st[0] / st[2])
    available = st[0] + growth
    caught = quota if quota < available else available
    st[0] = st[0] + growth - caught
    return caught

r = 0.4
k = 10000.0
msy = r * k / 4.0
print(f"maximum sustainable yield {msy:.0f} t a year at a biomass of {k / 2.0:.0f} t")
for quota in [600.0, 900.0, 1000.0, 1100.0, 1400.0]:
    s = [6000.0, r, k]
    landed = 0.0
    collapsed = -1
    for y in range(1, 41):
        landed += year(s, quota)
        if s[0] < 1.0 and collapsed < 0:
            collapsed = y
    status = f"collapsed in year {collapsed}" if collapsed > 0 else f"biomass {s[0]:.0f} t after 40 years"
    print(f"quota {quota:>6.0f} t: {status}, landed {landed:.0f} t in all")
