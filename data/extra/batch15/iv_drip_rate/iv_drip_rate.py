def drops(o): return (o[1] * o[3] * 2 + o[2]) // (2 * o[2])
def clock(m):
    t = m % 1440
    return f"{t // 60:02}:{t % 60:02}"
orders = [("saline 0.9%", 1000, 480, 20, 8 * 60), ("glucose 5%", 500, 240, 15, 13 * 60 + 30), ("antibiotic", 100, 30, 20, 18 * 60), ("child maintenance", 250, 600, 60, 21 * 60)]
for o in orders:
    gtt = drops(o)
    per_hour = o[1] * 60 // o[2]
    print(f"{o[0]:<18} {o[1]:>5} mL over {o[2] // 60}h{o[2] % 60:02}: {gtt:>3} drops/min ({o[3]} gtt/mL), pump {per_hour} mL/h, {clock(o[4])} to {clock(o[4] + o[2])}")
micro = len([o for o in orders if o[3] == 60])
print(f"{micro} order uses a micro-drip set")
