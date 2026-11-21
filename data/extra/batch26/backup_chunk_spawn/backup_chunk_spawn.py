def rolling(s):
    h = 7
    for ch in s: h = (h * 31 + ord(ch)) % 1000003
    return h
orig = ["header:v2;size=4096", "rows 0-999 of orders", "rows 1000-1999 of orders", "footer:end"]
up = ["header:v2;size=4096", "rows 0-999 of orders", "rows 1000-1999 of 0rders", "footer:end"]
man = [rolling(s) for s in orig]; got = [rolling(s) for s in up]
bad = 0
for i in range(4):
    ok = got[i] == man[i]
    if not ok: bad += 1
    print(f"chunk {i + 1}: {got[i]:>7} vs {man[i]:>7} {'ok' if ok else 'MISMATCH, re-upload'}")
print(f"{bad} of 4 chunks need sending again")
