N = ["GBP", "EUR", "USD", "JPY"]; R = [10000, 11650, 12710, 191300]
def cv(a, f, t): return (a * t * 2 + f) // (f * 2)
print("100 of  " + "".join(f"{n:>9}" for n in N))
for i in range(4): print(f"{N[i]:<7} " + "".join(f"{cv(10000, R[i], R[j]) // 100:>6}.{cv(10000, R[i], R[j]) % 100:02}" for j in range(4)))
