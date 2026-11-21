def loss_watts(power, volts, ohms):
    amps = power / volts
    return amps * amps * ohms
power = 10000000.0
ohms = 0.1 * 50.0
print(f"sending 10 MW over 50 km of line ({ohms} ohm)")
for kv in [11, 33, 132, 400]:
    volts = float(kv) * 1000.0
    amps = power / volts
    loss = loss_watts(power, volts, ohms)
    pct = loss / power * 100.0
    kw = loss / 1000.0
    print(f"{kv:>4} kV: {amps:>7.1f} A, loss {kw:>9.1f} kW ({pct:.3f}%)")
ratio = loss_watts(power, 11000.0, ohms) / loss_watts(power, 110000.0, ohms)
print(f"ten times the voltage: {ratio:.1f} times less loss")
