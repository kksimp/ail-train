partners = [("Atlantis", (420, 130), (380, 90)), ("Borduria", (150, 60), (240, 20)), ("Cascadia", (90, 75), (60, 110))]
tg = ts = 0; worst = ""; wn = 0
for n, e, i in partners:
    g = e[0] - i[0]; s = e[1] - i[1]; net = g + s
    tg += g; ts += s
    print(f"{n:<9} goods {g:>4}, services {s:>4}, net {net:>4}")
    if net < wn: wn = net; worst = n
print(f"overall   goods {tg:>4}, services {ts:>4}, net {tg + ts:>4}")
print(f"biggest deficit: {worst} ({wn})")
