import math
PI = 3.141592653589793
MU0 = 0.0000012566370614

def solenoid(turns, length, amps):
    return MU0 * float(turns) / length * amps

def wire(amps, r):
    return MU0 * amps / (2.0 * PI * r)

def turns_for(target, length, amps):
    return int(math.ceil(target * length / (MU0 * amps)))

for t in [200, 500, 1000]:
    b = solenoid(t, 0.2, 2.0) * 1000.0
    print(f"{t:>4} turns on 20 cm at 2 A: {b:.2f} mT")
need = turns_for(0.05, 0.2, 2.0)
print(f"50 mT at 2 A needs {need} turns")
earth = 0.00005
for amps in [1.0, 10.0, 100.0]:
    reach = MU0 * amps / (2.0 * PI * earth)
    near = wire(amps, 0.01) * 1000000.0
    print(f"wire at {amps:.0f} A: {near:.0f} uT at 1 cm, equals the Earth's field at {reach * 100.0:.1f} cm")
