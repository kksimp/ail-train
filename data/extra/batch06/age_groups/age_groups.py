A = [34, 7, 61, 45, 23, 38, 19, 72, 41, 29, 33, 56, 12, 48, 37, 66, 25, 31]; B = {}
for a in A: B[a // 10 * 10] = B.get(a // 10 * 10, 0) + 1
for b in sorted(B): print(f"{b:>2}-{b + 9:<2} {'#' * B[b]}")
s = sorted(A); n = len(s); m = float(s[n // 2]) if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2; print(f"median {m:.1f}")
