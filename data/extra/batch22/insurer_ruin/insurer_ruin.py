def ruined(capital, seed):
    sizes = [50, 100, 150, 250, 400]
    x = seed
    fund = capital
    for _ in range(50):
        fund += 110
        x = (x * 1103515245 + 12345) % 2147483648
        roll = (x >> 16) % 10
        if roll >= 5:
            fund -= sizes[roll - 5]
        if fund < 0:
            return True
    return False

print("expected claims 95 a period against 110 of premium")
for capital in [0, 100, 300, 600, 1000]:
    count = sum(1 for run in range(400) if ruined(capital, run * 7919 + 1))
    print(f"start {capital:>4}: ruined in {count:>3} of 400 runs ({count * 100 // 400}%)")
