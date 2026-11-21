import math
a_rate = 0.012; b_rate = 0.006
a = 900.0; b = 1200.0
a_power = a_rate * a * a; b_power = b_rate * b * b
print(f"fighting strength A {a_power:.1f}, B {b_power:.1f}")
dt = 0.5; steps = 0
while a > 0.0 and b > 0.0:
    da = b_rate * b * dt
    db = a_rate * a * dt
    a -= da; b -= db
    steps += 1
    if steps % 40 == 0:
        print(f"hour {steps // 2:>3}: A {a:.1f}, B {b:.1f}")
predicted = math.sqrt((a_power - b_power) / a_rate)
winner = "A" if a > 0.0 else "B"
left = a if a > 0.0 else b
print(f"{winner} wins after {steps} half hours with {left:.1f} left; the law predicts {predicted:.1f}")
