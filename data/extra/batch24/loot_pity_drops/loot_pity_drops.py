state = 4096
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def bucket(k):
    if 1 <= k <= 10: return "1-10"
    if 11 <= k <= 20: return "11-20"
    if 21 <= k <= 29: return "21-29"
    return "30 (pity)"
groups = {n: 0 for n in ["1-10", "11-20", "21-29", "30 (pity)"]}
streak = 0; rares = 0; kills = 0
while rares < 200:
    kills += 1; streak += 1
    if streak >= 30 or below(100) < 4:
        groups[bucket(streak)] += 1
        rares += 1; streak = 0
for name, n in groups.items():
    print(f"{name:<9} {n:>3} {'#' * (n // 4)}")
mean = kills / rares
print(f"{rares} rares in {kills} kills, {mean:.3f} kills each")
