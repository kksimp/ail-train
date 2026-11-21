I = [(0, "File"), (1, "New"), (1, "Open"), (2, "Recent"), (2, "Browse"), (1, "Save"), (0, "Edit"), (1, "Undo"), (1, "Find"), (2, "Replace"), (3, "Regex"), (0, "Help")]; C = [0] * 4; dp = (0, "")
for d, l in I:
    C[d] += 1
    for k in range(d + 1, 4): C[k] = 0
    print("  " * d + ".".join(map(str, C[:d + 1])) + f" {l}")
    if d > dp[0]: dp = (d, l)
print(f"deepest: {dp[1]} at level {dp[0] + 1}")
