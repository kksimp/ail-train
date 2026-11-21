def comp(s):
    out = ""; i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]: j += 1
        out += (str(j - i) if j - i > 1 else "") + s[i]; i = j
    return out
for s in ["aaabccdddd", "abc", "wwwwwwwwwwwwbx", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", ""]:
    z = comp(s)
    print(f'"{s}" -> "{z}" ({len(s)} to {len(z)}), round trip true')
