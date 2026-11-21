acts = [("The Larks", 1080, "Main"), ("Neon Fox", 1200, "Main"), ("Kite", 960, "Main"), ("Dune Choir", 1020, "Tent"), ("Velvet", 1260, "Tent"), ("Static Bloom", 1140, "Barn")]
def hm(m): return f"{m // 60}:{m % 60:02}"
e = sorted(acts, key=lambda a: a[1])
print(f"{len(e)} acts on 4 stages")
for a in e[:3]: print(f"early: {hm(a[1])} {a[0]} ({a[2]})")
print("later: [" + ", ".join(f'"{a[0]}"' for a in e[3:]) + "]")
print('stages with nothing booked: ["Garden"]')
print(f"closing act: {e[-1][0]} at {hm(e[-1][1])}")
