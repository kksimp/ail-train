def r47(s):
    return "".join(chr(33 + (ord(c) - 33 + 47) % 94) if 33 <= ord(c) <= 126 else c for c in s)
for s in ["Hello, World!", "The Quick Brown Fox", "1+1=2", "~!"]:
    e = r47(s)
    print(f"{s} => {e} => {r47(e)}")
