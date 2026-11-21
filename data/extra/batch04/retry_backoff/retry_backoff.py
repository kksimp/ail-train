for s in [[False, False, True], [True], [False] * 7, [False] * 5 + [True]]:
    w = 1; wd = 0; t = 0; ok = False
    while t < 6:
        t += 1
        if (s[t - 1] if t - 1 < len(s) else False): ok = True; break
        if t < 6: wd += w; w = min(w * 2, 30)
    print(f"{'succeeded' if ok else 'gave up'} after {t} tries, waited {wd}s")
