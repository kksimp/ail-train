t = 287; r = b = 0
for x in [31, 24, 42, 28, 19, 33, 37, 22, 26, 22]:
    r += x; b += 30; l = 300 - b; nd = t - r; cu = r * 6.0 / b; o = f"{b // 6}.{b % 6}"
    if nd <= 0: print(f"{o} overs: {r} - target reached"); break
    if l == 0: print(f"{o} overs: {r} - lost by {nd - 1} runs"); break
    rq = nd * 6.0 / l; print(f"{o} overs: {r}, rate {cu:.2f}, need {nd} at {rq:.2f}, {'ahead' if cu >= rq else 'behind'}")
