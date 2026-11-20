temps = [13, 14, 15, 11, 9, 12, 16, 13]
out = [0] * len(temps); st = []
for i, t in enumerate(temps):
    while st and temps[st[-1]] < t:
        j = st.pop(); out[j] = i - j
    st.append(i)
for i, t in enumerate(temps):
    print(f"day {i + 1}: {t:>2}C " + ("none warmer" if out[i] == 0 else f"wait {out[i]}"))
print(f"longest wait: {max(out)}")
