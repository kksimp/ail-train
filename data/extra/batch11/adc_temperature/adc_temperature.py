def to_code(volts, vref):
    code = int(volts / vref * 1024.0)
    return 1023 if code > 1023 else (0 if code < 0 else code)
def to_volts(code, vref):
    return float(code) * vref / 1024.0
vref = 3.3
step = vref / 1024.0 * 1000.0
print(f"one step is {step:.3f} mV")
for v in [0.0, 0.75, 1.65, 3.3, 3.5]:
    c = to_code(v, vref)
    back = to_volts(c, vref)
    print(f"{v:.2f} V -> code {c:>4} -> {back:.4f} V")
for code in [217, 232, 248, 261]:
    volts = to_volts(code, vref)
    temp = (volts - 0.5) * 100.0
    print(f"sensor code {code}: {temp:.1f} C")
