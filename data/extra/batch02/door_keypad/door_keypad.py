keys = "1234 12*4321 1111 2222 3333 xxx 4321"
st = ("Idle",); misses = 0; opens = 0
def press(s, k):
    global misses
    if s[0] == "Open": return ("Idle",)
    if s[0] == "Locked": return ("Locked", s[1] - 1) if s[1] > 1 else ("Idle",)
    if s[0] == "Idle": return ("Typing", k) if k.isdigit() else ("Idle",)
    if k == "*": return ("Idle",)
    c = s[1] + k
    if len(c) < 4: return ("Typing", c)
    if c == "4321":
        misses = 0; return ("Open",)
    misses += 1
    if misses >= 3:
        misses = 0; return ("Locked", 3)
    return ("Idle",)
def show(s):
    return {"Idle": "idle", "Open": "OPEN"}.get(s[0]) or (f"typing {'*' * len(s[1])}" if s[0] == "Typing" else f"locked ({s[1]})")
for k in keys:
    if k == " ": continue
    st = press(st, k)
    if st[0] == "Open": opens += 1
    print(f"{k} -> {show(st)}")
print(f"opened {opens} times")
