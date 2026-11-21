def multiplier(mpc, tax):
    return 1.0 / (1.0 - mpc * (1.0 - tax))
injection = 100.0
mpc = 0.8
tax = 0.25
round_amount = injection
total = 0.0
for n in range(1, 9):
    total += round_amount
    print(f"round {n}: spent {round_amount:>6.2f}, total {total:>6.2f}")
    round_amount = round_amount * mpc * (1.0 - tax)
limit = injection * multiplier(mpc, tax)
print(f"limit {limit:.2f} (multiplier {multiplier(mpc, tax):.2f})")
for m, t in [(0.9, 0.0), (0.9, 0.3), (0.6, 0.2)]:
    print(f"MPC {m}, tax {t}: multiplier {multiplier(m, t):.3f}")
