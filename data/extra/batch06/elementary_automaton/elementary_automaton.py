for ru in [30, 90, 110]:
    print(f"rule {ru}:"); R = [False] * 31; R[15] = True
    for _ in range(12):
        print("".join("#" if b else "." for b in R)); N = [False] * 31
        for i in range(1, 30): N[i] = (ru >> ((4 if R[i - 1] else 0) + (2 if R[i] else 0) + (1 if R[i + 1] else 0))) & 1 == 1
        R = N
