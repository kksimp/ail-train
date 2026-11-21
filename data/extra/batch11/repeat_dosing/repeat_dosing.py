import math
dose_mg = 500.0
volume_l = 40.0
half_life = 6.0
tau = 8.0
two = 2.0
k = math.log(two) / half_life
keep = math.exp(0.0 - k * tau)
step = dose_mg / volume_l
level = 0.0
for n in range(1, 7):
    level += step
    trough = level * keep
    print(f"dose {n}: peak {level:.2f} mg/L, before next {trough:.2f} mg/L")
    level = trough
peak_ss = step / (1.0 - keep)
trough_ss = peak_ss * keep
print(f"steady state: peak {peak_ss:.2f} mg/L, trough {trough_ss:.2f} mg/L")
print(f"{keep * 100.0:.1f}% of each level remains after {tau} h")
