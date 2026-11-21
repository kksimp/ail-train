def avail(mtbf, mttr):
    return mtbf / (mtbf + mttr)

def parallel(a):
    down = 1.0 - a
    return 1.0 - down * down

pump = avail(1200.0, 24.0)
control = avail(5000.0, 8.0)
valve = avail(2500.0, 12.0)
print(f"pump {pump:.5f}, controller {control:.5f}, valve {valve:.5f}")
single = pump * control * valve
double = parallel(pump) * control * valve
for name, a in [("one pump", single), ("two pumps", double)]:
    hours = (1.0 - a) * 8760.0
    print(f"{name:<9}: available {a:.5f}, down about {hours:.1f} hours a year")
