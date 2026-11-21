def outs(ip):
    parts = ip.split(".")
    whole = int(parts[0])
    thirds = int(parts[1]) if len(parts) > 1 else 0
    return whole * 3 + thirds

lines = [("Alvarez", "6.2", 2, 5, 1), ("Brook", "7.0", 3, 8, 2), ("Chen", "5.1", 4, 6, 3), ("Doyle", "1.2", 1, 2, 1), ("Ekko", "8.1", 0, 4, 0)]
all_outs = 0
all_er = 0
for name, ip, er, hits, walks in lines:
    o = outs(ip)
    all_outs += o
    all_er += er
    era = float(er * 27) / float(o)
    whip = float((walks + hits) * 3) / float(o)
    print(f"{name:<8} IP {ip:>4}  outs {o:>2}  ERA {era:>5.2f}  WHIP {whip:.2f}")
staff = float(all_er * 27) / float(all_outs)
print(f"staff: {all_outs // 3}.{all_outs % 3} innings, ERA {staff:.2f}")
