import math

def kelly(p, b):
    return (b * p - (1.0 - p)) / b

def growth(p, f):
    return p * math.log(1.0 + f) + (1.0 - p) * math.log(1.0 - f)

p = 0.55
f = kelly(p, 1.0)
print(f"Kelly fraction {f:.3f}")
for halves in [1, 2, 4]:
    stake = f * float(halves) / 2.0
    wealth = 100.0
    seed = 2024
    wins = 0
    low = 100.0
    for _ in range(300):
        seed = (seed * 1103515245 + 12345) % 2147483648
        bet = wealth * stake
        if (seed >> 16) % 100 < 55:
            wealth += bet
            wins += 1
        else:
            wealth -= bet
        low = min(low, wealth)
    g = growth(p, stake) * 100.0
    print(f"stake {stake:.2f}: expected growth {g:.3f}% a bet, {wins} wins, lowest {low:.2f}, final {wealth:.2f}")
