def hyphenate(word, patterns):
    w = "." + word + "."
    points = [0] * (len(w) + 1)
    for p in patterns:
        letters = []
        nums = [0]
        for c in p:
            if c.isdigit():
                nums[len(nums) - 1] = int(c)
            else:
                letters.append(c)
                nums.append(0)
        n = len(letters)
        for i in range(len(w) - n + 1):
            if list(w[i:i + n]) == letters:
                for j in range(n + 1):
                    points[i + j] = max(points[i + j], nums[j])
    out = []
    for k in range(len(word)):
        if k >= 2 and k <= len(word) - 3 and points[k + 1] % 2 == 1:
            out.append("-")
        out.append(word[k])
    return "".join(out)

patterns = ["hy3ph", "he2n", "hena4", "hen5at", "1na", "n2at", "1tio", "2io", "o2n", "1ca", "4m1p", "pu2t", "5pute", "put3er", "1ta", "2bl", "1le", "4ble.", "1ber", "1mo"]
words = ["hyphenation", "computer", "nation", "table", "station", "cucumber", "memorable", "onion"]
breaks = 0
for w in words:
    h = hyphenate(w, patterns)
    breaks += h.count("-")
    print(f"{w:<12} {h}")
print(f"{breaks} break points from {len(patterns)} patterns")
