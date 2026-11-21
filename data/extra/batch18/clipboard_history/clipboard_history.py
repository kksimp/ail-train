h = []
def copy(t):
    global h
    if t in h: h = [x for x in h if x != t]
    h.insert(0, t)
    if len(h) > 4: d = h.pop(); print(f"  (dropped '{d}')")
for t in ["invoice #4471", "kim@site.io", "SELECT * FROM users", "kim@site.io", "+44 20 7946 0958", "https://ail.dev", "invoice #4471"]:
    print(f"copy '{t}'"); copy(t)
print(f"history: {' | '.join(h)}")
print(f"paste 2nd: {h[1]}")
print(f"oldest kept: {h[-1]}")
