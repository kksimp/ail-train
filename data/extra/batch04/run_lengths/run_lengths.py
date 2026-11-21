def enc(s):
    o = ""; i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]: j += 1
        o += f"{j - i}{s[i]}"; i = j
    return o
for s in ["aaabccdddd", "abc", "zzzzzzzzzzzz", "hello", "mississippi"]:
    print(f"{s} -> {enc(s)} -> true")
