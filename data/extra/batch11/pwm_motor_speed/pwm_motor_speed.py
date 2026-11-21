def register(duty):
    return duty * 255 // 100
supply = 12.0
kv = 850.0
winding_drop = 1.5 * 0.8
period_ns = 50000
for duty in [0, 10, 25, 50, 75, 100]:
    avg = supply * float(duty) / 100.0
    on_ns = period_ns * duty // 100
    left = avg - winding_drop
    rpm = int(kv * left) if left > 0.0 else 0
    print(f"duty {duty:>3}%: register {register(duty):>3}, on {on_ns:>5} ns, average {avg:>5.2f} V, {rpm:>5} rpm")
print(f"the motor starts turning above {winding_drop / supply * 100.0:.1f}% duty")
