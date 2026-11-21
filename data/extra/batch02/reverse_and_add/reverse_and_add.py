def stp(n, lim):
    v = n
    for s in range(1, lim + 1):
        v = v + int(str(v)[::-1])
        if str(v) == str(v)[::-1]: return s, str(v)
    return None
for n in [56, 57, 59, 89, 10, 196, 295]:
    r = stp(n, 60)
    print(f"{n}: {r[0]} steps -> {r[1]}" if r else f"{n}: no palindrome in 60 steps")
print("candidates below 300: " + " ".join(str(n) for n in range(1, 300) if stp(n, 60) is None))
