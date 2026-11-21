def beaufort(text, key):
    out = []
    i = 0
    for c in text:
        if c.isupper():
            k = ord(key[i % len(key)]) - 65
            v = ((k - (ord(c) - 65)) % 26 + 26) % 26
            out.append(chr(v + 65))
            i += 1
        else:
            out.append(c)
    return "".join(out)

key = "FORTIFICATION"
for msg in ["DEFEND THE EAST WALL", "HOLD FAST", "SEND MORE FLARES"]:
    code = beaufort(msg, key)
    back = beaufort(code, key)
    print(f"{msg:<21} -> {code:<21} -> {back}")
same = beaufort("AAAA", "WXYZ")
print(f"with all A the output is the key itself: {same}")
