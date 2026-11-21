def balance(r1, r2, r3):
    return r3 * r2 / r1
def bridge_out(volts, r, rx):
    return volts * (rx / (r + rx) - 0.5)
print(f"balance with 1000 / 2200 / 470: Rx = {balance(1000.0, 2200.0, 470.0):.1f} ohm")
print(f"balance with 330 / 1000 / 150: Rx = {balance(330.0, 1000.0, 150.0):.1f} ohm")
gauge = 350.0
for micro in [0, 100, 500, 1000, 2000]:
    strain = float(micro) / 1000000.0
    rx = gauge * (1.0 + 2.0 * strain)
    mv = bridge_out(5.0, gauge, rx) * 1000.0
    print(f"{micro:>5} microstrain: gauge {rx:.3f} ohm, output {mv:.3f} mV")
