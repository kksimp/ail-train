c = [1]
for r in range(1, 11): c = [1] + [c[i - 1] + c[i] for i in range(1, r)] + [1]
t = 0
for i, k in enumerate(c): n = k * 1024 // 1024; t += n; print(f"bin {i:>2}: {n:>3} |{'#' * (n // 6)}")
print(f"{t} beans in {len(c)} bins")
