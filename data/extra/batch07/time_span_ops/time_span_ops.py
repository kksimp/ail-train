def sh(t): return f"{t // 60}h{t % 60:02}"
L = [95, 40, 130, 25]; T = sum(L)
print(f"legs: {' + '.join(sh(x) for x in L)} = {sh(T)}"); print(f"left of {sh(300)}: {sh(300 - T)}"); print("shortest to longest: " + " ".join(sh(x) for x in sorted(L)))
