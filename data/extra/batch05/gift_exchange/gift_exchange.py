P = ["Ani", "Bo", "Cleo", "Dev", "Eun", "Fox"]; Pa = [("Ani", "Bo"), ("Cleo", "Dev")]
def dr(seed):
    ix = list(range(6)); s = seed; i = 5
    while i > 0:
        s = (s * 1103515245 + 12345) % 2147483648; j = (s // 65536) % (i + 1); ix[i], ix[j] = ix[j], ix[i]; i -= 1
    return ix
sd = 1
while True:
    d = dr(sd)
    if all(P[k] != P[d[k]] and (P[k], P[d[k]]) not in Pa and (P[d[k]], P[k]) not in Pa for k in range(6)):
        print(f"seed {sd} works")
        for k in range(6): print(f"{P[k]} -> {P[d[k]]}")
        break
    sd += 1
